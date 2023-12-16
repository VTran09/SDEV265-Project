from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from  collections import OrderedDict 
from pymongo import MongoClient

class AdminWindow(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    

def get_users(self):
    client = MongoClient()
    db = client.silverpos
    users = db.users
    _users = OrderedDict(
        first_names = [],
        last_names = [],
        user_names = [],
        passwords = [],
        designations = []
        )
    first_names = []
    last_names = []
    user_names = []
    passwords = []
    designations = []
    for user in users.find():
        first_names.append(user['first_name'])
        last_names.append(user['last_name'])
        user_names.append(user['user_name'])
        passwords.append(user['password'])
        designations.append(user['designation'])

    #print(designations)
    users_length = len(first_names)
    idx = 0
    while idx < users_length:
         _users['first_names'][idx] = first_names[idx]
         _users['last_names'][idx] = last_names[idx]
         _users['user_names'][idx] = user_names[idx]
         _users['passwords'][idx] = passwords[idx]
         _users['designations'][idx] = designations[idx]

    idx += 1
    
    return _users

def get_products(self):
    client = MongoClient()
    db = client.silverpos
    products = db.stocks
    _stocks = OrderedDict()
    _stocks['product_code'] = {}
    _stocks['product_name'] = {}
    _stocks['product_weight'] = {}
    _stocks['in_stock'] = {}
    _stocks['sold'] = {}
    _stocks['order'] = {}
    _stocks['last_purchase'] = {}
    
    
    product_code = []
    product_name = []
    product_weight = []
    in_stock = []
    sold = []
    order = []
    last_purchase = []


    for product in products.find():
        product_code.append(product['product_code'])
        product_name.append(product['product_name'])
        product_weight.append(product['product_weight'])
        in_stock.append(product['in_stock'])
        sold.append(product['sold'])
        order.append(product['order'])
        last_purchase.append(product['last_purchase'])

    # print(designations)
    products_length = len(product_code)
    idx = 0
    while idx < products_length:
         _stocks['product_code'][idx] = product_code[idx]
         _stocks['product_name'][idx] = product_name[idx]
         _stocks['product_weight'][idx] = product_weight[idx]
         _stocks['in_stock'][idx] = in_stock[idx]
         _stocks['sold'][idx] = sold[idx]
         _stocks['order'][idx] = order[idx]
    _stocks['last_purchase'][idx] = last_purchase[idx]


    idx += 1
    
    return _stocks


class AdminApp(App):
        def build(Self):

            return AdminWindow()
    
if __name__=='__main__':
    AdminApp().run