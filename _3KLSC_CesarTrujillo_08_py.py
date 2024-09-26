MaxTamC = 10
A = [0] * MaxTamC 
frente = 0
final = 0
contador = 0

respuesta = input("Desea agregar elementos a la cola? (s/n): ").lower()

while respuesta == 's' and contador < MaxTamC:
    if (final + 1) % MaxTamC == frente:
        print("Desbordamiento de la cola")
        exit(1)

    elemento = int(input("Ingrese un elemento para la cola: "))
    A[final] = elemento  
    final = (final + 1) % MaxTamC  
    
    contador += 1
    print(f"Elemento {contador} agregado a la cola: {elemento}")

    if contador < MaxTamC:
        respuesta = input("Desea agregar mas elementos a la cola? (s/n): ").lower()

if frente == final:
    print("La cola esta vacia")
    exit(1)

primerElemento = A[frente]
print(f"El primer elemento de la cola es: {primerElemento}")
frente = (frente + 1) % MaxTamC 

print("Elementos de la cola en el orden de ingreso:")
i = frente
while i != final:
    print(A[i], end=" ")
    i = (i + 1) % MaxTamC
print() 

