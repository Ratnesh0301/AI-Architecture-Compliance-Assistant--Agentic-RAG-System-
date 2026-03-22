from app.llm.llm import get_llm_response
from app.rag.retriever import retrieve_context

def analyze_doc(state):
    prompt = f"""
    Analyze this architecture document:
    {state['document']}
    Extract key components.
    """
    result = get_llm_response(prompt)
    return {"context": result}

def check_compliance(state):
    prompt = f"""
    Compare architecture with rules:

    Architecture:
    {state['context']}

    Rules:
    {state['rules']}

    Identify violations and risks.
    """
    result = get_llm_response(prompt)
    return {"report": result}

def generate_report(state):
    prompt = f"""
    Generate structured compliance report:

    {state['report']}

    Format:
    - Issues
    - Severity
    - Recommendations
    """
    final = get_llm_response(prompt)
    return {"report": final}