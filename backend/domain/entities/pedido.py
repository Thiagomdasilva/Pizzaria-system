class Pedido:
    def __init__(
            self, 
            id, 
            cliente, 
            pizza, 
            quantidade):
        
        self.id = id
        self.cliente = cliente
        self.pizza = pizza
        self.quantidade = quantidade