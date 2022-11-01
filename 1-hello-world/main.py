from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def helloWorld():
    return {"msg": "Hello World"}


if __name__ == "__main__":
    import uvicorn
                            # host="0.0.0.0" -> acessivel para rede local
    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level="info", reload=True)
