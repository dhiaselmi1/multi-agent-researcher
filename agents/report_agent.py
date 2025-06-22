import requests
def generate_report(summary: str, corrections: str) -> str:
    prompt = f"""Using the summary and fact check comments below, write a final research report:
    Summary:\n{summary}
    Corrections:\n{corrections}
    """
    response = requests.post("http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": prompt, "stream": False})
    return response.json()["response"].strip()