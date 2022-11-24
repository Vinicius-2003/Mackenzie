print('Responda as perguntas a seguir com (sim = 1) e (não = 0)')
a = int(input("Telefonou para a vítima? : "))
b = int(input("Esteve no local do crime? : "))
c = int(input("Mora perto da vítima? : "))
d = int(input("Devia para a vítima? : "))
e = int(input("Já trabalhou com a vítima? : "))
count = 0
if a == 1:
    count=count+1
elif a == 0:
    count=count
if b == 1:
    count=count+1
elif b == 0:
    count=count
if c == 1:
    count=count+1
elif c == 0:
    count=count
if d == 1 :
    count=count+1
elif d == 0 : 
    count=count
if e == 1:
    count=count+1
elif e == 0:
    count=count
if count == 0:
    print('Inocente')
else:
    if (count > 0) and (count < 3):
        print('Suspeita')
    if (count >= 3)and(count<5):
        print('Cumplice')
    if (count == 5):
        print('assassina(o)')