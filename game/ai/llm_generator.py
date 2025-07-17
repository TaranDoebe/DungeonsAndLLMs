import requests
import re

LLM_CHAT_URL = "http://localhost:1234/v1/chat/completions"
LLM_COMPLETION_URL = "http://localhost:1234/v1/completions"
MODEL_NAME = "meta-llama-3-8b-instruct"  # or whatever model name is shown in LM Studio

def call_llm(prompt, max_tokens=100):
    url = "http://localhost:1234/v1/completions"

    payload = {
        "model": "meta-llama-3-8b-instruct",  # Or match what you see in LM Studio
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": 0.7
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["text"].strip()
    except Exception as e:
        print("❌ Failed to interpret input:", e)
        return "unknown"

def generate_monster(prompt, max_tokens=256):
    """
    Uses chat format to generate a JSON-formatted monster.
    """
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are an API that generates fantasy monsters in JSON format."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.8,
        "max_tokens": max_tokens
    }

    try:
        response = requests.post(LLM_CHAT_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        print("❌ LLM monster generation failed:", e)
        return ""

def generate_story_text(prompt, max_tokens=300):
    """
    Uses completion-style prompt to generate narrative story events.
    """
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": 0.9
    }

    try:
        response = requests.post(LLM_COMPLETION_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["text"].strip()
    except Exception as e:
        print("❌ LLM story generation failed:", e)
        return ""

def clean_llm_output(raw: str) -> str:
    """
    Extracts first JSON-like block from LLM output. Used to clean up monster responses.
    """
    # Try extracting JSON inside code block
    match = re.search(r"```(?:json)?\s*({.*?})\s*```", raw, re.DOTALL)
    if match:
        return match.group(1)

    # Fallback: naive JSON block
    match = re.search(r"{.*}", raw, re.DOTALL)
    if match:
        return match.group(0)

    return ""
