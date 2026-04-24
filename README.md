# Secure Ollama Lab

A ready-to-run local LLM security demo using Ollama.

This project demonstrates:
- insecure LLM prompt behavior
- secure system prompt design
- prompt injection detection
- unsafe input filtering
- safe response validation

## Demo Goal

Show how a local LLM can be protected from common prompt injection attempts using simple security controls.

## Requirements

- Linux
- Python 3.10+
- Ollama installed
- Model downloaded locally

## Install Ollama Model

```bash
ollama pull llama3.2:3b
```

## Start Ollama

```bash
ollama serve
```

Keep this terminal running.

## Setup Project

```bash
git clone https://github.com/mmukul/prompt-injection-defense-lab.git
cd prompt-injection-defense-lab

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Run Secure Chat Demo

```bash
python app/secure_chat.py
```

## Run Security Test Cases

```bash
python tests/run_prompt_tests.py
```

## Expected Output

The unsafe prompts should be blocked before reaching the LLM, or the unsafe LLM response should be detected.


## Disclaimer

This lab is for educational and defensive security learning only.
