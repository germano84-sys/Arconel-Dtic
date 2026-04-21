import os

def listar_carpetas(ruta):
    try:
        print(f"\n📂 Carpetas en: {ruta}\n")
        for elemento in os.listdir(ruta):
            ruta_completa = os.path.join(ruta, elemento)
            if os.path.isdir(ruta_completa):
                print(f"- {elemento}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ruta = "D:\\"
    listar_carpetas(ruta)