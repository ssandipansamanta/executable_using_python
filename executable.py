from cx_Freeze import setup, Executable

base = None

executables = [Executable("PYTHON CODE PATH", base=base)]

packages = ["idna","pyautogui","time","datetime"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "check",
    options = options,
    version = "1.0",
    description = 'have fun',
    executables = executables
)
