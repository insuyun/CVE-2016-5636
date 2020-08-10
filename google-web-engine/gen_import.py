#!/usr/bin/env python2
import os
import zipimport
import zipfile
import struct

FILE = 'payload.txt'
ZIP = 'templates/import.zip'

# generate input
with open(FILE, 'wb') as f:
    payload = ("AAAA" * 128)
    f.write(payload)

zf = zipfile.PyZipFile(ZIP, mode='w')
zf.write(FILE)
zf.close()
