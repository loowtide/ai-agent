import os
import subprocess


def run_python_file(working_directory: str, file_path: str, args: list[str] = []):
    wd = os.path.realpath(os.path.abspath(working_directory))
    path: str = file_path if os.path.isabs(file_path) else os.path.join(wd, file_path)
    path = os.path.realpath(path)

    if not (path + os.sep).startswith(wd + os.sep):
        print(
            f'Error : Cannot execute "{file_path}" as it is outside the working directory'
        )
    elif not os.path.exists(path):
        print(f'Error : File "{file_path}" not found')
    elif not file_path.endswith(".py"):
        print(f'Error : "{file_path}" is not a python file')
    else:
        try:
            command = ["python", path] + args
            result = subprocess.run(command, capture_output=True, text=True, timeout=30)

            print("Output: ", result.stdout)
            if result.stderr:
                print("Errors:", result.stderr)
        except Exception as e:
            print(f"Error : {str(e)}")
