
import os
import sys

import requests


def main() -> None:
    report_path = sys.argv[1] if len(sys.argv) > 1 else "reports/pytest-output.txt"
    analysis_path = sys.argv[2] if len(sys.argv) > 2 else "reports/ollama-analysis.txt"
    with open(report_path, encoding="utf-8") as report_file:
        test_output = report_file.read()

    host = os.environ.get("OLLAMA_HOST", "http://localhost:11434").rstrip("/")
    model = os.environ.get("OLLAMA_MODEL", "llama3.2")
    payload = {
        "model": model,
        "prompt": (
            "You are analyzing a failed Playwright pytest run. Use only evidence in "
            "the output; clearly label any uncertainty. Write a detailed, practical "
            "report with these sections:\n"
            "1. Failed test and exact error/location\n"
            "2. What happened and why it failed\n"
            "3. Root cause, distinguishing confirmed facts from likely causes\n"
            "4. Minimal code change or corrected code example\n"
            "5. Step-by-step actions to fix the failure\n"
            "6. How to rerun and what result confirms the test passes\n"
            "7. Any remaining limitations or checks\n"
            "Do not claim the test passed unless the output proves it.\n\n"
            f"Test output:\n{test_output[-12000:]}"
        ),
        "stream": False,
        "options": {"num_predict": 1000},
    }

    response = requests.post(
        f"{host}/api/generate",
        json=payload,
        timeout=300,
    )
    response.raise_for_status()

    result = response.json()
    analysis = result.get("response")
    if not isinstance(analysis, str):
        raise ValueError("Ollama response did not contain a string 'response' field")

    with open(analysis_path, "w", encoding="utf-8") as analysis_file:
        analysis_file.write(analysis)
        analysis_file.write("\n")

    print(f"Ollama analysis saved to {analysis_path}\n")
    print(analysis)


if __name__ == "__main__":
    main()
