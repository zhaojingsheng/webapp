import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time,aiomysql
from datetime import datetime
from logging import log

from aiohttp import web
routes=web.RouteTableDef()

@routes.get("/")
async  def index(request):
    return web.Response(body=b'<h1>test</h1>',content_type="text/html")

def init():
    app=web.Application()
    app.add_routes(routes)
    logging.info('server started at http://127.0.0.1:9000...')
    web.run_app(app,host="127.0.0.1",port=9000)

init()
