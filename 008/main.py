x=0.0
y=0.0
irány = input()
while irány != "stop":
  if irány == "forward":
    y = y + float(input())
  if irány == "backward":
    y = y - float(input())
  if irány == "right":
    x = x + float(input())
  if irány == "left":
    x = x - float(input())
  irány = input()

if irány == "stop":
  print(round(x,2))
  print(round(y,2))
  origo = ((x**2)+(y**2))**(1/2)
  print(round(origo,2)) 
