
from struct import unpack
import sys


class KDay(object):
    def __init__(self, buf):
        self.data = unpack('IIIIIfII', buf)

    def __str__(self):
        return ('日期: %s, '
                '开盘: %s, '
                '最高: %s, '
                '最低: %s, '
                '收盘: %s, '
                '成交: %s, '
                '金额: %s, '
                '保留: %s\n') % self.data

def main():
    with open('day/sh600060.day', 'rb') as fp:
        m = 0
        d = 0
        while True:
            try:
                buf = fp.read(32)
                record = unpack('IIIIIfII', buf)
                # print record
                if record[5] > m:
                    m = record[5]
                    r = buf
            except:
                break
        print KDay(r)

if __name__ == '__main__':
    main()