from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import socket

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
  hostname = socket.gethostname()
  local_ip = socket.gethostbyname(hostname)

  return templates.TemplateResponse("index.html", {"request": request, "ip": local_ip})
