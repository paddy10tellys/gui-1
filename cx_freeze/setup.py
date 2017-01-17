#  setup.py
import cx_Freeze
import sys
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [cx_Freeze.Executable('wsgui.py', base=base)]

cx_Freeze.setup(
    name='wsgui',
    options={'build_exe': {'packages': ['tkinter', 'argparse']}},
    version='0.01',
    description='gui word counting application',
    executables=executables
    )
