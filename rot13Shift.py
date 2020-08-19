alpha =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
shift = 13

def rot13Shift(str_in, str_len):
    shift_out = ""

    for i in range(str_len):
        char = str_in[i]
        index = alpha.find(char)
        shift_index = (index + shift)%26
        shift_out += alpha[shift_index]

    return shift_out

def main():
    try:
        while True:
            str_in = input("\n[+] Enter message for ROT13 shift: \n")
            str_len = len(str_in)
            print("Output:\n" + rot13Shift(str_in, str_len))
    except KeyboardInterrupt:
        print("\n[+] Exiting..\n")

if __name__ == '__main__':
    main()