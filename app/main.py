import uvicorn
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, status

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
async def hello():
    ret = '''<html><body><h2>Hello World!</h2></body></html>'''

    return HTMLResponse(content=ret)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)
