#-------------------------------------------------------------------------------#
# Error de sintaxis: falta dos puntos
if x > 5
    print("Greater")

# Error: SyntaxError: invalid syntax

#-------------------------------------------------------------------------------#
# Código sintácticamente correcto, pero genera excepción en tiempo de ejecución
x = 10
y = 0
result = x / y  # ZeroDivisionError: division by zero
#-------------------------------------------------------------------------------#

"""
1.ZeroDivisionError: Ocurre cuando se intenta dividir un número por cero.
2.TypeError: Ocurre cuando una operación o función se aplica a un objeto de un tipo inapropiado.
3.ValueError: Ocurre cuando una función recibe un argumento con el tipo correcto pero un valor inapropiado.
4.NameError: Ocurre cuando se intenta acceder a una variable que no ha sido definida.
5.IndexError: Ocurre cuando se intenta acceder a un índice que está fuera del rango de una lista o tupla.
6.KeyError: Ocurre cuando se intenta acceder a una clave que no existe en un diccionario.
7.AttributeError: Ocurre cuando se intenta acceder a un atributo que no existe en un objeto.
8.FileNotFoundError: Ocurre cuando se intenta abrir un archivo que no existe.
9.ImportError: Ocurre cuando una importación de módulo falla.
10.IndentationError: Ocurre cuando la indentación del código no es correcta.

# Todas las excepciones heredan de BaseException
# La mayoría heredan de Exception

BaseException
    ├── Exception
    │    ├── ArithmeticError
    │    │    ├── ZeroDivisionError
    │    │    ├── OverflowError
    │    ├── LookupError
    │    │    ├── IndexError
    │    │    ├── KeyError
    │    ├── ValueError
    │    ├── TypeError
    │    ├── NameError
    │    └── ... (muchas más)
    ├── KeyboardInterrupt
    └── SystemExit

"""

#-------------------------------------------------------------------------------#
try:
    # Código que puede generar una excepción
    risky_operation()
except ExceptionType:
    # Código que se ejecuta si ocurre la excepción
    handle_error()

#-------------------------------------------------------------------------------#
#Without error handling
def divide(a, b):
    return a / b

# Esto hace que el programa se detenga
result = divide(10, 0)  # Programa crashea
print("Program continues...")  # Esta línea nunca se ejecuta

# With error handling
def divide(a, b):
    try:
        # Intentamos la operación riesgosa
        result = a / b
        return result
    except ZeroDivisionError:
        # Manejamos el error específico
        print("Error: Cannot divide by zero!")
        return None

result = divide(10, 0)
print(f"Result: {result}")
print("Program continues...")  # Esta línea SÍ se ejecuta
#-------------------------------------------------------------------------------#
def calculate(operation, a, b):
    try:
        if operation == "divide":
            result = a / b
        elif operation == "power":
            result = a ** b
        else:
            result = None
        return result
    except ZeroDivisionError:
        # Maneja división por cero
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        # Maneja tipos de datos incorrectos
        print("Error: Invalid data types")
        return None
    except OverflowError:
        # Maneja resultados demasiado grandes
        print("Error: Result is too large")
        return None

# Pruebas
print(calculate("divide", 10, 2))     # 5.0
print(calculate("divide", 10, 0))     # Error: Cannot divide by zero
print(calculate("divide", "10", 2))   # Error: Invalid data types
print(calculate("power", 10, 10000))  # Error: Result is too large

#-------------------------------------------------------------------------------#
def process_user_input(value):
    try:
        # Intentamos convertir a número
        number = int(value)
        # Intentamos calcular raíz cuadrada
        import math
        result = math.sqrt(number)
        return result
    except ValueError:
        # Captura errores de conversión o raíz cuadrada de negativos
        print(f"Error: '{value}' is not a valid number or is negative")
        return None
    except Exception as e:
        # Captura cualquier otra excepción
        print(f"Unexpected error occurred: {e}")
        return None

# Pruebas
print(process_user_input("16"))      # 4.0
print(process_user_input("hello"))   # Error: 'hello' is not a valid number
print(process_user_input("-4"))      # Error: '-4' is negative
#-------------------------------------------------------------------------------#
def safe_list_access(my_list, index):
    try:
        # Intentamos acceder al índice
        value = my_list[index]
        return value
    except IndexError as e:
        # Capturamos información detallada del error
        print(f"Error accessing index {index}: {e}")
        print(f"List length is {len(my_list)}")
        return None
    except TypeError as e:
        # Capturamos errores de tipo
        print(f"Error with index type: {e}")
        return None

# Pruebas
numbers = [10, 20, 30, 40, 50]
print(safe_list_access(numbers, 2))      # 30
print(safe_list_access(numbers, 10))     # Error: list index out of range
print(safe_list_access(numbers, "two"))  # Error with index type