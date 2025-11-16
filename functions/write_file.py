import os


def write_file(working_directory: str, file_path: str, content: str):
    wd = os.path.realpath(os.path.abspath(working_directory))
    path: str = file_path if os.path.isabs(file_path) else os.path.join(wd, file_path)
    path = os.path.realpath(path)

    if (path + os.sep).startswith(wd + os.sep):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content)
    else:
        print(
            f'Error: Cannot write to "{path}" as it is outside the permitted working directory'
        )
