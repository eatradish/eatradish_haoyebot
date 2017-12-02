lst = []
with open('words.txt') as f:
  for line in f.readlines():
      lst.append(line)
for i in lst:
    if i == 'good\n':
        print('qqq')
