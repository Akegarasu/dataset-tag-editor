import importlib.util
import os
import subprocess
import sys

import cmd_args, logger


# ================================================================
# brought from AUTOMATIC1111/stable-diffusion-webui and modified

python = sys.executable




def is_installed(package):
    try:
        spec = importlib.util.find_spec(package)
    except ModuleNotFoundError:
        return False

    return spec is not None


def run(command):
    return subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        env=os.environ,
    )


def run_pip(args, desc=None):
    if desc is not None:
        print(f"Installing {desc}")

    command = f'"{sys.executable}" -m pip {args}'
    result = run(command)
    if result.returncode != 0:
        message = f"""
Couldn't Install {desc}.
Command: {command}
Error code: {result.returncode}
stdout: {result.stdout.decode(encoding="utf8", errors="ignore") if len(result.stdout)>0 else '<empty>'}
stderr: {result.stderr.decode(encoding="utf8", errors="ignore") if len(result.stderr)>0 else '<empty>'}
"""
        raise RuntimeError(message)


# ================================================================


if __name__ == "__main__":
    import interface

    interface.main()
