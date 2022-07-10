# -*- coding:utf-8 -*-

import websocket,sys,time,json
from websocket import WebSocketApp
import _thread as thread
from loguru import logger

def loggerConsole(logDetail=0):
    if not logDetail:
        logger.remove(0)
        logger.add(sys.stdout,
                   level="DEBUG", colorize=True,
                   format='<yellow>{time:YYYY-MM-DD HH:mm:ss.SSS}</> | <level>{message}</>')

def loggerFile(*args):
    filename = f"datas/{'.'.join(args)}.log"
    logger.add(filename, level="DEBUG", rotation="200 MB", encoding='utf-8',
               format='{time:YYYY-MM-DD HH:mm:ss.SSS} | {message}')

def on_message(ws, message):
    try:
        message=json.loads(message)
    except BaseException as e:
        logger.error(e)
    else:
        if "msgtype" in message.keys():
            msg=message["msgtype"]
            if msg==3001:
                logger.info(f"[注册监听消息] - {message}")
            elif msg==20:
                logger.info(f"[用户上线] - {message}")
            elif msg==21:
                logger.info(f"[用户下线] - {message}")
            elif msg==22:
                logger.info(f"[账户信息更新] - {message}")
            elif msg==26:
                logger.info(f"[任务进度更新] - {message}")
            else:
                logger.info(message)


def on_error(ws, error):
    logger.error(error)

def on_close(ws, close_status_code, close_msg):
    logger.debug("连接断开")

def on_open(ws):
    logger.debug(f"连接服务器: {ws.url}")

    msg='{"version":1,"reqid":1,"msgtype":3001,"time":1640594905,"identity":2,"code":0,"message":"","data":[20,21,22,26]}'
    ws.send(msg)

    # thread.start_new_thread(run, (ws,))

def run(ws, *args):
    while True:
        time.sleep(1)
        input_msg = input("输入要发送的消息（ps：输入关键词 e 结束程序）:\n")
        if input_msg == "e":
            ws.close()  # 关闭
            print("thread terminating...")
            break
        else:
            ws.send(input_msg)

if __name__ == '__main__':
    loggerConsole()
    logsuffix = [time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))]
    loggerFile(*logsuffix)

    websocket.enableTrace(False)  # 开启运行状态追踪。debug 的时候最好打开他，便于追踪定位问题。

    ws = WebSocketApp("ws://127.0.0.1:17580",
                    on_open=on_open,
                    on_message=on_message,
                    on_error=on_error,
                    on_close=on_close)

    ws.run_forever(ping_interval=30,ping_timeout=10)

