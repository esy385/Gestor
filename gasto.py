class Gasto:
    def __init__(self, descripcion, monto, categoria):
        self.descripcion = descripcion
        self.monto = monto
        self.categoria = categoria
        
    def __repr__(self):
        return f'{self.descripcion} - ${self.monto}'
    
    def to_dict(self):
        return {
            'descripcion' : self.descripcion,
            'monto' : self.monto,
            'categoria' : self.categoria
        }
        
    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos['descripcion'],
            datos['monto'],
            datos['categoria']
        )
        
    
    
    
    
