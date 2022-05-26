from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import socket

from dataclasses import dataclass, asdict, field
import os
import json

@dataclass
class Client:
  name: str = ""
  place: str = ""
  tvs_count: int = 0
  ip: str = ""

  def __post_init__(self):
    self.ip = self.__set_ip()

  def __set_ip(self) -> str:
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def pre_init():
  client_json = {}

  if os.path.exists("client.json"):
    with open("client.json", mode="r", encoding="UTF-8") as json_file:
      client_json = json.load(json_file)

  client = Client(**client_json)

  # TODO: Отправка информации о клиенте на сервер
  # client.register()

  with open("client.json", mode="w+", encoding="UTF-8") as json_file:
    json.dump(asdict(client), json_file)

pre_init()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})

@app.post("/play")
async def play():
  pass

@app.post("/pause")
async def pause():
  pass

@app.post("/stop")
async def stop():
  pass

@app.get("/info")
async def get_info():
  pass