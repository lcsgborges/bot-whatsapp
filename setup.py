import sys
import os
from cx_Freeze import setup, Executable

# Definindo o caminho para a área de trabalho do usuário
desktop_path = os.path.expanduser("~/Área de Trabalho")

# Opções de build
build_exe_options = {
    "packages": ["os"],
    "includes": [
        "tkinter", "blinker", "certifi", 
        "click", "cx_Freeze", "filelock",
        "idna", "itsdangerous",
        "packaging", "pyperclip",  
        "pytweening", "pywhatkit", "requests",
        "setuptools", "soupsieve",
        "typing_extensions", "urllib3",
    ],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Meu App",
    version="0.1",
    description="Minha 1° Aplicação!",
    options={"build_exe": build_exe_options},
    executables=[Executable("src/app.py", base=base)]
)
