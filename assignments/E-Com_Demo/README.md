## This Project is to mock a ecommerce platform
#### Here we collowing class based approch
#### The fecility in the platforms are following

        User
        Product
        ShoppingCart
        Order
        PaymentProcessor
        Email service [function based or class based][mock using print function and writing to file]
        SMS service [function based or class based][mock using print function and writing to file]

#####   User Deatils
            Userid,
            name,
            addrress,
            mobile,
            email
        
        features:
        -------------
            1.  Should be Able to create Users , View user Details.
            2.  Should be able to change the details such as name,address,etc..
            3.  Should be able to add/remove product to/from the Cart (quantity and product)
            4.  Should be able to order and pay the products in thier cart
            5.  Should send mail/sms to user in different occations[order/update details/payment]

#####   Product Deatils
            product_id
            name
            price
            discount


####    ShoppingCart

            1.  Should be able to see the items in the cart of that user.
            2.  Should be able to view the items in the cart,each item price(quantity*unitprice), view discount price ,view total price.
            3.  Should be able to add remove items from cart by each User


Try to use Following things in the project

1.  Learn About List Comprehension.

2.  Learn about python decorator
        impliment property decorator in class if required https://www.programiz.com/python-programming/property

2.  Learn About dataclasses
        Use dataclasses if required

3.  Use Type hints in the code   ==> https://docs.python.org/3/library/typing.html

4.  Try to make module like approch
        user.py
        product.py
        shoppingCart.py

