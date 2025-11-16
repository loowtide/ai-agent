import os


def get_dir_size(path: str, root: str):
    total: int = 0
    with os.scandir(path) as it:
        for entry in it:
            entry_real = os.path.realpath(entry.path)

            if not (entry_real + os.sep).startswith(root + os.sep):
                continue

            if entry.is_file(follow_symlinks=False):
                total += entry.stat(follow_symlinks=False).st_size

            elif entry.is_dir(follow_symlinks=False):
                total += get_dir_size(entry_real, root)

    return total


def get_files_info(working_directory: str, directory: str = "."):
    working_directory = os.path.realpath(os.path.abspath(working_directory))
    abs_path = os.path.realpath(os.path.join(working_directory, directory))
    print(f"Result for {directory} directory:")

    if not (abs_path + os.sep).startswith(working_directory + os.sep):
        raise Exception(
            f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        )

    if not os.path.isdir(abs_path):
        raise Exception(f'Error: "{directory}" is not a directory')

    for i in os.listdir(abs_path):
        full_path = os.path.realpath(os.path.join(abs_path, i))
        if not (full_path + os.sep).startswith(working_directory + os.sep):
            continue

        if os.path.isdir(full_path):
            print(
                f"  - {i}: file_size={get_dir_size(full_path, working_directory)} bytes, is_dir=True"
            )
        else:
            print(
                f"  - {i}: file_size={os.path.getsize(full_path)} bytes, is_dir=False "
            )
