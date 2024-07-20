from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn
from readJSON import load_json
from renderHTML import render_html

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/json", StaticFiles(directory="json"), name="json")

@app.get('/', response_class=HTMLResponse)
async def name(request: Request):
    json_dict = load_json("./json/resume.json")
    return templates.TemplateResponse("resume.html", {"request": request, **json_dict})

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)