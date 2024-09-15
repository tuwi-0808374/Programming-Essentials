
def decimal_to_system(decimal, number_system):
    string_numer = ""
    while decimal > 1:
        decimal = decimal / number_system
        remainder = decimal - int(decimal)
        rest = remainder * number_system
        chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        string_numer = str(chars[int(rest)]) + string_numer
    return string_numer

decimaal = 600
result_bin = decimal_to_system(decimaal, 2)
result_oct = decimal_to_system(decimaal, 8)
result_hex = decimal_to_system(decimaal, 16)

print(f"{decimaal}")
print(f"Binair: {result_bin}")
print(f"Octaal: {result_oct}")
print(f"Hexidecimaal: {result_hex}")