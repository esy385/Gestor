from gasto import Gasto
import json

class GestorGastos:
    def __init__(self):
        self._gastos = []
    
    def agregar_gasto(self, gasto):
        self._gastos.append(gasto)
        
    def mostrar_gastos(self):
        if self._gastos:
            print(self._gastos)
        else:
            print('No hay gastos')
    
    def buscar_categoria(self, categoria):
        for gasto in self._gastos:
            if gasto.categoria == categoria:
                print(gasto)
    
    def ordernar_por_monto(self):
        pass
    
    def calcular_total(self):
        suma = 0
        if self._gastos:
            for gasto in self._gastos:
                suma += gasto.monto
        else:
            print('No hay gastos')
    
    def guardar(self):
        with open("datos.json", 'a', encoding='utf-8') as archivo:
            pass
    
    def cargar(self):
        with open("datos.json", 'r', encoding='utf-8') as archivo:
            pass
    
            
    