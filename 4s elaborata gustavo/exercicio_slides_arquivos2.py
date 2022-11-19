
arquivo = open("ips2.txt" , "r")
ips = arquivo.readlines()
validos = []
invalidos = []
for ip in ips:
    ip = ip.replace("\n", "")
    apoio = ip.split(".")

    apoio = [a for a in apoio if int(a) <= 255]
    if len(apoio) == 4:
        validos.append(ip)
    else:
        invalidos.append(ip)

saida = open("saida.txt" , "w")

saida.write(["Endereços válidos:]")
for v in validos:
    saida.write([f"{v}\n"])
    