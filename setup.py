import subprocess


def setup():
    pip_install = subprocess.run(["pip install", "-r", "requirements.txt"])
    return_code = pip_install.returncode
    print(pip_install.returncode)
    return return_code
