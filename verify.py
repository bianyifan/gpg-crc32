import binascii
import sys

def lpad(s, l, c=' '):
    return c * (l - len(s)) + s

def rpad(s, l, c=' '):
    return s + c * (l - len(s))

out = ''

with open(sys.argv[1]) as fp:
    v = fp.read().splitlines()
    for i, x in enumerate(v):
        a = x.rsplit(' ', maxsplit=2)
        l = int(a[2])
        c = int(a[1], base=16)
        s = a[0][:l]
        if binascii.crc32(s.encode('utf-8')) == c:
            out = out + s + '\n'
        else:
            print('Validation error on line {}'.format(i))
            exit()

print(out)
