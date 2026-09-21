from paciente import Paciente
pacientes: list[Paciente] = []

def agregar_paciente()->None:
    rut= input("Ingrese el Rut del paciente: ")
    nombre = input("Ingrese el Nombre del paciente ")
    edad =int(input("Ingrese la edad del apciente: "))
    print("previsiones disponibles: ")
    print("1.- Fonasa")
    print("2.- Isapre")
    prevision = input("Seleccione la prevencion del paciente: ")
    if prevision == "1":
            prevision = "Fonasa"
    else:
            prevision = "Isapre"

    Paciente = Paciente(rut, nombre, edad, prevision)
    pacientes.apprend (Paciente)
    print("Paciente agregado exitosamente.")

def leer_numero(mensaje:str)->int:
     while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese un número válido.")

def menu()->int:
    opcion=-1
    while opcion<0 or opcion>5:
      print("Menu clinica")
      print("1.- Agregar paciente")
      print("2.- Editar paciente")
      print("3.- Eliminar paciente")
      print("4.- Imprimir un paciente")
      print("5.- Imprimir todos los pacientes")
      print("0.- Salir")
      opcion = leer_numero("Seleccione una opcion ")
    return opcion

def main():
    op=-1
    while op!=0:
        op=menu()
        if op==1:
            print("Agregando paciente")
        elif op==2:
            print("Editando paciente")
        elif op==3:
            print("Eliminando paciente")
        elif op==4:
            print("Imprimiendo un paciente")
        elif op==5:
            print("Imprimiendo todos los pacientes")
        elif op==0:
            print("Saliendo del programa")
              
   
if __name__ == "__main__":
    main()