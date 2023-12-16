from kivy.app import App
from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout

Builder.load_file("views/auth/auth.kv")
class Auth(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        
    def authenticate(self):
        App.get_running_app().root.ids.scrn_mngr.current = 'scrn_home'
