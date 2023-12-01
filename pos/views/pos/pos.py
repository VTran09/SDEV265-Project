from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

from kivy.clock import Clock, mainthread

from kivy.properties import StringProperty, ListProperty, ColorProperty, NumericProperty, ObjectProperty, BooleanProperty

from random import randint

Builder.load_file('views/pos/pos.kv')
class Pos(BoxLayout):
    current_total = NumericProperty(0.0)
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
        
    def render(self, _):
        for x in range(3):
            #pcode = randint(10000000, 40000000)
            prod = {
                "name": f"Product {x}",
                "qty": 1,
                "price": 200.00,
                "pcode": str(randint(10000000, 40000000))
            }
            self.add_product(prod)
    
    def add_product(self, product: dict):
        grid = self.ids.gl_products
        
        pt = ProductTile()
        pt.name = product.get("name", "")
        pt.pcode = product.get("pcode", "")
        pt.qty = product.get("qty", 0)
        pt.price = product.get("price", 0)
        pt.qty_callback = self.qty_control
        
        grid.add_widget(pt)
    
    def qty_control(self, tile, increasing=False):
        _qty = int(tile.qty)
        
        if increasing:
            _qty += 1
        else:
            _qty -= 1
            
            if _qty < 0:
                # Ask user if they want to delete this product
                _qty = 0
        
        tile.qty = _qty
    

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