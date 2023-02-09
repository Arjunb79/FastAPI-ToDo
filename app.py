import uvicorn
from fastapi import FastAPI

from scripts.config.application_config import port_no

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", port=int(port_no), reload=True)
