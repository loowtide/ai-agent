import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.types import *
from functions.prompt import system_prompt


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
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ],
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if verbose == "--verbose":
        print(f"User Prompt: {user_prompt}\n{response.text}")
    else:
        if response.function_calls:
            for i in response.function_calls:
                print(f"function : {i.name}({i.args})")
            # if response.text:
            # print(response.text)


if __name__ == "__main__":
    main()
