

while 1:
    try:
        numero = int(input('Digite um número'))
        print(1 / numero)
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("Infinito")
        break
    except Exception as e:
        print(f"Erro desconhecido: {e}")