import hashlib
from datetime import datetime
from kivy.app import App
from threading import Thread
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
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
    
    def add_new(self): 
        md=ModUser()
        md.callback = self.add_user
        md.open()    

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

def add_user(self, mv):
        fname = mv.ids.fname
        lname = mv.ids.lname
        uname = mv.ids.uname
        pwd = mv.ids.pwd
        cpwd = mv.ids.cpwd
        #Check if inputs are not empty
        if len(fname.text.strip()) < 3:
            # inform user first name is invalid
            return
        _pwd = pwd.text.strip()
        upass = hashlib.sha256(_pwd.encode).hexdigest()
        now = datetime.now()
        _now = datetime.strftime(now, '%Y/%m/%d %H:%M')
        user={
                "firstName": fname.text.strip(),
                "lastName": lname.text.strip(),
                "username": uname.text.strip(),
                "password": upass,
                "created": _now,
                "signedIn": "12/15/2023 11:47:10 AM"
            }
        self.set_users([user])

    def update_user(self,user):
        mv = ModUser()
        mv.first_name = user.first_name
        mv.last_name = user.last_name
        mv. username = user.username
        mv.callback = self.
        
        mv.open()
    
    def set_update(self, mv)
        print("Updating...")

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
            ut.callback = self.delete_user
            ut.bind(on_release=self.update_user)

            grid.add_widget(ut)


    def delete_user(self, user):
        dc = DeleteConfirm()
        dc.open()

class UserTile(ButtonBehavior, BoxLayout):
    first_name = StringProperty("")
    last_name = StringProperty("")
    username = StringProperty("")
    password = StringProperty("")
    created = StringProperty("")
    last_login = StringProperty("")
    callback = ObjectProperty(allownone=None)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
        
    def render(self, _):
        pass
    
    def delete_user(self):
        if self.callback:
            self.callback(self)

class DeleteConfirm(ModalView):
    callback = ObjectProperty(allownone=True)
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
        
    def render(self, _):
        pass
        
    def complete(self):
        self.dismiss()
        
        if self.callback:
            self.callback(self)
 

class ModUser(ModalView):
    first_name = StringProperty("")
    last_name = StringProperty("")
    username = StringProperty("")
    created = StringProperty("")
    last_login = StringProperty("")
    callback = ObjectProperty(allownone=True)
 
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
        
    def render(self, _):
        pass

    def on_first_name(self, inst, fname)
        self.ids.fname.text = fname
        self.ids.title.text = "Update User"
        self.ids.btn_confirm.text = "Update User"
        self.ids.subtitle.text = "Enter your details below to update user"
    
    def on_last_name(self, inst, lname)
        self.ids.lname.text = lname
    
    def on_username(self, inst, uname)
        self.ids.uname.text = uname