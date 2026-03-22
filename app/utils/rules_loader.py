import os

def load_rules():
    rules = []
    for file in os.listdir("data/rules"):
        with open(f"data/rules/{file}", "r") as f:
            rules.append(f.read())
    return "\n".join(rules)