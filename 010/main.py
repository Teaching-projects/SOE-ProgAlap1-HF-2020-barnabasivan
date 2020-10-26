percek = []
sms = []

for honap in range(12):
    percek.append(int(input()))
    sms.append(int(input()))

havidíj = int(input())
percdíj = int(input())
smsdíj = int(input())

szamla = []
total = 0

for honap in range(12):
    mennyilenne=percdíj*percek[honap] + smsdíj * sms[honap]
    if mennyilenne > havidíj:
        szamla.append(mennyilenne)
    else:
        szamla.append(havidíj)

for sz in szamla:
    total+=sz

print(szamla)
print(total)
