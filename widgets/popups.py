from kivy.uix.modalview import ModalView
from kivy.properties import StringProperty, ObjectProperty

class DeleteConfirm(ModalView):
    title = StringProperty("")
    subtitle = StringProperty("")
    texConfirm = StringProperty("")
    textCancel = StringProperty("")
    cancelCallback = ObjectProperty(allownone=True)
    confirmCallback = ObjectProperty(allownone=True)
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
        
    def render(self, _):
        pass
        
    def complete(self):
        self.dismiss()

        if self.confirmCallback:
            self.confirmCallback(self)