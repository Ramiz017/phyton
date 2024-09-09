num1 = int(input("Ingrese el primer numero: ")) 
num2 = int(input("Ingrese el segundo numero: "))

if (num1 > num2):
    resultado = num1 + num2
elif(num1 == num2):
    resultado = num1 * num2
else:
    resultado = num1 - num2

print(resultado)

cont = 0
while(cont < 10):
    cont=+1
    print(cont)