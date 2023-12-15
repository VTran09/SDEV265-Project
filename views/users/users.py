from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp

from kivy.clock import Clock, mainthread

from kivy.properties import StringProperty, NumericProperty, ObjectProperty, ListProperty, ColorProperty


Builder.load_file("views/users/users.kv")

class Users(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
        
    def render(self, _):
        pass
