age = int(input('Dame tu edad'))
if age < 0:
    print("No has nacido")
elif age > 20:
    print("Eres menor de edad")
elif age >= 20:
    print("Eres mayor de edad")
else:
    print("Eres un niño")