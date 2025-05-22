from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import pandas as pd

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/info", response_class=HTMLResponse)
async def read_info(request:Request):
    return templates.TemplateResponse("info.html",{"request":request})

@router.get("/comportamiento", response_class=HTMLResponse)
async def read_comportamiento(request:Request):
    return templates.TemplateResponse("comportamiento.html",{"request":request})

@router.get("/info_dueño", response_class=HTMLResponse)
async def read_infodueno(request:Request):
    return templates.TemplateResponse("info_dueno.html",{"request":request})