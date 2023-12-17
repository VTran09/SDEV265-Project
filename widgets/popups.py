from kivy.uix.modalview import ModalView
from kivy.properties import StringProperty, ObjectProperty, ColorProperty
from kivy.clock import Clock
from kivy.lang import Builder

Builder.load_string("""
<ConfirmDialog>:
    background: ""
    background_color: [0, 0, 0, .1]
    BackBox:
        orientation: 'vertical'
        spacing: dp(12)
        padding: dp(14)
        bcolor: app.color_primary_bg
        radius: [self.height*.08]
        size_hint: [None, .7]
        width: self.height
        BoxLayout:
            size_hint_y: .6
            orientation: 'vertical'
            Text:
                text: root.title
                halign: "center"
                font_name: app.fonts.styled
                font_size: app.fonts.size.extra
                color: app.color_primary_text
            Text:
                text: root.subtitle
                halign: "center"
                font_size: app.fonts.size.h2
                color: app.color_primary_text
        AnchorLayout:
            BoxLayout:
                size_hint_y: .4
                spacing: dp(12)
                size_hint_y: None
                height: dp(64)
                FlatButton:
                    text: root.textCancel
                    font_size: app.fonts.size.h2
                    color: root.cancelColor
                    on_release: root.cancel()
                RoundedButton:
                    text: root.textConfirm
                    font_size: app.fonts.size.h2
                    bcolor: root.confirmColor
                    color: rgba('#ffffff')
                    radius: [self.height*.1]
                    on_release: root.complete()                  
""")

class ConfirmDialog(ModalView):
    title = StringProperty("")
    subtitle = StringProperty("")
    textConfirm = StringProperty("")
    textCancel = StringProperty("")
    cancelCallback = ObjectProperty(allownone=True)
    confirmCallback = ObjectProperty(allownone=True)
    confirmColor = ColorProperty([1,1,1,1])
    cancelColor = ColorProperty([1,1,1,1])
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
        
    def render(self, _):
        pass
    
    def cancel(self):
        self.dismiss()
        
        if self.cancelCallback:
            self.cancelCallback(self)
        
    def complete(self):
        self.dismiss()

        if self.confirmCallback:
            self.confirmCallback(self)