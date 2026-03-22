from langgraph.graph import StateGraph
from app.agent.state import GraphState
from app.agent.nodes import analyze_doc, check_compliance, generate_report

def build_graph():
    builder = StateGraph(GraphState)

    builder.add_node("analyze", analyze_doc)
    builder.add_node("compliance", check_compliance)
    builder.add_node("report", generate_report)

    builder.set_entry_point("analyze")

    builder.add_edge("analyze", "compliance")
    builder.add_edge("compliance", "report")

    return builder.compile()