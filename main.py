from fastapi import FastAPI
import uvicorn
from config.environments import parameter_store

from modules.user.router import user_route 

app = FastAPI()
app.title = "Todo fast api"
app.version = "0.0.1"
app.include_router(user_route)

def run():
    hot_reload = True
    if parameter_store["ENV"] == "Production":
        hot_reload = False
    uvicorn.run("main:app", host=parameter_store["HOST"], port=int(parameter_store["PORT"]), reload=hot_reload)

if __name__ == "__main__":
    run()