from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from router import machine, machinerepairhistory, maps, peripherals, users
import uvicorn
import models
from db import engine


app = FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(machine.router)
app.include_router(machinerepairhistory.router)
app.include_router(maps.router)
app.include_router(peripherals.router)
app.include_router(users.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)

# gunicorn -k uvicorn.workers.UvicornWorker --access-logfile ./gunicorn-access.log main:app --bind 0.0.0.0:8000 --workers 2 --daemon
