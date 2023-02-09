import uvicorn
from fastapi import FastAPI

from scripts.config.application_config import port_no
from scripts.services.todo import router

app = FastAPI()
app.include_router(router)
if __name__ == "__main__":
    uvicorn.run(app, port=int(port_no))
