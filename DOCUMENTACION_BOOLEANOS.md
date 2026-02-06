# Documentación: Operaciones Lógicas y Booleanos en Python

## Tipo de dato bool

Python tiene un tipo de dato nativo para representar valores de verdad: `bool`. Solo admite dos valores posibles: `True` y `False` (con mayúscula inicial). Los booleanos son subclase de enteros: `True == 1` y `False == 0`.

## Operadores de comparación

| Operador | Significado    | Ejemplo |
|----------|----------------|---------|
| `==`     | Igual a        | `5 == 5` → True |
| `!=`     | Diferente de   | `3 != 7` → True |
| `<`      | Menor que      | `2 < 5` → True |
| `>`      | Mayor que      | `10 > 3` → True |
| `<=`     | Menor o igual  | `4 <= 4` → True |
| `>=`     | Mayor o igual  | `6 >= 6` → True |

## Operadores lógicos

| Operador | Significado | Descripción |
|----------|-------------|-------------|
| `and`    | Y lógico     | Retorna True si ambas expresiones son verdaderas. Prioridad baja. |
| `or`     | O lógico     | Retorna True si al menos una expresión es verdadera. Prioridad media. |
| `not`    | Negación     | Invierte el valor booleano. Prioridad alta. |

**Orden de evaluación:** `not` → `and` → `or`

## Valores Truthy y Falsy

En Python, cualquier objeto puede evaluarse en contexto booleano. Los valores considerados **falsy** (equivalentes a False) son:
- `False`
- `None`
- `0` (entero), `0.0` (float)
- Cadenas vacías: `""`
- Listas vacías: `[]`
- Tuplas vacías: `()`
- Diccionarios vacíos: `{}`
- Conjuntos vacíos: `set()`

Todo lo demás se considera **truthy** (equivalente a True).

## Conversión explícita: bool()

La función `bool()` convierte cualquier valor a booleano según las reglas truthy/falsy:
```python
bool(0)      # False
bool(1)      # True
bool("")     # False
bool("hola") # True
bool([])     # False
bool([1,2])  # True
```

## Evaluación de cortocircuito (short-circuit)

- `and`: Si el primer operando es False, no evalúa el segundo (ya sabe que el resultado será False).
- `or`: Si el primer operando es True, no evalúa el segundo (ya sabe que el resultado será True).

Esto permite escribir expresiones como `x and x.metodo()` para evitar errores cuando `x` podría ser None.

## Operadores de identidad: is e is not

- `is`: Comprueba si dos objetos son el mismo en memoria (identidad).
- `is not`: Comprueba que no sean el mismo objeto.

**Importante:** `==` compara valores; `is` compara identidad. Para `None` siempre usa `is None` o `is not None`.

## Operadores de pertenencia: in y not in

- `in`: True si el elemento está en la secuencia.
- `not in`: True si el elemento no está en la secuencia.

Funcionan con cadenas, listas, tuplas, conjuntos y diccionarios (en diccionarios se busca en las claves).

## Comparaciones encadenadas

Python permite encadenar comparaciones de forma natural:
```python
0 < x < 10     # equivalente a: 0 < x and x < 10
a == b == c    # True si los tres son iguales
```

## Leyes de De Morgan

- `not (A and B)` equivale a `(not A) or (not B)`
- `not (A or B)` equivale a `(not A) and (not B)`

Útil para simplificar condiciones negadas.

## Precedencia de operadores (de mayor a menor)

1. `**` (potencia)
2. `+x`, `-x`, `~x` (unarios)
3. `*`, `/`, `//`, `%`
4. `+`, `-`
5. `<<`, `>>` (bits)
6. `&` (AND bit a bit)
7. `^` (XOR bit a bit)
8. `|` (OR bit a bit)
9. Operadores de comparación (`<`, `<=`, `>`, `>=`, `!=`, `==`)
10. `not`
11. `and`
12. `or`

Los operadores de comparación tienen la misma precedencia y se evalúan de izquierda a derecha.

## Expresiones condicionales (ternario)

```python
resultado = valor_si_true if condicion else valor_si_false
```

## Tablas de verdad

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| T | T | T       | T      | F     |
| T | F | F       | T      | F     |
| F | T | F       | T      | T     |
| F | F | F       | F      | T     |

## Operadores bit a bit (relacionados con lógica)

| Operador | Significado | Ejemplo |
|----------|-------------|---------|
| `&`  | AND bit a bit  | `5 & 3` → 1 |
| `|`  | OR bit a bit   | `5 | 3` → 7 |
| `^`  | XOR bit a bit  | `5 ^ 3` → 6 |
| `~`  | NOT bit a bit  | `~5` → -6 |
| `<<` | Desplazamiento izquierda  | `1 << 2` → 4 |
| `>>` | Desplazamiento derecha    | `8 >> 2` → 2 |

## any() y all()

- `any(iterable)`: True si al menos un elemento es truthy.
- `all(iterable)`: True si todos los elementos son truthy.
- Con iterables vacíos: `any([])` → False, `all([])` → True.
