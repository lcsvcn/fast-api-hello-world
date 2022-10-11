
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class NumbersRequest(BaseModel):
    a: float
    b: float


@app.get('/hello_world')
async def hello_world():
    return {'mensagem': 'hello world'}


@app.post('/somar')
async def sum(
    request: NumbersRequest,
):
    return request.a + request.b


@app.post('/subtrair')
async def sum(
    request: NumbersRequest,
):
    return request.a - request.b

if __name__ == "__main__":
    uvicorn.run("api.application:app", reload=True)