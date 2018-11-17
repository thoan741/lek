# Uppgift 19

# a)
"""
foo = open("foo.txt", "r")
foo.read(7)
foo.read(5)
foo.readline()
foo.seek(0)

bar = open("bar.txt", "w")
bar.write(foo.read(35))
foo.tell()
foo.read()
foo.close()
bar.write("a"*12)
bar.close()
"""
# Uppgift 20)

# a)

N = 12
okrypterad_fil = open("foo.txt")
krypterad_fil = open("foo.txt.krypterad", "w")

for c in okrypterad_fil.read():
    c_e = chr((ord(c) - ord('A') + N) % 26 + ord('A'))
    krypterad_fil.write(c_e)

okrypterad_fil.close()
krypterad_fil.close()

# b)

