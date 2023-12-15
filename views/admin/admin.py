from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock, mainthread

Builder.load_file("views/admin/admin.kv")

class Admin(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)