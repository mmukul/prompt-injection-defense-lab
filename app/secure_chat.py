import requests
from security_rules import is_prompt_safe, is_response_safe, SECURITY_SYSTEM_PROMPT

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"


def ask_ollama(user_prompt: str) -> str:
    if not is_prompt_safe(user_prompt):
        return "BLOCKED: Unsafe prompt injection attempt detected."

    full_prompt = f"""
{SECURITY_SYSTEM_PROMPT}

User request:
{user_prompt}

Safe assistant response:
"""

    payload = {
        "model": MODEL,
        "prompt": full_prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)
    response.raise_for_status()

    llm_response = response.json().get("response", "")

    if not is_response_safe(llm_response):
        return "BLOCKED: Unsafe LLM response detected."

    return llm_response


def main():
    print("Secure Ollama Chat")
    print("Type 'exit' to quit.\n")

    while True:
        user_prompt = input("You: ")

        if user_prompt.lower() in ["exit", "quit"]:
            break

        result = ask_ollama(user_prompt)
        print(f"\nAssistant: {result}\n")


if __name__ == "__main__":
    main()
