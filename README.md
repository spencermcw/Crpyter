# CRPYTER
A command line interface tool for encrypting and decrypting files.

### Requirements
- Python 3.9+
- venv
- tkinter

### CLI Usage
1. Create & Activate Virtual Environment
2. Install project's Requirements
3. EXE may be built with `pyinstaller`

~~~
$ pip install virtualenv
$ virtualenv env
$ source env/Scripts/activate
$ pip install -r requirements.txt
$ python <main|gui>.py
~~~

EXE Building
~~~
$ pyinstaller --onefile gui.py
~~~
