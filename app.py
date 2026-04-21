# Cambios Rafael Espinosa
import os

def listar_carpetas(ruta):
    try:
        carpetas = []  # lista donde guardamos carpetas

        for elemento in os.listdir(ruta):
            ruta_completa = os.path.join(ruta, elemento)
            if os.path.isdir(ruta_completa):
                carpetas.append(elemento)

        return carpetas

    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    ruta = "D:\\"
    lista_carpetas = listar_carpetas(ruta)

    print("\n📂 Lista de carpetas en el Ambito de Gestion DTIC:\n")
    print(lista_carpetas)