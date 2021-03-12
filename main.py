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

def main():
  # Prompt
  print('Password = Written Down.')
  print('Salt = Not Written Down.\n')
  # Build Fernet
  password = getpass('Password> ')
  salt = getpass('Salt> ')
  key = pass_to_key(password, salt)
  f = Fernet(key)
  # Determine Operation
  operation = input('[1] Encrypt\n[2] Decrypt\n> ')
  if operation not in ['1','2']:
    exit()
  # Handle Files
  ifile = input('Input File> ').strip('"')
  ofile = input('Ouptput File> ').strip('"')
  try:
    ifile = open(ifile, 'rb')
    ofile = open(ofile, 'wb')
  except OSError:
    print('Could not open one or both of the specified files')
    exit()
  # Do Work
  with ifile, ofile:
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

main()
