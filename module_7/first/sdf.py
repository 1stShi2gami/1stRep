import io
from pprint import pprint

name = 'sample2.txt'
with open(name, encoding='utf-8') as file:
    for line in file:
        for char in line:
            print(char, end='')
    print(file.tell())

print(file.read())