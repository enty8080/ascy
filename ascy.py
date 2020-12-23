import sys

if len(sys.argv) < 2:
    print("Usage: ascy <input_file>")
    sys.exit()

print("Reading input file...")
fout = open(sys.argv[1], 'rb').read().decode("unicode_escape")

print("Formatting input file...")
fin = open(sys.argv[1], 'wb')

print("Outputting formated file...")
fin.write(fout.encode())

# you should believe that this code works.
