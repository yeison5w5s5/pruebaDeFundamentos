promedio=0
for i in range(3):
    voltaje=int(input(f"Ingresa el voltaje {i+1}: "))
    promedio+=voltaje
promedio/=3
if promedio<150:
    print(f"VOLTAJE CORRECTO= {promedio}")
elif 220>promedio>150:
    print(f"ALTO VOLTAJE= {promedio}")
else:
    print("PELIGRO!!")