from paciente import Paciente

def main():
    # Crear paciente con contructor __init__
    p1 = Paciente("11.111.111-1", "Gabriel Mendez", 40, "Isapre")
    # Mostrar informacion del paciente
    # __str__ es el llamado automaticamente al imprimir el objeto
    print(p1)
if __name__ == "__main__":
    main()