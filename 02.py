def calculaFibonacci(n):
    sequenciaFibo = [0, 1]
    while sequenciaFibo[-1] < n:
        sequenciaFibo.append(sequenciaFibo[-1] + sequenciaFibo[-2])
    
    return sequenciaFibo

def perteceFrequencia(num):
    sequenciaFibo = calculaFibonacci(num)
    
    if num in sequenciaFibo:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
print(perteceFrequencia(numero))