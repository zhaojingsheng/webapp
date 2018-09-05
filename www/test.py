# import aiohttp
# import asyncio
# async def go(URL,params):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(URL,params=params) as resp:
#             print(resp.url)
#             # print(await resp.text())
#
#
# URL="https://so.csdn.net/so/search/s.do"
# params={"q":"aiohttp","t":"blog","u":"ydyang1126"}
# loop=asyncio.get_event_loop()
# tasks=[asyncio.ensure_future(go(URL,params))]
# loop.run_until_complete(asyncio.gather(*tasks))
# loop.close()
import asyncio
from aiomysql import create_pool
async def go():
    async with create_pool(host="10.92.1.121",port=3306,
                           user="pyweb",password="pyweb",
                           db="pyweb",loop=loop) as pool:
        async with pool.get() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT VERSION();")
                value = await cur.fetchone()
                print(value)

loop=asyncio.get_event_loop()
loop.run_until_complete(go())