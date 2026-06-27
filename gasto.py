class Gasto:
    def __init__(self, descripcion, monto, categoria, mes):
        self.descripcion = descripcion
        self.monto = monto
        self.categoria = categoria
        self._mes = mes
        
    def __repr__(self):
        return f'{self.descripcion} - ${self.monto} - Mes:{self._mes}'
    
    def to_dict(self):
        return {
            'descripcion' : self.descripcion,
            'monto' : self.monto,
            'categoria' : self.categoria,
            'mes' : self._mes
            
        }
        
    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos['descripcion'],
            datos['monto'],
            datos['categoria'],
            datos['mes']
        )
        
    
    
    
    
