from cx_Freeze import setup, Executable

base = None    

executables = [Executable("loginInside.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Tool",
    options = options,
    version = "1.0.0",
    description = 'Author: PhucPTit',
    executables = executables
)