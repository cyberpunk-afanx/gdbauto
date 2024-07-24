import sys,os
def create_source_file(platform, binary, data):
        disassembly = 'set disassembly intel\n'        
        info_functions = 'info functions\n'
        disassemble = 'disassemble main\n'        
        run = 'run ' + data + '\n'        
        registers = 'i r\n'        
        backtrace = 'bt\n'        
        
        with open("source.txt", 'w') as f:
                f.write(disassembly + info_functions + disassemble + run + registers + backtrace)
        
        if(platform == 0):
                try:
                    os.system("gdb -x source.txt " + binary)
                    print("[+] Well, done!")
                except Exception as ex:
                    print("[-] " + str(ex))
        else:
                try:
                    os.system("gdb.exe -x source.txt " + binary)
                    print("[+] Well, done!")
                except Exception as ex:
                    print("[-] " + str(ex))
        print("AFANX")
        
        print("channel: https://t.me/k0n70r4")
def signature(binary):
        with open(binary, 'rb') as f:
                data = f.read(4)
        if(b'Mz' in data):
                return 0        
        elif(b'\x7fELF' in data):
                return 1

def main():
        if(len(sys.argv) != 3):
                print("USAGE: gdbauto.py <binary_file> <data>")
                print("AFANX")
        if(signature(sys.argv[1])):
                print("[+] linux")
                create_source_file(0, sys.argv[1], sys.argv[2])
        else:
                print("[+] windows")
                create_source_file(1, sys.argv[1], sys.argv[2])
if __name__ == "__main__":
    main()