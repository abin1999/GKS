class Product:
    def __init__(self,productid:int,name:str,price:int,discount:int):
        self.id=productid
        self.name=name
        self.price=price
        self.discount=discount
        
        
    def productdetails(self):
        return f"productid:{self.id}\nname:{self.name}\nprice:{self.price}\ndiscount:{self.discount}"


# if __name__=='__main__':
#    product()