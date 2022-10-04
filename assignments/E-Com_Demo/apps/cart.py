from typing import Dict,Tuple


class Cart():
    
    def __init__(self) -> None:
        self._items : Dict[int,Tuple] = {}
    def __str__(self):
        return (self.items_show())
    def add_items(self,product,quantity=1):
        self._items[product.id] = (product,quantity)    
    

    def remove_items(self,product)-> None:
        product,quantity = self._items.pop(product.id)
        print("-------------------------------")
        return f"{product.name} removed from cart"
        

    def items_show(self):
        if not self._items:
           print("No items in the cart :")
           return
        
        print("---------------------------------")
        print("Items in the Cart are as follows :")
        
        for key,data in self._items.items():
            print(' |ID:',key,'\n |Product name:',data[0].name,'\n |Quantity :',data[1])
        print(self.totalprice())

    def totalprice(self):
        total=0
        for key,data in self._items.items():
           pr= data[0].price - data[0].discount
           qn=data[1]
           tot=pr*qn
           total=total+tot
        return "Total Price:",total
    

