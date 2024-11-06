from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from api.graph import chain  
from fastapi.middleware.cors import CORSMiddleware
from api.rephrase import rephrase_query_for_schema
import uvicorn
app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/test")
async def test():
    return "Test...🔥"
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","https://nlp-group35.vercel.app"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
@app.post("/query")
async def query_graph(request: QueryRequest):
    try:
        rephrased_query = rephrase_query_for_schema(request.query)
        result = chain.invoke({"query": rephrased_query})
        print(result)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        log_level="debug",
        reload=True,
    )
