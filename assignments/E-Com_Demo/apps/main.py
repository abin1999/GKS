from product import Product
from user import User
from sms import Sms
from Email import email
from order import Order


user1_details=User(1,'jerin','kottayam','jerinseb521@gmail.com',8956767745)
user2_details=User(2,'arun','ernakulam','arun@gmail.com',67867845645)
print(user2_details.Details())
print("-----------------------")

print("----after updating----")
user2_details.update_details('thoma','ernakulam')
print(user2_details.Details())
print("------------------------")

laptop = Product(1,'laptop',100,50)
mouse = Product(2,'mouse',50,0)
book = Product(3,'book',15,5)

print("---Products Available---")
print(laptop.productdetails())
print("-------------------------")
print(mouse.productdetails())
print("-------------------------")
print(book.productdetails())
print("-------------------------")

user1_details.cart.add_items(laptop,5)
user1_details.cart.add_items(mouse,6)
user1_details.cart.add_items(book,10)

user2_details.cart.add_items(laptop,1)
user2_details.cart.add_items(book,2)

print(Sms.send_sms())
print(email.send_email())

user2_details.cart.items_show()
print(user2_details.cart.remove_items(laptop))
user2_details.cart.items_show()
user2_details.order.order_confirm(1,'book',15)




