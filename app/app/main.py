import uvicorn
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, status
from config import load_config, Config
import os
app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
async def hello():
    config_obj: Config = load_config()
    ret = f'''<html><body><h2>Hello World!
    port database : {config_obj.db.port}</h2>
    <h4>{os.listdir(path=".")}<h4></body></html>'''

    return HTMLResponse(content=ret)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)
