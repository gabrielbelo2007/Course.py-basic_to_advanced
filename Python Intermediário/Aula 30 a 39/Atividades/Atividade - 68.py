string = '01234567890123456789012345678901234567890123456789'

n = 10
l1 = [string[i:i+n] for i in range(0, len(string), n)]
l2 = [string.replace('9', '9.', string.count('9') - 1)]
print(l1)
print(l2)

