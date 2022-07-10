import asyncio
import websockets
import json
import time
import queue
import copy
import httplib2
import os
import sys

from threading import Thread
from threading import Lock
from threading import Event

import os
import codecs

data = {"version":1,"reqid":1,"msgtype":3001,"time":1640594905,"identity":2,"code":0,"message":"","data":[]}
uploadurl="https://crm-wechat-callback.baidao.com/crm-wechat-callback/api/v1/task/updateStatus"
usersign="unknown"

def InitConfigData():
    localUserSign="unknown"
    msgType=[26]
    # determine if application is a script file or frozen exe+3223136
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(os.path.abspath(__file__))

    filePath = os.path.join(os.path.dirname(application_path), "Data\DI02.data")
    print(filePath)
    try:
        with open(filePath, 'r') as configFile:
            configData = json.load(configFile)
            for configItem in configData:
                if "softname" not in configItem:
                    continue
                if configItem["softname"].lower() != "crm":
                    break
                if "usersign" in configItem :
                    localUserSign=configItem["usersign"]
                if "msgtype" in configItem :
                    msgType=configItem["msgType"]
    except Exception as e:
        print(e)
    return  localUserSign, msgType
class MgrDataThread(Thread):
    def __init__(self, queue, dataLock, cache):
        Thread.__init__(self)
        self.m_queue = queue
        self.m_dataLock = dataLock
        self.m_cache = cache
    def run(self):
        while True:
            try:
                data = self.m_queue.get(block=True)
                jsonData = json.loads(data)
                msgType = jsonData["msgtype"]
                statData={}
                if msgType == 26:
                    msgData = jsonData["data"]
                    key=msgData["taskid"]
                    statData["taskId"] = key
                    #statData["createTime"] = msgData["createTime"]
                    statData["startTime"] = msgData["starttime"]
                    statData["finishTime"] = msgData["finishtime"]
                    statData["successNum"] = msgData["successnum"]
                    statData["failNum"] = msgData["failnum"]
                    statData["excuteNum"] = msgData["excutenum"]
                    statData["invalidNum"] = msgData["invalidnum"]
                    statData["sendStatus"] = msgData["status"]
                    statData["percent"] = msgData["percent"]
                    statData["operEmpId"] = usersign
                    self.m_dataLock.acquire()
                    finish = False
                    for keyMsg, valueMsg in self.m_cache.items():
                        if keyMsg == msgType :
                            self.m_cache[msgType][key] = statData
                            finish = True
                    if finish == False:
                        dataTmp={}
                        dataTmp[key] = statData
                        self.m_cache[msgType] = dataTmp
                    self.m_dataLock.release()
            except Exception as e:
                continue

class UploadDataThread(Thread):
    def __init__(self, cache, dataLock):
        Thread.__init__(self)
        self.m_cache = cache
        self.m_dataLock = dataLock


    def run(self):
        while True:
            time.sleep(120)
            try:
                self.m_dataLock.acquire()
                dictData = copy.deepcopy(self.m_cache)
                self.m_cache.clear()
                self.m_dataLock.release()
                if not dictData:
                    print("数据为空")
                    continue
                for key, value in dictData.items():
                    if key == 26:
                        msgBody=[]
                        for keyData, valueData in value.items():
                            msgBody.append(valueData)
                        if not msgBody:
                            continue
                        head = {"Content-Type": "application/json",
                                "jobnumber": usersign}
                        http = httplib2.Http()
                        body = json.dumps(msgBody)
                        print(body)
                        response, content = http.request(uploadurl, "POST", body, head)
                        jsonData = json.loads(content)
                        print(jsonData)
            except Exception as e:
                return

# 客户端主逻辑
async def main_logic():
    usersign1, data["data"]=InitConfigData()
    global usersign
    usersign = usersign1
    print("用户类型：", usersign)
    print("监听消息：", data)

    dataLock = Lock()
    recvQueue = queue.Queue()
    dataCache = {}
    mgrThread = MgrDataThread(recvQueue, dataLock, dataCache)
    uploadThread = UploadDataThread(dataCache, dataLock)
    mgrThread.start()
    uploadThread.start()
    while True:
        try:
            async with websockets.connect('ws://127.0.0.1:17580') as websocket:
                jsonData = json.dumps(data, ensure_ascii=False, indent=1)
                await websocket.send(jsonData)
                while True:
                    recvText = await websocket.recv()
                    recvQueue.put(recvText)
        except Exception as e:
            websockets.close()
            print("连接断开")
            continue
        time.sleep(2)