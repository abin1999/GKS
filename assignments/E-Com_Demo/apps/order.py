from random import choices
from cart import Cart
from product import Product

class Order:
    def order_confirm(self,productid:int,name:str,price:int):
        Cart.prodctid=productid
        Cart.name=name
        Cart.price=price
        choices=("do you want to confirm order:")
        if choices =="y":
            for key,data in self._items.items():
                print(' |ID:',key,'\n |Product id:',data[0].id,'\n |Product name:',data[0].name,'\n |price :',data[0].price)
            
            