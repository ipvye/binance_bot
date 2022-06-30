# PURPOSE: websocket stream from binance for BTCUSDT pair. No Kline graphs.
#          updated every second @ 2000ms update speed.
# To Do: (1) Look into the column header signs. (2) 

import websocket  # requires websocket-client to be installed.
import json
import pandas as pd  # requires pandas to be installed.
from collections import OrderedDict
import asyncio



def on_message(in_time_data, message):
    print(message)
    in_time_data.send(json.dumps(in_time_data))

def on_close(in_time_data):
    print("connection closed.")

socket = f'wss://stream.binance.com:9443/ws/btcusdt@kline_1m'

"""socket = f'wss://stream.binance.com:9443/ws'
"""

in_time_data = websocket.WebSocketApp(socket,
                                    on_message=on_message,
                                    on_close=on_close)

"""df = pd.DataFrame(rawdata[-1])"""

"""ws_json = json.dumps(ws)
ws_dict = json.loads(ws_json)

file = json.dumps(in_time_data)
"""

"""in_time_data.run_forever(ping_interval=1)
"""


in_time_data.run_forever()


"""# Empty DF to append info into using asyncio.
df = pd.DataFrame(columns=['e', 'E', 's', 'k', 'T', 's', 'i', 'f', 'L', 'o', 'c', 'h', 'l', 'v', 'n', 'x', 'q', 'V', 'Q', 'B'])

@asyncio
async def socket(uri, ):"""








"""# PURPOSE: websocket stream from binance for BTCUSDT pair. No Kline graphs.
#          updated every second @ 2000ms update speed.

import websocket  # requires websocket-client.
# websocket-client => https://github.com/websocket-client/websocket-client
# websocket (2010) => https://pypi.org/project/websocket/
# binance repo     => https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md

def on_message(ws, message):
    print(message)

def on_close(ws):
    print("connection closed.")


socket = f'wss://stream.binance.com:9443/ws/btcusdt@kline_1m'
ws = websocket.WebSocketApp(socket,
                                on_message=on_message,
                                on_close=on_close)
ws.run_forever()"""