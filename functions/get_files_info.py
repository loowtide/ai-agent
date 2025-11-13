import os


def get_dir_size(path: str = "."):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


def get_files_info(working_directory: str, directory: str = "."):
    abs_path = os.path.abspath(os.path.join(working_directory, directory))
    print(f"Result for {directory} directory:")
    if os.path.isdir(abs_path):
        if os.path.realpath(abs_path).startswith(os.path.realpath(working_directory)):
            for i in os.listdir(abs_path):
                full_path = os.path.join(abs_path, i)
                if os.path.isdir(full_path):
                    print(
                        f"  - {i}: file_size={get_dir_size(full_path)} bytes, is_dir=True"
                    )

                else:
                    print(
                        f"  - {i}: file_size={os.path.getsize(full_path)} bytes, is_dir=False "
                    )
        else:
            raise Exception(
                f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            )
    else:
        raise Exception(f'Error: "{directory}" is not a directory')
