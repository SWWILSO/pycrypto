import base64, argparse

encoding = True

parser = argparse.ArgumentParser(description="Encode/Decode Base64")
parser.add_argument('--d', dest='encoding', action='store_false', required=False)
args = parser.parse_args()

if args.encoding:
  try:
      while True:
        str_in = input("\n[+] Enter message for Base64 encoding: \n")
        encoding = base64.standard_b64encode(bytearray(str_in, 'utf-8'))
        print("\nOutput:")
        print(encoding)
  except KeyboardInterrupt:
      print("\n[+] Exiting..\n")
else:
  try:
      while True:
        str_in = input("\n[+] Enter message for Base64 decoding: \n")
        decoding = base64.standard_b64decode(str_in)
        print("\nOutput:")
        print(decoding)
  except KeyboardInterrupt:
      print("\n[+] Exiting..\n")