def calculadora(a, b, operacion):
    operaciones = {
        'suma': a + b,
        'resta': a - b,
        'multiplicacion': a * b,
        'division': a / b if b != 0 else "error: División por cero",
    }
    return operaciones.get(operacion, "Error: Operación no valida")

print(calculadora(10, 5, "suma"))
print(calculadora(10, 5, "resta"))
print(calculadora(10, 5, "multiplicacion"))
print(calculadora(10, 5, "division"))