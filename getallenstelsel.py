
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

def system_to_decimal(input, system):
    string_numbers = str(input)
    result_decimal = 0
    for string_index in range(len(string_numbers)):
        number = int(string_numbers[string_index])
        power = system ** (len(string_numbers) - string_index - 1)
        # print(f"{str(string_index)} {number} {power}")
        result_decimal += power * number
    return result_decimal

print()

test_bin = 111101
out_dec_bin = system_to_decimal(test_bin, 2)
print(f"{test_bin} -> {out_dec_bin}")

test_oct = 7623
out_dec_oct = system_to_decimal(test_oct, 8)
print(f"{test_oct} -> {out_dec_oct}")

test_hex = 12124
out_dec_hex = system_to_decimal(test_hex, 16)
print(f"{test_hex} -> {out_dec_hex}")