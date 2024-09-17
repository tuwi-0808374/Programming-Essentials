
def decimal_to_system(decimal, number_system):
    string_numer = ""
    while decimal > 1:
        decimal = decimal / number_system
        remainder = decimal - int(decimal)
        rest = remainder * number_system
        chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        string_numer = str(chars[int(rest)]) + string_numer
    return string_numer

decimaal = 372
result_bin = decimal_to_system(decimaal, 2)
result_oct = decimal_to_system(decimaal, 8)
result_hex = decimal_to_system(decimaal, 16)

print(f"Decimale input: {decimaal}")
print(f"Binair: {result_bin}")
print(f"Octaal: {result_oct}")
print(f"Hexidecimaal: {result_hex}")

def system_to_decimal(input_number, system):
    hex_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    input_number = input_number.upper()
    result_decimal = 0
    for string_index in range(len(input_number)):
        number = int(hex_chars.index(input_number[string_index]))
        power = system ** (len(input_number) - string_index - 1)
        result_decimal += power * number
    return result_decimal

print()

test_bin = "111101"
out_dec_bin = system_to_decimal(test_bin, 2)
print(f"Input binair: {test_bin} -> Uitkomst decimaal: {out_dec_bin}")

test_oct = "7623"
out_dec_oct = system_to_decimal(test_oct, 8)
print(f"Input octaal: {test_oct} -> Uitkomst decimaal: {out_dec_oct}")

test_hex = "ee44"
out_dec_hex = system_to_decimal(test_hex, 16)
print(f"Input heximaal: {test_hex} -> Uitkomst decimaal: {out_dec_hex}")
