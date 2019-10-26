import binascii
import sys

def lpad(s, l, c=' '):
    return c * (l - len(s)) + s

def rpad(s, l, c=' '):
    return s + c * (l - len(s))

with open(sys.argv[1]) as fp:
    v = fp.read().splitlines()
    for x in v:
        print('{} {} {}'.format(
            rpad(x, 64),
            lpad(hex(binascii.crc32(x.encode('utf-8')))[2:], 8, c='0'),
            len(x)
        ))

