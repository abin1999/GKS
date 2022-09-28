class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Details(self):
        return f"{self.name}'s Age is {self.age}."
    def Update_name(self,name):
        self.name=name
    def Update_age(self,age):
        self.age=age
def main():
    P1=Person('jojo',22)
    P2=Person('ram',33)
    print("\n\n==Before updation==")
    print("P1 Details is:\n",P1.Details())
    print("P2 Details is:\n",P2.Details())
    P1.Update_age(45)
    P2.Update_name(f'Mr.{P2.name}')
    print("\n\n==After updation==")
    print("P1 Details is:\n",P1.Details())
    print("P2 Details is:\n",P2.Details())

def main2():
    persons=[('arun',22),('sanal',36),('rahul',17)]
    per=[Person(name,age)for name,age in persons]
    print("persons details are using list")
    for p in per:
        print(p.Details())

def main3():
    persons=[('arun',22),('sanal',36),('rahul',17)]
    per={name:Person(name,age)for name,age in persons}
    arun=per.get('arun')
    arun.Update_age(45)
    print("personnel details are using dictionary")
    for key,p in per.items():
        print(f"{key}:{p.Details()}")
if __name__=='__main__':
    main()
    main2()
    main3()

