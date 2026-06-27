from gasto import Gasto
import json
from datetime import datetime # Calendario
import time # Pausar ejecucion

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
        mes = datetime.now().month              
        self._gastos.append(Gasto(descripcion,monto,categoria, mes))
        
    def mostrar_gastos(self):
        if self._gastos:
            print(self._gastos)
        else:
            print('No hay gastos')
    
    def buscar_categoria(self):
        if self._gastos:
            categoria = input("Ingresa la categoria: ")
            for gasto in self._gastos:
                if gasto.categoria == categoria:
                    print(gasto)
        else:
            print("No hay gastos")
    
    def ordernar_por_monto(self):
        temp_list = self._gastos.copy()
        if temp_list:
            for pasada in range(len(temp_list)):
                for gasto in range(len(temp_list) - 1 - pasada):
                    if temp_list[gasto].monto > temp_list[gasto+1].monto:
                        temp_list[gasto], temp_list[gasto+1] = temp_list[gasto + 1], temp_list[gasto]
            
            print(temp_list)
        else:
            print("No hay gastos.")
    
    def calcular_total_mensual(self):
        if self._gastos:
            mes_actual = datetime.now().month
            total = 0
            for gasto in self._gastos:
                if gasto._mes == mes_actual:
                    total += gasto.monto
            print(f'El total mensual es de: {total}')
        else:
            print("No hay gastos")           
    
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
            
           
    
            
    