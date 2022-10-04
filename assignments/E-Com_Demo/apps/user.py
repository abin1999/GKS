from cart import Cart
from order import Order

class User:
    def __init__(self,userid:int,name:str,address:str,email:str,phone:int):
        self.userid=userid
        self.name=name
        self.address=address
        self.email=email
        self.phone=phone
        self.cart = Cart()
        self.order = Order()

    
    def Details(self):
        return f"userid:{self.userid}\nname:{self.name}\naddress:{self.address}\nemail:{self.email}\nphone:{self.phone}"

    def update_details(self,name,address):
        self.name=name
        self.address=address

if __name__=='__main__':
    pass
   

   
   