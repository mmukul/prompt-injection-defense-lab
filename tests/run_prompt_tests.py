import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
APP_DIR = ROOT / "app"
sys.path.append(str(APP_DIR))

from secure_chat import ask_ollama


def run_tests(file_path: pathlib.Path, expected_block: bool):
    print(f"\nRunning tests from: {file_path.name}")
    print("=" * 60)

    prompts = [line.strip() for line in file_path.read_text().splitlines() if line.strip()]

    for prompt in prompts:
        print(f"\nPrompt: {prompt}")
        response = ask_ollama(prompt)
        print(f"Response: {response[:500]}")

        blocked = response.startswith("BLOCKED")

        if expected_block and blocked:
            print("Result: PASS - unsafe prompt blocked")
        elif expected_block and not blocked:
            print("Result: FAIL - unsafe prompt was not blocked")
        elif not expected_block and not blocked:
            print("Result: PASS - safe prompt allowed")
        else:
            print("Result: FAIL - safe prompt was blocked")


def main():
    run_tests(ROOT / "prompts" / "attack_prompts.txt", expected_block=True)
    run_tests(ROOT / "prompts" / "safe_prompts.txt", expected_block=False)


if __name__ == "__main__":
    main()
