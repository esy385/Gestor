from gasto import Gasto
import json

class GestorGastos:
    def __init__(self):
        self._gastos = []
    
    def agregar_gasto(self):
        while True:
            try:
                descripcion,monto,categoria = input("Descripcion: "), int(input("Monto: ")), input("Categoria: ")
                break
            except ValueError:
                print("Ingresa el monto correctamente.")                
        self._gastos.append(Gasto(descripcion,monto,categoria))
        
    def mostrar_gastos(self):
        if self._gastos:
            print(self._gastos)
        else:
            print('No hay gastos')
    
    def buscar_categoria(self):
        categoria = input("Ingresa la categoria: ")
        for gasto in self._gastos:
            if gasto.categoria == categoria:
                print(gasto)
    
    def ordernar_por_monto(self):
        pass
    
    def calcular_total_mensual(self):
        pass
    
    def guardar(self):
        with open("datos.json", 'a', encoding='utf-8') as archivo:
            pass
    
    def cargar(self):
        with open("datos.json", 'r', encoding='utf-8') as archivo:
            pass
    
            
    