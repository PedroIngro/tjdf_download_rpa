from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from mecanismo import rpa_process_function

app = FastAPI()

# Montar o diretório 'static' para servir arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar o diretório de templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/start-api")
async def start_api():
    rpa_process_function()
    
