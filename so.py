import asyncio
import sys

import websockets
import datetime
import json
async def hello():
    async with websockets.connect("wss://stream.binance.me/stream") as websocket:
        await websocket.send('{"id":1011,"params":["!miniTicker@arr"],"method":"SUBSCRIBE"}')
        while True:
            msg = await websocket.recv()
            try:
                time = int(json.loads(msg)['data'][0]['E'])
                rtime = datetime.datetime.fromtimestamp(time/1000.0)
                #dt = datetime.datetime.fromtimestamp(time)
                print(str(datetime.datetime.now())+"," +str(rtime)+","+ str(msg)+";" )
            except Exception:
                print("error")

                e = sys.exc_info()[1]
                print(e.args[0])

asyncio.get_event_loop().run_until_complete(hello())