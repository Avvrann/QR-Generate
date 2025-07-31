import qrcode
from pathlib import Path

# Creamos el el objeto qr con el tamano del qr ,el de los cubos y el borde
qr = qrcode.QRCode(version=3, box_size=20, border=5, error_correction=qrcode.constants.ERROR_CORRECT_H)
ruta_img = Path()
def menu():
    print("===========================")
    print("|| 1 : Importar archivo  ||")
    print("|| 2 : Generar QR        ||")
    print("|| 3 : Ruta de Imagen QR ||")
    print("===========================")


def case():
    opt = int(input())
    match opt:
        case 1:
            importar_archivo()
        case 2 : 
            generar_qrcode()
        case 3 :
            agg_ruta()

# Importar la ruta del archivo que vamos a codificar
def importar_archivo():
    ruta = Path(input("Ruta del a archivo a codificar: "))
    if ruta.exists():
        global data
        data = open(ruta).read()
    else :
        print("Ruta invalida")
    main()    

# Generar el codigo qr
def generar_qrcode():
    qr.add_data(data)
    qr.make(fit = True)
    generar_img()        
    main()  

def generar_img():
        img = qr.make_image(fill_color="black", back_color="white")
        if ruta_img.is_dir():
            save_path = ruta_img / "qr_code.png"
        elif ruta_img.exists():
            save_path = ruta_img
        else:
            save_path = "qr_code.png"
        img.save(save_path)

# De forma opcional podemos cambiar la ruta donde se guradara la imagen
def agg_ruta():
    global ruta_img
    ruta_img = Path(input("Ruta de la imagen QR: "))
    main()

def main():
    menu()
    case()

main()