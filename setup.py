from setuptools import setup

APP = ['SD_Card_Data_Offloading.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter', 'shutil', 'pathlib']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
