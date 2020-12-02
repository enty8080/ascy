import sys


if len(sys.argv) < 2:
    print("Usage: ascy <input_file>")
    sys.exit()
    
fout = open(sys.argv[1], 'rb').read().decode("unicode_escape")
fin = open(sys.argv[1], 'wb')
fin.write(fout.encode())
