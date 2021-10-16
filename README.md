
# Auth

Authentication and Authorization system using JWT in Python.


![Logo](https://user-images.githubusercontent.com/73296863/137582997-0e1b0868-0116-43ce-b92e-5b3798e283d3.jpeg)

    
## Run Locally

Clone the project

```bash
  git clone https://github.com/Vibhav0/Auth.git
```

Go to the project directory

```bash
  cd Auth
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
 uvicorn main:app --reload
```

  
## API Reference

#### To edit user details user should be logged to genrate JWT token

```http/https
  GET /me/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `token` | `str(session_cookie)` | **Required**.  To edit details |


  
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

`ALGORITHM`

To generate a secure random secret key use the command:
```bash
openssl rand -hex 32
```
`ALGORITHM`=`HS256`
  
## Acknowledgements

 - [FastAPI](https://fastapi.tiangolo.com/)
 - [Nginx and FastAPI](https://techoff.live/how-to-host-fastapi-application-using-uvicorn-nginx/)

  
## Feedback

If you have any feedback, please reach out to me at survevibhav09@gmail.com

  
