def is_decimal(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False

def is_hexadecimal(input_str):
    hex_digits = set("0123456789abcdefABCDEF")
    return all(char in hex_digits for char in input_str)

def decimal_to_hexadecimal(decimal_str):
    decimal_int = int(decimal_str)
    hexadecimal_str = ""
    while decimal_int > 0:
        remainder = decimal_int % 16
        hexadecimal_str = "0123456789ABCDEF"[remainder] + hexadecimal_str
        decimal_int //= 16
    return hexadecimal_str

def hexadecimal_to_decimal(hexadecimal_str):
    hexadecimal_str = hexadecimal_str.upper()
    decimal_int = 0
    for char in hexadecimal_str:
        decimal_int = decimal_int * 16 + "0123456789ABCDEF".index(char)
    return str(decimal_int)

input_str = input("Enter a number: ")

if is_decimal(input_str):
    print("Valid decimal input")
    print("Hexadecimal equivalent:", decimal_to_hexadecimal(input_str))
elif is_hexadecimal(input_str):
    print("Valid hexadecimal input")
    print("Decimal equivalent:", hexadecimal_to_decimal(input_str))
else:
    print("Invalid input")