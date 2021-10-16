from fastapi import APIRouter,Request,Form,Depends,status
from fastapi.responses import HTMLResponse,Response,RedirectResponse
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine,get_db
import models
from sqlalchemy.orm import Session
from jwt import create_access_token
from fastapi.security import APIKeyCookie
from hashing import verify_password
router=APIRouter(
    prefix="/login",
)

templates = Jinja2Templates(directory="templates")

@router.get("/",response_class=HTMLResponse,status_code=status.HTTP_200_OK)
async def login_(request:Request):
    return templates.TemplateResponse("index.html", context={"request": request})


@router.post("",response_class=RedirectResponse,status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def authenticateUser(request:Request,response: Response,email:str=Form(...),password:str=Form(...),db:Session=Depends(get_db)):
    user=db.query(models.Users).filter(models.Users.email==email).first()
    if not user:
       return templates.TemplateResponse("index.html", context={"request":request,"message":"User does not exist","tag":"warning"})
    isCorrect=await verify_password(password,user.password)
    if not isCorrect:
        return templates.TemplateResponse("index.html", context={"request":request,"message":"Invalid Credentials","tag":"danger"})
    token=await create_access_token(data={"sub":email})
    response.set_cookie("session", token)
    return ("/me")



