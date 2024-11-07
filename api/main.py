from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from api.graph import chain 
from fastapi.middleware.cors import CORSMiddleware
from api.test_prompt import rephrase_query_for_schema
from api.extract_entities import entity_extraction_chain
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
        print(result['query'])

        return {
            "query" : result['query'],
            "result" : result['result']
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.post("/description")
def extract_entities_from_description(request: QueryRequest):
    print(request)
    """
    Extract entities from a description using LangChain with OpenAI.
    """
    response = entity_extraction_chain.invoke({"description": request.query})
    
    response_text = response.get("text", "")

    response_data = {}
    for line in response_text.strip().split("\n"):
        try:
            key, value = line.split(": ", 1)
            response_data[key] = value.strip()
        except ValueError:
            continue  
        
    expected_keys = [
        "Operating_System", "Software_Component", "Version", "Impact", 
        "Affected_Hardware", "Network_Requirements", "Affected_Protocols", 
        "Authentication_Required", "Privileges_Required", 
        "User_Interaction_Required", "Vendor"
    ]
    for key in expected_keys:
        response_data.setdefault(key, "NaN")

    return response_data

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        log_level="debug",
        reload=True,
    )
