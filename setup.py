import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("EvoScript.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = [],
        excludes = []
)




setup(
    name = "EvoScript by Jony",
    version = "1.0",
    description = "Evo Bracket Sort script",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
