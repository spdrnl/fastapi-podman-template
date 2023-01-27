from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Serve a hello world at the root"""
    return {"Hello": "World"}
