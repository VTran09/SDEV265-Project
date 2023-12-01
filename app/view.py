
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class MainWindow(BoxLayout):
    username = "first.samuel"
    role = StringProperty("user")
    
    def __init__(self, **kw):
        super().__init__(**kw)
