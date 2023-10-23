class Carrito:
    def __init__(self, id, list):
        self.userid=id
        self.list=list
    

    def toDBCollection(self):
        data={"userid":self.userid,"list":self.list}
        return data