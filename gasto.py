class Gasto:
    def __init__(self, descripcion, monto, categoria):
        self.descripcion = descripcion
        self.monto = monto
        self.categoria = categoria
        
    def __repr__(self):
        return f'{self.descripcion} - ${self.monto}'
    
    
