import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
        name='NSim',
        version='0.1',
        url='www.swglobal.com',
        author='Abraham Yusuf',
        author_email='yabraham@swglobal.com',
        description='NSim Demographics Viewer',
        options={'build_exe': {'includes': 'atexit'}},
        executables=[Executable('NSim.py', base=base)])