from fastapi import APIRouter,Request,Form,Depends,status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine,get_db
import models
from sqlalchemy.orm import Session
from jwt import get_current_user
from database import get_db
from schemas import User

router=APIRouter(
    prefix="/me/edit"
)
templates = Jinja2Templates(directory="templates")
#to update or edit data
@router.get("/username",response_class=HTMLResponse,status_code=status.HTTP_200_OK)
async def edit_username(request:Request,username:str,db:Session=Depends(get_db),active_user: User = Depends(get_current_user)):
    user=db.query(models.Users).filter(models.Users.email==active_user.email)
    updated_name=user.update({"username":username}, synchronize_session=False)
    db.commit()
    return templates.TemplateResponse("me.html", context={"request":request,"username":username,"email":active_user.email,"address":active_user.address})


@router.get("/email",response_class=HTMLResponse,status_code=status.HTTP_200_OK)
async def edit_username(request:Request,email:str,db:Session=Depends(get_db),active_user: User = Depends(get_current_user)):
    user=db.query(models.Users).filter(models.Users.email==active_user.email)
    updated=user.update({"email":email}, synchronize_session=False)
    db.commit()
    return templates.TemplateResponse("index.html", context={"request":request,"username":active_user.username,"email":email,"address":active_user.address,"message":"Since email was changed refresh your token","tag":"warning"})

@router.get("/address",response_class=HTMLResponse,status_code=status.HTTP_200_OK)
async def edit_username(request:Request,address:str,db:Session=Depends(get_db),active_user: User = Depends(get_current_user)):
    user=db.query(models.Users).filter(models.Users.email==active_user.email)
    updated=user.update({"address":address}, synchronize_session=False)
    db.commit()
    return templates.TemplateResponse("me.html", context={"request":request,"username":active_user.username,"email":active_user.email,"address":address})

#to delete
@router.get("/delete/username",response_class=HTMLResponse,status_code=status.HTTP_204_NO_CONTENT)
async def edit_username(request:Request,db:Session=Depends(get_db),active_user: User = Depends(get_current_user)):
    user=db.query(models.Users).filter(models.Users.email==active_user.email)
    updated_name=user.update({"username":""}, synchronize_session=False)
    db.commit()
    return templates.TemplateResponse("me.html", context={"request":request,"username":"","email":active_user.email,"address":active_user.address})

@router.get("/delete/email",response_class=HTMLResponse,status_code=status.HTTP_204_NO_CONTENT)
async def edit_username(request:Request,db:Session=Depends(get_db),active_user: User = Depends(get_current_user)):
    user=db.query(models.Users).filter(models.Users.email==active_user.email)
    updated=user.update({"email":""}, synchronize_session=False)
    db.commit()
    return templates.TemplateResponse("index.html", context={"request":request,"username":active_user.username,"email":"","address":active_user.address,"message":"Email has been deleted, Register a new account","tag":"danger"})

@router.get("/delete/address",response_class=HTMLResponse,status_code=status.HTTP_204_NO_CONTENT)
async def edit_username(request:Request,db:Session=Depends(get_db),active_user: User = Depends(get_current_user)):
    user=db.query(models.Users).filter(models.Users.email==active_user.email)
    updated=user.update({"address":""}, synchronize_session=False)
    db.commit()
    return templates.TemplateResponse("me.html", context={"request":request,"username":active_user.username,"email":active_user.email,"address":""})

