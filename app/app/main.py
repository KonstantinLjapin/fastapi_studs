import uvicorn
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, status
from utils.some import some
from utils.config import Config, load_config
from utils.db_worker import make_connection_string
import os
app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
async def hello():
    config_obj: Config = load_config()
    ret = f'''<html><body><h2>Hello World!
    port database : {config_obj.db.port}</h2>
    <h4>{os.listdir(path=".")}<h4>
    <h5>{make_connection_string(config_obj)}<h5>
    <h6>{some}<h6></body></html>'''

    return HTMLResponse(content=ret)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)
