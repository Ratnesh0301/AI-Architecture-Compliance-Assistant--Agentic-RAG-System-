from fastapi import FastAPI, UploadFile, File
from app.agent.graph import build_graph
from app.utils.rules_loader import load_rules

app = FastAPI()
graph = build_graph()

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    document = content.decode()

    rules = load_rules()

    result = graph.invoke({
        "document": document,
        "rules": rules,
        "context": "",
        "report": ""
    })

    return {"report": result["report"]}