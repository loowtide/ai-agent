import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    _ = load_dotenv()
    args = sys.argv
    user_prompt = args[1]
    verbose = args[2] if len(args) >= 3 else ""
    api_key = os.environ.get("GEMINI_API_KEY")
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=messages,
    )
    if verbose == "--verbose":
        print(f"User Prompt: {user_prompt}\n{response.text}")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
