a = '1'
for i in xrange(30):
    pos = 0
    tmp = ''
    str_len = len(a)
    while pos < str_len:
        count = 1
        while pos+1<str_len and a[pos] == a[pos+1]:
            count += 1
            pos += 1

        tmp += '%d%s'%(count,a[pos])
        pos += 1
    a = tmp
print(len(a))
