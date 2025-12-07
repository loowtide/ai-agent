import os


def get_file_content(working_directory: str, file_path: str):
    wd = os.path.realpath(os.path.abspath(working_directory))
    path: str = file_path if os.path.isabs(file_path) else os.path.join(wd, file_path)
    path = os.path.abspath(path)

    if (path + os.sep).startswith(wd + os.sep):
        if not os.path.exists(path):
            print(f"Error : File {file_path} does not exists")
            return

        MAX_CHARS = 10000
        with open(path, "r") as f:
            file_content = f.read(MAX_CHARS)
        print(file_content)
    else:
        print(
            f"Error: Cannot get file {file_path} as it is outside the working_directory"
        )
