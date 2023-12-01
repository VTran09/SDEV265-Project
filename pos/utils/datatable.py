from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from pymongo import MongoClient
from collections import OrderedDict

Builder.load_string('''
<DataTable>:
    id: main_win
    RecycleView: 
        viewclass: 'Label'
        id: table_floor
        RecycleGridLayout:
            cols: 5
            default_size: (None, 250)
            default_size_hint:(1,None)
            size_hint_y: None
            height: self.minimum_height
            spacing: 5
''')

class DataTable(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

products = self.get_products()

col_titles = [k for k in products.keys()]
rows_len = len(products[col_titles[0]])
print (col_titles)
print(rows_len)
table_data = []
for t in col_titles:
     table_data.append({'text': str(t)})
self.ids.table_floor.data = table_data





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

class DataTableApp(App):
        def build(Self):

            return DataTable()
    
if __name__=='__main__':
    DataTableApp().run