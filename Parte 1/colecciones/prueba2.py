nombre = input("Por favor ingrese su nombre: ")
edad = int(input("Por favor ingrese su edad: "))
peso = float(input("Por favor ingrese su peso: "))

if (edad > 0 and edad < 18):
    print("Hola " + nombre + " eres menor de edad")
elif(edad >= 18):
    print("Hola " + nombre + " eres mayor de edad")
else:
    print("Edad incorrecta")

print(f"{nombre} y tu edad es de: {edad} y su peso es de: {peso}")

cont = 0
while(cont <= 100 ):
    print(cont)
    cont++1

for cont in range(0, 100, 5):
    print(cont)

texto = "Hola, mundo!"
for caracter in texto:
    print(caracter)