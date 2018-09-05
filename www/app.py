import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time,aiomysql
from datetime import datetime
from logging import log
import aiohttp_jinja2
from aiohttp import web
routes=web.RouteTableDef()
import jinja2

@routes.get("/")
@aiohttp_jinja2.template("index.html")
async def index(request):
    return {}

def init():
    app=web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(r".\static"))
    app.add_routes(routes)
    logging.info('server started at http://127.0.0.1:9000...')
    return app


web.run_app(init(),port=9000)
