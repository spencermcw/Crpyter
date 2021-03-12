import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def pass_to_key(password):
  kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=b'BadPractice',
    iterations=100000,
  )
  key = base64.urlsafe_b64encode(kdf.derive(password))
  return key

def main():
  # Build Fernet
  password = bytes(input('Password> '),'utf-8')
  key = pass_to_key(password)
  f = Fernet(key)
  # Determine Operation
  operation = input('[1] Encrypt\n[2] Decrypt\n> ')
  if operation not in ['1','2']:
    exit()
  # Handle Files
  ifile = input('Input File> ')
  ofile = input('Ouptput File> ')
  try:
    ifile = open(ifile, 'rb')
    ofile = open(ofile, 'wb')
  except OSError:
    print("Could not open one or both of the specified files")
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
