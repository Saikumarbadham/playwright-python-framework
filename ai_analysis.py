
import os
import sys

import requests


def main() -> None:
    report_path = sys.argv[1] if len(sys.argv) > 1 else "reports/pytest-output.txt"
    with open(report_path, encoding="utf-8") as report_file:
        test_output = report_file.read()

    host = os.environ.get("OLLAMA_HOST", "http://localhost:11434").rstrip("/")
    model = os.environ.get("OLLAMA_MODEL", "llama3.2")
    payload = {
        "model": model,
        "prompt": (
            "Analyze this Playwright pytest failure. Use the test output below "
            "to identify the root cause, possible reason, and suggested solution.\n\n"
            f"Test output:\n{test_output[-12000:]}"
        ),
        "stream": False,
    }

    response = requests.post(
        f"{host}/api/generate",
        json=payload,
        timeout=120,
    )
    response.raise_for_status()

    result = response.json()
    analysis = result.get("response")
    if not isinstance(analysis, str):
        raise ValueError("Ollama response did not contain a string 'response' field")

    print(analysis)


if __name__ == "__main__":
    main()
