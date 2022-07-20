import time
dmt =  [{'id' : 1,'Name':'sugar','price':40},{'id' : 2,'Name':'tea','price':500},
        {'id' : 3,'Name':'liril','price':70},
        {'id' : 4,'Name':'rin','price':10},{'id' : 5,'Name':'vim','price':10},
        {'id' : 6,'Name':'rin poder','price':180},{'id' : 7,'Name':'saffola gold','price':1300},
        {'id' : 8,'Name':'rice','price':58},
        {'id' : 9,'Name':'wheat','price':30},{'id' : 10,'Name':'almond','price':900},
        {'id' : 11,'Name':'kaju','price':1200},{'id' : 12,'Name':'suace','price':120}]
trolly = []
class Dmart:

    def __init__(self,bal):
        self.bal = bal
        pass

    def buy(self,product):
        self.bal+= product

        pass

    def cell(self, total_amt):

        pass

nm = input('enter your name:')
time.sleep(1)
d = Dmart(nm)
print('------------------------------------')
print('Welcome to Dmart',nm)
print('-------------------------------------')
time.sleep(2)
print('what you want to buy')
time.sleep(2)
print('1.accesories,\n2.cloth ,\n3.kitchen tools,\n4.vegitables,\n5.exist')
print('-------------------------------------------')
n = input('Enter your choice please:')
for choice in dmt:
    print(choice)
    if choice["id"] == n:
        print(choice)

