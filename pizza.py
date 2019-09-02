import datetime
from datetime import date
class Food:

    def __init__(self,type):
        self.type = type

    @property
    def description(self):
        return self.type

class Pasta(Food):

    pasta_types = {"carbonara":24,
                   "Penne Siciliene":22,
                   "Al forno":28}

    def __init__(self,type,name):
        super().__init__(type)
        self.name = name
        self.pret = Pasta.pasta_types[name]

    @property
    def description(self):
        return self.type,self.name,self.pret

class Customer:

    CustomerId = 1000
    CardId = 2000


    def __init__(self,first,last,has_card):
        Customer.CustomerId += 1
        Customer.CardId += 1
        self.customerID = Customer.CustomerId
        self.first = first
        self.last = last
        self.has_card = has_card

        if self.has_card == True:
            self.CardId = Customer.CardId
        else:
            self.CardId = None

    def add_card(self):
            self.has_card = True
            self.CardId = Customer.CardId

    def rem_card(self):
            self.has_card = False
            self.CardId = None

    @property
    def description(self):
        return 'First name',self.first,'Last Name',self.last,'Customer ID', self.customerID ,'Card ID',self.CardId,'Posesor de card',self.has_card

class Order:

    OrderID = 0

    def __init__(self,customer,produse = []):
        Order.OrderID += 1
        self.CustomerID = customer.customerID
        self.produse = produse
        self.Order_number = Order.OrderID
        self.to_apply_discount = customer.has_card
        self.calculate_price()

    def add_products(self,prod):

        self.produse.append(prod)
        self.calculate_price()

    def rem_products(self,prod):
        if prod not in self.produse:
            print ("Produsul nu se afla in cos")
        else:
            self.produse.remove(prod)
            self.calculate_price()

    def calculate_price(self):

        self.pret = 0
        if self.to_apply_discount == True:
            coeficient = 0.8
        else:
            coeficient = 1
        for x in self.produse:
            self.pret = self.pret+x.pret

        self.pret = self.pret * coeficient


    @property
    def description(self):
        for x in self.produse:
            print(x.description)
        return 'Numarul comenzii',self.Order_number,'Id Client:',self.CustomerID,'Se Aplica reducere',self.to_apply_discount,'Pret total comanda:',self.pret


class Pizza(Food):

    nr_of_pizzamade = 0
    default_ingredients = ['mozarella','sos_rosii']
    blaturi = {"Subtire":24,"Normal":22,"Pufos":20,}
    dimensiuni = {"Mare":1.3,"Mic":1}
    ingrediente_pizza_default = {"Quatro_Stagione":['peperoni','sunca','masline','ciuperci'],
                                 "Prosciuto_Fungi":['prosciuto','funghi'],
                                 "Quatro_Formagi":['branza','branza','branza','branza'],
                                 "Suprema":['sunca','bacon','ananas','porumb','broclli']
                                 }


    def __init__(self,type,blat,dimensiune,toppings,name):
        super().__init__(type)
        self.blat = blat
        self.dimensiune = dimensiune
        self.ingrediente = Pizza.default_ingredients.copy()
        self.addtoping(toppings)
        self.name=name
        self.set_price()
        Pizza.nr_of_pizzamade += 1

    @classmethod
    def create_pizza(cls,type,nume,dimensiune,blat):
        if nume in Pizza.ingrediente_pizza_default:
            created_pizza = cls(type,blat,dimensiune,[],nume)
            created_pizza.addtoping(Pizza.ingrediente_pizza_default[nume])
            created_pizza.set_price()
            return created_pizza
        else:
            print('Nu avem acest tip de pizza')

    def set_price(self):

        if self.blat in Pizza.blaturi:
            pret_blat = Pizza.blaturi[self.blat]
        else:
            pret_blat = Pizza.blaturi["Normal"]

        if self.dimensiune in Pizza.dimensiuni:
            pret_dimensiune=Pizza.dimensiuni[self.dimensiune]
        else:
            pret_dimensiune=Pizza.dimensiuni["Mic"]

        if len(self.ingrediente) <= 2:
            pret_ingrediente = 0
        else:
            pret_ingrediente = 2 * (len(self.ingrediente)-2)

        self.pret = (pret_blat * pret_dimensiune + pret_ingrediente) * Pizza.weekday_price()

    @property
    def get_price(self):
        return self.pret

    @property
    def description(self):
        return self.name, self.blat,self.dimensiune,self.ingrediente,self.pret,self.type

    def addtoping(self,topping):
        self.ingrediente.extend(topping)
        self.set_price()

    def removetopings(self,toping):
        for x in toping:
            print(x)
            try:
                self.ingrediente.remove(x)
            except:
                print('Topingul',x,'nu se afla pe pizza!')
        self.set_price()

    def removealltoppings(self):
        self.ingrediente=Pizza.default_ingredients.copy()
        self.set_price()

    @staticmethod
    def weekday_price():
        day = date.today().weekday()
        if day == 6:
            coeficient = 1.1
        elif day == 1:
            coeficient = 0.8
        else:
            coeficient = 1
        return(coeficient)

Razvan = Customer('Razvan','Nitu',True)
Razvan2 = Customer('xxx','yyyy',False)
pizza1 = Pizza('Pizza','Subtire', 'Mare', ['x', 'y', 'z'],'Quatro_Formagi')
pizza1 = Pizza('Pizza','Subtire', 'Mare', ['x', 'y', 'z','t'],'margherita')
#pizza1.getdescription()
#pizza1.addtoping(['sunca', 'carnati', 'porumb'])
#pizza1.calculatorpizza()
#pizza1.getdescription()
#pizza1.removealltoppings()
#pizza1.getdescription()
pizza3=Pizza.create_pizza('Pizza','Quatro_Stagione','Mare','Pufos')
#pizza4=Pizza.create_pizza('Quatro_Formagi','Mare','Pufos')
#pizza4=Pizza.create_pizza('Suprema','Mare','Pufos')

pasta1 = Pasta('Paste','carbonara')
Order1 = Order(Razvan,produse = [pizza1,pasta1])
Order2 = Order(Razvan2,produse = [pasta1,pizza3,pizza1])
#Order2.add_products(pasta1)

import pdb; pdb.set_trace()










#day1=date.today()
#day = day1.weekday()
#print(day)

#pizza1.weekday(date.today())

#pizza3.weekday(day)















