from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

from kivy.clock import Clock, mainthread

from kivy.properties import StringProperty, ListProperty, ColorProperty, NumericProperty, ObjectProperty, BooleanProperty

from random import randint

from widgets.popups import ConfirmDialog

Builder.load_file('views/pos/pos.kv')
class Pos(BoxLayout):
    current_total = NumericProperty(0.0)
    current_cart = ListProperty([])
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
        

        
    def render(self, _):
        prods = [
            {
                "name": "Chii Cheese Etouffee with Crawfish",
                "pcode": "01",
                "price": 11.99,
                "qty": 0,
            },
            {
                "name": "Drunken Chicken",
                "pcode": "02",
                "price": 9.99,
                "qty": 0,
            },
            {
                "name": "Red Beans with Smoked Sausage",
                "pcode": "03",
                "price": 10.99,
                "qty": 0,
            },
            {
                "name": "Gumbo",
                "pcode": "04",
                "price": 12.99,
                "qty": 0,
            },
            {
                "name": "White Chili with Chicken",
                "pcode": "05",
                "price": 10.99,
                "qty": 0,
            },
            {
                "name": "Maque Choux",
                "pcode": "06",
                "price": 9.99,
                "qty": 0,
            },
            {
                "name": "Jambalaya",
                "pcode": "07",
                "price": 11.99,
                "qty": 0,
            },
            {
                "name": "Chipotle Alexio",
                "pcode": "08",
                "price": 10.99,
                "qty": 0,
            },
            {
                "name": "Italiano",
                "pcode": "09",
                "price": 10.99,
                "qty": 0,
            },
            {
                "name": "Black Chili",
                "pcode": "10",
                "price": 12.99,
                "qty": 0,
            },
            {
                "name": "Caribbean Jerk Etouffee",
                "pcode": "11",
                "price": 11.99,
                "qty": 0,
            },
            {
                "name": "Chorizo Etouffee",
                "pcode": "12",
                "price": 10.99,
                "qty": 0,
            },
            {
                "name": "Chicken Creole",
                "pcode": "13",
                "price": 10.99,
                "qty": 0,
            },
            {
                "name": "Curry Chicken and Mushroom Etouffee",
                "pcode": "14",
                "price": 11.99,
                "qty": 0,
            },
            {
                "name": "B&B (Vegetarian)",
                "pcode": "15",
                "price": 10.99,
                "qty": 0,
            },
            {
                "name": "Spinach and Mushroom Etouffee (Vegetarian)",
                "pcode": "16",
                "price": 10.99,
                "qty": 0,
            },
            {
                "name": "Vegan White Chili (Vegan)",
                "pcode": "17",
                "price": 10.99,
                "qty": 0,
            }
        ]
        for prod in prods:
            self._add_product(prod)  
        
    
    def update_total(self):
        prods = self.ids.gl_receipt.children
        
        _total = 0
        for c in prods:
            _total += round(float(c.price)*int(c.qty), 2)
            
        self.current_total = _total + (_total*.07)
        
    def on_current_cart(self, inst, cart):
        print("Refreshing....")
        print(cart)
        self.ids.gl_receipt.clear_widgets()
        
        widget_to_remove  = None
        for widget in self.ids.gl_receipt.children:
            if widget.pcode == inst.pcode:
                widget_to_remove = widget
                break
        if widget_to_remove:
            self.ids.gl_receipt.remove_widget(widget_to_remove)
            cart.append(inst)
        
        for f in cart:
            self.add_receipt_item(f)
            
        
        self.update_total()    

    
    def _add_product(self, product: dict):
        grid = self.ids.gl_products
        
        pt = ProductTile()
        pt.name = product.get("name", "")
        pt.pcode = product.get("pcode", "")
        pt.qty = product.get("qty", 0)
        pt.price = product.get("price", 0)
        pt.qty_callback = self.qty_control
        
        print("Adding product")
        print(pt.name)
        print(pt.pcode)
        print(pt.price)
        print(pt.qty)
        
        grid.add_widget(pt)
        
    def add_receipt_item(self, item: dict) -> None:
        rc = ReceiptItem()
        rc.name = item['name']
        rc.qty = item['qty']
        rc.price = item['price']
        
        self.ids.gl_receipt.add_widget(rc)
    
    def qty_control(self, tile, increasing=False):
        _qty = int(tile.qty)
        
        #temp = list(filter(lambda x: x['pcode'] == tile.pcode, self.current_cart))
                
        if increasing:
            _qty += 1
        else:
            _qty -= 1
            
            if _qty < 0:
                # Ask user if they want to delete this product
                _qty = 0
        
        data = {
            "name": tile.name,
            "pcode": tile.pcode,
            "price": tile.price,
            "qty": 0
        }
        
        
        tgt = None
        temp = list(self.current_cart)
        for i, x in enumerate(temp):
            if x['pcode'] == tile.pcode:
                tgt = i
                break
            
        data['qty'] = _qty
        data['price'] = (data['price'])
        
        if tgt is not None:
            self.current_cart[tgt]['qty'] = _qty
            self.on_current_cart(data, self.current_cart)
        else:
            self.current_cart.append(data)
        
        tile.qty = _qty
        print("qty_control is called")
        print(tile.name)
        print(tile.pcode)
        print(tile.price)
        print(tile.qty)
        print(temp)

        
        
    def checkout_callback(self, posview):
        self.current_cart = []
        for item in self.ids.gl_products.children:
            item.qty = 0
        
    def checkout(self):
        dc = ConfirmDialog()
        dc.title = "Checkout"
        dc.subtitle = "Are you sure you want to check out this cart?"
        dc.textConfirm = "Yes, Checkout"
        dc.textCancel = "Cancel"
        dc.confirmColor = App.get_running_app().color_primary
        dc.cancelColor = App.get_running_app().color_primary
        dc.confirmCallback = self.checkout_callback
        dc.open()
        
    

class ProductTile(BoxLayout):
    pcode = StringProperty("")
    name = StringProperty("")
    qty = NumericProperty(0)
    price = NumericProperty(0)
    qty_callback = ObjectProperty(allownone=True)
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
        
    def render(self, _):
        pass
    

class ReceiptItem(BoxLayout):
    name = StringProperty("")
    qty = NumericProperty(0)
    price = NumericProperty(0)
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
        
    def render(self, _):
        pass
    
