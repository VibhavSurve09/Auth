from fastapi import APIRouter,Request,Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine,get_db
import models
from sqlalchemy.orm import Session
from jwt import get_current_user
from schemas import User
router=APIRouter(
    prefix="/me",
)

templates = Jinja2Templates(directory="templates")
models.Base.metadata.create_all(bind=engine)

@router.get("/",response_class=HTMLResponse)
async def user_(request:Request,active_user: User = Depends(get_current_user)):
    return templates.TemplateResponse("me.html", context={"request": request,"username":active_user.username,"email":active_user.email,"address":active_user.address})

@router.post("/",response_class=HTMLResponse)
async def user_(request:Request,active_user: User = Depends(get_current_user)):
    return templates.TemplateResponse("me.html", context={"request": request,"username":active_user.username,"email":active_user.email,"address":active_user.address})

