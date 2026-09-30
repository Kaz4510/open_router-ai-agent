import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Execute a python script given the file path, relative to the working directory, optionally passing command-line arguments.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the python file to execute, relative to the working directory.",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "list of arguments to be passed to the function.",
                },
            },
            "required": ["file_path"],
        },
    },
}


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_directory_abs, file_path))
        if (
            not os.path.commonpath([working_directory_abs, file_path_abs])
            == working_directory_abs
        ):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        else:
            if not os.path.isfile(file_path_abs):
                return f'Error: "{file_path}" does not exist or is not a regular file'
            if file_path_abs.split(".")[-1] != "py":
                return f'Error: "{file_path}" is not a Python file'
            command = ["python", file_path_abs]

            if args:
                command.extend(args)
            result = subprocess.run(
                command,
                cwd=working_directory_abs,
                capture_output=True,
                text=True,
                timeout=30,
            )
            output: list[str] = []
            if result.returncode != 0:
                output.append(f"Process exited with code {result.returncode}")
            if not result.stdout and not result.stderr:
                output.append("No output produced")

            if result.stdout:
                output.append(f"STDOUT:\n{result.stdout}")
            if result.stderr:
                output.append(f"STDERR:\n{result.stderr}")

            return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"
