from fastapi import FastAPI

app = FastAPI()

# domain:  http://127.0.0.1:8000, Swagger UI :  http://127.0.0.1:8000/docs
@app.get('/')
def root():
    return {'message' : "Hello"}