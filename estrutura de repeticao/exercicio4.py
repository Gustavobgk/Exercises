

ano = 0
a = 80000
b = 200000

while a < b:
    a = a + (a* 0.03)
    b = b + b * 0.015
    ano += 1

print(f"Passaram {ano} anos")