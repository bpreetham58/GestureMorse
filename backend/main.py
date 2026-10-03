from fastapi import FastAPI

app = FastAPI(title="GestureMorse API")


@app.get("/")
def root():
    return {"message": "GestureMorse Backend is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}