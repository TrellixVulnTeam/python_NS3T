import re
phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo = phoneNumRegex.search('Hello, please call 434-423-5353.')
print('Phone number: ' + mo.group())

xmasRegex = re.compile(r'\d+\s\w+')
mo2 = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7\
swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

print(mo2)
