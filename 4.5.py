# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
from asyncore import write
import random


def mnogochlen(a=None, b=None, c=None, res='') -> str:
    if a is None:
        a = random.randint(1, 100)
    if b is None:
        b = random.randint(0, 100)
    if c is None:
        c = random.randint(0, 100)
    if b > 0:
        res += '+' + str(b) + '*x'
    if c > 0:
        res += '+' + str(c)
    return f'{a}*x^2'+res


f = open('dz40.txt', 'w')
f.write(mnogochlen())
print(mnogochlen())
f.close

f = open('dz41.txt', 'w')
f.write(mnogochlen())
print(mnogochlen())
f.close

f = open('dz40.txt', 'r')
list_50 = str(f.readline()).split('x')
c1 = a1 = b1 = 0
if len(list_50) == 3:
    c1 = list_50[2][1:]
if len(list_50) >= 2:
    b1 = list_50[1][3:-1]
a1 = list_50[0][:-1]
f.close()

f = open('dz41.txt', 'r')
list_51 = str(f.readline()).split('x')
c2 = a2 = b2 = 0
if len(list_51) == 3:
    c2 = list_51[2][1:]
if len(list_51) >= 2:
    b2 = list_51[1][3:-1]
a2 = list_51[0][:-1]
f.close()

f = open('dz42.txt', 'w')
f.write(mnogochlen(int(a1)+int(a2),int(b1)+int(b2),int(c1)+int(c2)))
print(mnogochlen(int(a1)+int(a2),int(b1)+int(b2),int(c1)+int(c2)))
f.close()

# ffile1 = open('file1.txt','r')
# ffile2 = open('file2.txt','r')
# ffile3 = open('file3.txt','w')
# file1 = ffile1.readline()
# file2 = ffile2.readline()

# for i in range(len(file1)):
#     if file1[i-1] != '^':
#         if file1[i].isnumeric:
#             ffile3.write(str(int(file1[i])+int(file2[i])))
#         else:
#             ffile3.write(str(file1[i]))
#     else:
#         ffile3.write(str(file1[i]))

# ffile1.close
# ffile2.close
# ffile3.close

