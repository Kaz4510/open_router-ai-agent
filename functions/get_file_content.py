import os

from config import MAX_CHARS


def get_file_content(working_dir: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_dir)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        if (
            not os.path.commonpath([working_dir_abs, target_file_path])
            == working_dir_abs
        ):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        else:
            if not os.path.isfile(target_file_path):
                return f'Error: File not found or is not a regular file: "{file_path}"'
            else:
                with open(target_file_path, "r") as file:
                    content = file.read(MAX_CHARS)
                    if file.read(1):
                        content += (
                            f'[...file "{file_path}" truncated at {MAX_CHARS} characters]'
                        )
                return content

    except Exception as e:
        return f"Error: {e}"
