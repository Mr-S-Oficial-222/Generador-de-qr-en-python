import qrcode

def generar(link):
    qr = qrcode.make(link)
    qr.save("qr.png")

print("generador de QR De Mr.S")
texto = input("pon tu enlace: ")
generar(texto)
