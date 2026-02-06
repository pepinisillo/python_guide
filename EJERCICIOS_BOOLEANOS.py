"""
EJERCICIOS DE OPERACIONES LÓGICAS Y BOOLEANOS EN PYTHON
Dificultad: 1 (más fácil) → 15 (más difícil)
Lee DOCUMENTACION_BOOLEANOS.md antes de empezar.
"""

# =============================================================================
# DIFICULTAD 1: Escribe una función que reciba un número y retorne True si es
# mayor que 0, False en caso contrario.
# =============================================================================
def ejercicio_1(numero):
    pass  # Tu código aquí

# =============================================================================
# DIFICULTAD 2: Escribe una función que reciba dos booleanos a y b y retorne
# el resultado de (a and b).
# =============================================================================
def ejercicio_2(a, b):
    pass

# =============================================================================
# DIFICULTAD 3: Escribe una función que reciba un valor y retorne True si es
# "truthy", False si es "falsy" (sin usar if/else explícito; usa bool()).
# =============================================================================
def ejercicio_3(valor):
    pass

# =============================================================================
# DIFICULTAD 4: Escribe una función que reciba una edad (int) y retorne True
# si la edad está entre 18 y 65 (inclusive), False en caso contrario.
# Usa comparaciones encadenadas.
# =============================================================================
def ejercicio_4(edad):
    pass

# =============================================================================
# DIFICULTAD 5: Escribe una función que reciba un string y retorne True si
# contiene la letra 'a' Y la letra 'e' (ambas deben estar).
# =============================================================================
def ejercicio_5(texto):
    pass

# =============================================================================
# DIFICULTAD 6: Escribe una función que reciba tres booleanos a, b, c y
# retorne True si exactamente dos de ellos son True. (No uses if/elif/else.)
# =============================================================================
def ejercicio_6(a, b, c):
    pass

# =============================================================================
# DIFICULTAD 7: Escribe una función que reciba una lista y retorne True si
# todos sus elementos son truthy, False si alguno es falsy. Usa all().
# =============================================================================
def ejercicio_7(lista):
    pass

# =============================================================================
# DIFICULTAD 8: Escribe una función que reciba una variable x y retorne True
# solo si x es None. Usa el operador de identidad apropiado.
# =============================================================================
def ejercicio_8(x):
    pass

# =============================================================================
# DIFICULTAD 9: Escribe una función que reciba un número n y retorne True si
# n es par Y positivo. Una sola expresión con and.
# =============================================================================
def ejercicio_9(n):
    pass

# =============================================================================
# DIFICULTAD 10: Sin usar not, escribe una función que reciba un booleano b
# y retorne su negación. Pista: usa una tabla de verdad o equivalencia lógica.
# =============================================================================
def ejercicio_10(b):
    pass

# =============================================================================
# DIFICULTAD 11: Usando las leyes de De Morgan, simplifica y escribe una
# función equivalente a: not (a and b) usando solo or y not.
# Retorna el valor de esa expresión para los parámetros a, b.
# =============================================================================
def ejercicio_11(a, b):
    pass

# =============================================================================
# DIFICULTAD 12: Escribe una función que reciba una lista de números y
# retorne True si hay al menos un número negativo Y al menos un número
# positivo. Usa any() y listas por comprensión o similar.
# =============================================================================
def ejercicio_12(numeros):
    pass

# =============================================================================
# DIFICULTAD 13: Escribe una función que reciba un número entero n y retorne
# True si el bit en la posición 0 (el bit menos significativo) es 1.
# Pista: operaciones bit a bit (& con 1).
# =============================================================================
def ejercicio_13(n):
    pass

# =============================================================================
# DIFICULTAD 14: Escribe una función que implemente un XOR lógico entre dos
# booleanos a y b (True si uno es True y el otro False). Sin usar ^ ni
# operadores bit a bit.
# =============================================================================
def ejercicio_14(a, b):
    pass

# =============================================================================
# DIFICULTAD 15: Escribe una función que reciba una lista de booleanos y
# retorne True si el número de True es impar (paridad). Usa operaciones
# lógicas/booleanas, no count() ni sum() explícitos de 1s.
# Pista: XOR acumulado o similar.
# =============================================================================
def ejercicio_15(lista_bool):
    pass


# =============================================================================
# ZONA DE PRUEBAS (descomenta para probar)
# =============================================================================
if __name__ == "__main__":
    # assert ejercicio_1(5) == True
    # assert ejercicio_1(-3) == False
    # assert ejercicio_2(True, True) == True
    # assert ejercicio_2(True, False) == False
    # assert ejercicio_3(0) == False
    # assert ejercicio_3("hola") == True
    # assert ejercicio_4(25) == True
    # assert ejercicio_4(17) == False
    # assert ejercicio_5("casa") == False
    # assert ejercicio_5("parque") == True
    # assert ejercicio_6(True, True, False) == True
    # assert ejercicio_6(True, True, True) == False
    # assert ejercicio_7([1, 2, "a"]) == True
    # assert ejercicio_7([1, 0, "a"]) == False
    # assert ejercicio_8(None) == True
    # assert ejercicio_8(0) == False
    # assert ejercicio_9(4) == True
    # assert ejercicio_9(-2) == False
    # assert ejercicio_10(True) == False
    # assert ejercicio_10(False) == True
    # assert ejercicio_11(True, False) == True
    # assert ejercicio_12([-1, 2, 3]) == True
    # assert ejercicio_12([1, 2, 3]) == False
    # assert ejercicio_13(5) == True   # 5 = 101 en binario
    # assert ejercicio_13(4) == False  # 4 = 100 en binario
    # assert ejercicio_14(True, False) == True
    # assert ejercicio_14(True, True) == False
    # assert ejercicio_15([True, False, True]) == False  # 2 True = par
    # assert ejercicio_15([True, True, False]) == False  # 2 True = par
    # assert ejercicio_15([True, False, False]) == True  # 1 True = impar
    print("Completa los ejercicios y descomenta los assert para verificar.")
