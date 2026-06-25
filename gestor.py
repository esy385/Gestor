from gasto import Gasto
import json
import datetime
import time

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
        for pasada in range(len(self._gastos)):
            for gasto in range(len(self._gastos) - 1 - pasada):
                if self._gastos[gasto].monto > self._gastos[gasto+1].monto:
                    self._gastos[gasto], self._gastos[gasto+1] = self._gastos[gasto + 1], self._gastos[gasto]
        self.mostrar_gastos()
                
    
    def calcular_total_mensual(self):
        pass
    
    def guardar(self):
        datos = []
        
        for gasto in self._gastos:
            datos.append(gasto.to_dict())
        
        with open('datos.json', 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        
        print('Guardando datos...')
        time.sleep(2)
    
    def cargar(self):
        try:
            with open("datos.json", 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
            
            self._gastos = []    
            
            for gasto in datos:
                self._gastos.append(Gasto.from_dict(gasto))
        except FileNotFoundError:
            self._gastos = []
        
        print('Cargando datos...')
        time.sleep(2)
            
           
    
            
    