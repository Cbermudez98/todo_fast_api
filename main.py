from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/")
def hello_world():
    return HTMLResponse(content="<h1>Hello world</h1>")

def run():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    run()