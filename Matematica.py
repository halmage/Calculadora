# Librerias del sistema
from database.CalculadoraTable import CalculadoraTable
from Calculadora import Calculadora
from package.Otros import Otros

# Librerias externa
from os import system
import time


class Matematica:

    def menu(self):
        # Menu de operaciones
        presentacion_menu = """
        ***********************
        + Menu de operaciones +
        ***********************
                           """
        print(presentacion_menu)
        print("0.Crear base de datos")
        print("1. Calculadora")
        print("2. Salir")
        self.opcion = input("Ingrese una opcion: ")
        while self.opcion.isdigit() == False:
            # VERIFICANDO LA VARIABLE num1
            print("ERROR: la variable opcion tiene que ser numerico")
            self.opcion = input("Ingrese una opcion: ")

    def operaciones(self):
        # Operaciones que se relieazara en el sistema
        while True:
            self.menu()
            if self.opcion == "2":
                # Salida del sistema
                Otros.cargando(self)
                print("Hasta luego!")
                time.sleep(1)
                system("clear")
                break
            elif self.opcion == "0":
                # Creacion de la base de datos
                matematica = CalculadoraTable()
                matematica.createDatabase()
                time.sleep(2)  # Pausa de 1 segundo par1a visualizar el resultado
                system("clear")
            elif self.opcion == "1":
                # Salir del sistema
                system("clear")
                Calculadora.operaciones(
                    self
                )  # Pausa de 1 segundo para visualizar el resultado
            else:
                # Opcion invalida
                print("\n✖ Opcion invalida, intente nuevamente.")
                Otros.cargando(self)
                system("clear")


matematica = Matematica()
matematica.operaciones()
