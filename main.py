from gestor import GestorGastos
from gasto import Gasto
import time
def menu():
    gestor = GestorGastos()
    while True:
        print(f'{'-' * 10}MENU{'-' * 10}\n1. Agregar gasto\n2. Ver gastos\n3. Buscar por categoria\n4. Ordenar por monto\n5. Calcular total mensual\n6. Convertir CLP a USD\n7. Guardar datos\n8. Cargar datos\n9. Salir\n{'-' * 24}')
        
        try:
            opcion = int(input("Ingresa una opcion: "))
        except ValueError:
            print("Ingresa una opcion valida.")
        
        match opcion:
            case 1:
                gestor.agregar_gasto()
            case 2:
                gestor.mostrar_gastos()
                time.sleep(2)
            case 3:
                gestor.buscar_categoria()
            case 4:
                gestor.ordernar_por_monto()
            case 5:
                gestor.calcular_total_mensual()
            case 6:
                pass
            case 7:
                gestor.guardar()
            case 8:
                gestor.cargar()
            case 9:
                return
                
                
        
        
menu()