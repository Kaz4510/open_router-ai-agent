import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_directory = os.path.normpath(
            os.path.join(working_directory_abs, directory)
        )
        valid_target_dir = (
            os.path.commonpath([working_directory_abs, target_directory])
            == working_directory_abs
        )
        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:
            try:
                output_string = ""
                with os.scandir(target_directory) as entries:
                    for entry in entries:
                        file_size = os.path.getsize(entry)
                        is_dir = os.path.isdir(entry)
                        output_string += f"- {entry.name}: file_size={file_size} bytes, is_dir={is_dir}\n"
                return output_string
            except Exception as e:
                return "Error: {e}"
    except Exception as e:
        return f"Error: {e}"
