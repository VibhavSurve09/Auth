from fastapi import APIRouter,Request,Form,Depends,status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine,get_db
import models
from sqlalchemy.orm import Session
from hashing import verify_password,get_password_hash
from database import get_db
router=APIRouter(
    prefix="/signup",
)

models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

@router.get("/",response_class=HTMLResponse,status_code=status.HTTP_200_OK)
async def signin_(request:Request):
    return templates.TemplateResponse("signup.html", context={"request": request})

@router.post("/",response_class=HTMLResponse,status_code=status.HTTP_201_CREATED)
async def handle_signin(request:Request,username: str = Form(...), email:str=Form(...),password: str = Form(...),address:str=Form(...),db:Session=Depends(get_db)):
    old_email=db.query(models.Users).filter(models.Users.email==email).first()
    old_user=db.query(models.Users).filter(models.Users.username==username).first()
    if old_email:
        return templates.TemplateResponse("signup.html", context={"request":request,"message":"Email already exists","tag":"warning"})
    if old_user:
        return templates.TemplateResponse("signup.html", context={"request":request,"message":"Username already exists","tag":"warning"})
    hashed_password=await get_password_hash(password)
    new_user = models.Users(username=username,email=email, address=address,password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return templates.TemplateResponse("index.html", context={"request": request,"message":"Your account has been created successfully","tag":"success"})
