def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
n=int(input("Ingrese el valor de fibonacci a saber: ",))
print("El valor es: ",fibonacci(n))