#!python

from getpass import getpass
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def pass_to_key(password, salt):
  password = bytes(password, 'utf-8')
  salt = bytes(salt, 'utf-8')
  kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=500000,
  )
  key = base64.urlsafe_b64encode(kdf.derive(password))
  return key

def get_pass():
  password = getpass('Enter Password> ')
  password_conf = getpass('Confirm Password> ')
  if password != password_conf:
    print("Passwords Did Not Match")
    exit()
  return password

def get_salt():
  salt = getpass('Enter Salt> ')
  salt_conf = getpass('Confirm Salt> ')
  if salt != salt_conf:
    print("Salts Did Not Match")
    exit()
  return salt

def get_operation():
  print('[1] Encrypt\n[2] Decrypt')
  operation = input('Desired Operation> ')
  if operation not in ['1','2']:
    print('Invalid Operation')
    exit()
  return operation

def get_files():
  ifile = input('Input File Path> ').strip('"')
  ofile = input('Ouptput File Path> ').strip('"')
  try:
    ifile = open(ifile, 'rb')
    ofile = open(ofile, 'wb')
  except OSError:
    print('Could not open one or both of the specified file paths.')
    exit()
  return (ifile, ofile)

def do_work(ifile, ofile, operation, f):
  # Encrypt
  if operation == '1':
    token = f.encrypt(ifile.read())
  # Decrypt
  else:
    token = f.decrypt(ifile.read())
  # Write
  ofile.write(token)
  # Close Files
  ifile.close()
  ofile.close()

def main():
  # Prompts
  print('Password = Written Down.')
  print('Salt = Not Written Down.')
  # Build Fernet
  password = get_pass()
  salt = get_salt()
  key = pass_to_key(password, salt)
  f = Fernet(key)
  # Handle Operation
  operation = get_operation()
  ifile, ofile = get_files()
  do_work(ifile, ofile, operation, f)

main()
