string = '01234567890123456789012345678901234567890123456789'

l1 = [string.split("9", string.count('9') - 1)]
l2 = [string.replace('9', '9.', string.count('9') - 1)]
print(l1)
print(l2)

