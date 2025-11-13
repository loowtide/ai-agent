import os


def write_file(working_directory, file_path, content):
    if os.path.realpath(file_path).startswith(os.path.realpath(working_directory)):
        if os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(content)

    else:
        print(
            f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        )
