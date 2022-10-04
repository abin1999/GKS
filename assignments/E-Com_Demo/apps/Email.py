class email:
    def send_email():
        f=open("demoemail.txt", "w")
        f.write("Product Added")
        f.close()
        return f"Product added confirmation sended as email"