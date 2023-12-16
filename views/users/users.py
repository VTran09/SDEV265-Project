from kivy.app import App
from threading import Thread
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
        t1 = Thread(target=self.get_users, daemon=True)
        t1.start
    
    def get_users(self):
        users =  [

        {
                "firstName": "Andrew"
                "lastName": "Rehfeldt"
                "username": "firstAndrew"
                "password": "schoolproject"
                "created": "12/12/2023 10:02:23 PM"
                "signedIn": "12/15/2023 11:47:10 AM"
        },
        {
                "firstName": "James"
                "lastName": "Ramsey"
                "username": "firstJames"
                "password": "schoolproject"
                "created": "12/12/2023 10:02:25 PM"
                "signedIn": "12/15/2023 11:47:11 AM"
        },
        {
                "firstName": "Van"
                "lastName": "Tran"
                "username": "firstVan
                "password": "schoolproject"
                "createdAt": "12/12/2023 10:02:29 PM"
                "signedIn": "12/15/2023 11:47:19 AM"
        }
        
        ]

        self.set_users(users)

    @mainthread
    def set_users(self, users:list):
        grid = self.ids.gl_users
        grid.clear_widgets()

        for u in users:
            ut = UserTile()
            ut.first_name = u['firstName']
            ut.last_name = u['lastName']
            ut.username = u['username']
            ut.password = u['password']
            ut.created = u['createdAt']
            ut.last_login = u['signIn']

            grid.add_widget(ut)




class UserTile(BoxLayout):
    first_name = StringProperty("")
    last_name = StringProperty("")
    username = StringProperty("")
    password = StringProperty("")
    created = StringProperty("")
    last_login = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
        
    def render(self, _):
        pass

