# CRPYTER
A command line interface tool for encrypting and decrypting files.

### Requirements
- Python 3.9
- virtualenv

### CLI Usage
1. Create & Activate Virtual Environment
2. Install project's Requirements
3. EXE may be built with `pyinstaller`

~~~
$ virtualenv --no-site-packages --distribute env
$ source env/Scripts/activate
$ pip install -r requirements.txt
$ python main.py
~~~

EXE Building
~~~
$ pyinstaller --onefile main.py
~~~
