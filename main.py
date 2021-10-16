from fastapi import FastAPI,Request,status
from fastapi.staticfiles import StaticFiles
from routers import signup,login,user,edit,logout
from fastapi.responses import RedirectResponse
app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(signup.router)
app.include_router(login.router)
app.include_router(user.router)
app.include_router(edit.router)
app.include_router(logout.router)

@app.get("/",response_class=RedirectResponse,status_code=status.HTTP_307_TEMPORARY_REDIRECT)
def redirect_to_login(request:Request):
    redirect_url="/login/"
    return redirect_url
