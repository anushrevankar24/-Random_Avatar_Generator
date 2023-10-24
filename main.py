from dicebear import DAvatar, DStyle, DFormat
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates =Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def welcome_message(request: Request):
    return templates.TemplateResponse("landing_page.html", {"request": request})

@app.get("/getting-started", response_class=HTMLResponse)
async def getting_started(request: Request):
    return templates.TemplateResponse("getting_started.html", {"request": request})
@app.get("/{seed}")
async def generate_avatar(request: Request, seed: str, format: str = "svg"):
    if format not in ["svg", "png"]:
        return {"error": "Invalid format. Choose from 'svg' or 'png.'"}
    
    avatar = DAvatar(seed=seed, style=DStyle.random())
    
    if format == "svg":
        return templates.TemplateResponse("display_avatar.html", {"request": request, "avatar_url": avatar.url_svg})
    else:
        return templates.TemplateResponse("display_avatar.html", {"request": request, "avatar_url": avatar.url_png})

@app.get("/generate")
async def input_form(request: Request):
    return templates.TemplateResponse("input_form.html", {"request": request})
