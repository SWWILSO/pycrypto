import hashlib
from itertools import product

CRACK = raw_input('[+] 4-digit code MD4 UTF-16 hash cracker\n[+] Enter hash: ')
cracked = False


passes = product("0123456789", repeat=4)

for i in passes:
	password = str(i[0]) + str(i[1] + str(i[2]) + str(i[3]))
	hash = hashlib.new("md4", password.encode("utf-16le")).hexdigest()
	#print(i, password)
	if hash == CRACK:
		print("\n[+] Password cracked. \n" + password)
		cracked = True
		exit()

if not cracked:
	exit("\n\n[-] Password could not be cracked")