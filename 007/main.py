noszamla = 0
honap = 0
egyenleg = 0

while honap != 12:
    pmozgas = int(int(input()))
    egyenleg += pmozgas
    noszamla += pmozgas
    if honap != 0:
        egyenleg -= 2000
    if egyenleg > 0:
        egyenleg += int(egyenleg * 0.05)
    else:
        egyenleg += int(egyenleg * 0.1)
    honap += 1
    
print(int(egyenleg))
print(noszamla)