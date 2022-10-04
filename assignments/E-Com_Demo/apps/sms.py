from cart import Cart
from product import Product
class Sms:
    def send_sms()-> None:
        f=open("demofile.txt", "w")
        f.write("Product Added")
        f.close()
        return f"product added confirmation sended as SMS"