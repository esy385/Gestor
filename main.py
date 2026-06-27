from gestor import GestorGastos

def menu():
    gestor = GestorGastos()
    while True:
        print(f'\n1. Agregar gasto\n2. Ver gastos\n3. Buscar por categoria\n4. Ordenar por monto\n5. Calcular total mensual\n6. Convertir CLP a USD\n7. Guardar datos\n8. Cargar datos\n9. Salir\n')
        
        try:
            opcion = int(input("Ingresa una opcion: "))
        except ValueError:
            print("Ingresa una opcion valida.")
        
        match opcion:
            case 1:
                gestor.agregar_gasto()
            case 2:
                gestor.mostrar_gastos()
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