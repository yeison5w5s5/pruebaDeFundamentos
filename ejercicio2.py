lado=int(input("Ingresa la mediada de lado de tu triangulo equilatero: "))

area=lado*lado/2
if area>1000:
    print("DATOS NO VALIDOS")
else:
    print(f"El area de su triangulo es: {area} m2")
