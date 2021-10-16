from fastapi import APIRouter,Response,status,Request
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
router=APIRouter(
    prefix="/logout",
)
templates = Jinja2Templates(directory="templates")
#logout
@router.get("/",response_class=RedirectResponse,status_code=status.HTTP_200_OK)
async def logout(response: Response,request:Request):
    response=templates.TemplateResponse("index.html", context={"request":request})
    response.delete_cookie("session")
    return response
