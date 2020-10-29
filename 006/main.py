"""
Kerj be egesz szamokat addig, amig 0-t nem kapsz.
A vegen irj ki minden bekert szamot, de mindgyiket csak egyszer, es abban a sorrendben, ahogy az elso elofordulas tortent.

pl:

Bemenet:
1
2
3
4
3
2
4
7
5
6
7
0
Kimenet:
1
2
3
4
7
5
6
"""
szám = int(input())
list = []
index = 0

while szám != 0:
    if szám not in list:
        list.append(szám)
        szám = int(input())
    else:
        szám = int(input())

while index < len(list):
    print(list[index])
    index = index + 1