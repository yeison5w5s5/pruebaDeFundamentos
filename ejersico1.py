voltajes=[]
promedio=0
for i in range(5):
    voltaje=int(input(f"Ingresa el voltaje {i+1}: "))
    voltajes.append(voltaje)
for v in voltajes:
    promedio+=v
promedio/=5
if promedio>220:
    print(f"ALTO VOLTAJE= {promedio}")
else:
    print(f"VOLTAJE CORRECTO= {promedio}")