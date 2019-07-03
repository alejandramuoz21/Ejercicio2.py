calif = int(input("Intruzca tu calificacion"))
if calif < 0:
    print("Error: Calif invalida")
elif calif < 5:
    print("Suspenso")
elif calif == 5:
    print("Suficiente")
elif calif == 6:
    print("probado")
elif calif == 7:
    print("notable")
elif calif >= 8:
    print("sobresaliente")