"""
Kerj be ket egesz szamot (feltetelezhetjuk, hogy pozitivak), es ird ki a legnagyobb kozos osztojukat, majd a legkisebb kozos tobbszorosuket.

pl:
Bemenet:
6
27
Kimenet:
3
54
"""
elso = int(input())
masodik = int(input())
if (elso>0 and masodik>0):
    if (elso > masodik):
        nagyobb = elso
        kisebb = masodik
    else:
        nagyobb = masodik
        kisebb = elso

    index = 1
    szam = kisebb
    while index == 1:
        if (kisebb % szam == 0 and nagyobb % szam == 0):
            lko = szam
            index = 0
        szam -= 1
    print(lko)

print(elso * masodik // lko)

