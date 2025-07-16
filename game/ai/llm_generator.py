import requests
import re

def generate_monster(prompt, max_tokens=256):
    url = "http://localhost:1234/v1/chat/completions"

    payload = {
        "model": "meta-llama-3-8b-instruct",  # This must match the model name shown in LM Studio
        "messages": [
            {
                "role": "system",
                "content": "You are an API that generates fantasy monsters in JSON format."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.8,
        "max_tokens": max_tokens
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        print("❌ LLM request failed:", e)
        return ""

def clean_llm_output(raw: str) -> str:
    """
    Extract the first JSON-like block from the LLM response.
    Removes Markdown, explanations, etc.
    """
    # Try extracting code block between triple backticks
    code_block = re.search(r"```(?:json)?\s*({.*?})\s*```", raw, re.DOTALL)
    if code_block:
        return code_block.group(1)

    # Fallback: Extract any JSON-looking block
    inline_json = re.search(r"{.*}", raw, re.DOTALL)
    if inline_json:
        return inline_json.group(0)

    return ""
