from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty, ColorProperty, ObjectProperty, ListProperty, NumericProperty
from kivy.clock import Clock
from kivy.metrics import dp, sp
from kivy.utils import rgba

from kivy.graphics import Color, Ellipse, Line, Rectangle, RoundedRectangle

Builder.load_string("""
#: import SoftBox widgets.gradient.SoftBox
#: import Text widgets.labels.Text
#: import icon kivy.garden.iconfonts.icon
#: import FlatButton widgets.buttons.FlatButton

<ConfirmDialog>:
    background: ""
    background_color: [0,0,0, .3]
    auto_dismiss: False
    BoxLayout:
        size_hint: [None, .4]
        width: self.height
        orientation: "vertical"
        canvas.before:
            Color:
                rgba: [1,1,1,1]
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [dp(12)]
        SoftBox:
            size_hint_y: None
            height: dp(42)
            bcolor: [root.primary_color, root.primary_color]
            padding: [dp(14), dp(2)]
            radius: [dp(12), dp(12), 0, 0]
            Text:
                text: root.title
                font_name: app.fonts.heading
                halign: "center"
                color: app.colors.secondary
        AnchorLayout:
            Label:
                text: root.text
                halign: "center"
                valign: "middle"
                color: root.primary_color
                size_hint_y: None
                text_size: [self.parent.width*.9, None]
                size: self.texture_size
                # height: dp(24)
        BoxLayout:
            size_hint_y: None
            height: dp(54)
            padding: [dp(8), dp(10)]
            Widget:
                size_hint_x: .1
            FlatButton:
                text: "CANCEL"
                color: app.colors.danger
                size_hint_x: .4
                on_release: root.dismiss()
            SoftButton:
                text: "CONTINUE"
                color: root.primary_color
                font_size: sp(14)
                bcolor: [rgba("#f5f5f5"), rgba("#f5f5f5")]
                size_hint_x: .4
                on_release:
                    root.dismiss() 
                    root.callback()
            Widget:
                size_hint_x: .1

<CircularProgressIndicator>:
    AnchorLayout:
        id: spinner
<Indicator>
    size_hint: [None, None]
    size: [dp(24), dp(24)]
    canvas.before:
        PushMatrix
        Rotate:
            angle: self.angle
            origin: self.center
    canvas.after:
        PopMatrix

<RefreshLoader>:
    background: ""
    background_color: [0,0,0, .3]
    auto_dismiss: False
    AnchorLayout:
        anchor_y: "bottom"
        padding: dp(12)
        BoxLayout:
            size_hint_y: None
            height: dp(42)
            padding: [dp(12), dp(2)]
            canvas.before:
                Color:
                    rgba: root.bcolor
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [self.height*.1]
            Label:
                text: root.text
                text_size: self.size
                valign: "middle"
                font_size: sp(14)
                color: rgba("#a1a1a1")
            AnchorLayout:
                size_hint_x: None
                width: dp(24)
                CircularProgressIndicator:
                    id: prog
                    size_hint: [None, None]
                    size: [dp(24), dp(24)]

<AlertLoader>:
    background: ""
    background_color: [0,0,0, .3]
    auto_dismiss: True
    AnchorLayout:
        anchor_y: "bottom"
        padding: [dp(12), dp(6)]
        BoxLayout:
            size_hint_y: None
            height: dp(42)
            padding: [dp(12), dp(2)]
            canvas.before:
                Color:
                    rgba: root.bcolor
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [self.height*.1]
            Label:
                text: root.text
                text_size: self.size
                font_size: sp(14)
                valign: "middle"
                color: rgba("#a1a1a1")
""")

class RefreshLoader(ModalView):
    text = StringProperty("")
    bcolor = ColorProperty([1,1,1,1])
    def __init__(self, **kw):
        super().__init__(**kw)

class AlertLoader(ModalView):
    text = StringProperty("")
    bcolor = ColorProperty([1,1,1,1])
    def __init__(self, **kw):
        super().__init__(**kw)
        self.bind(on_open=Clock.schedule_once(self.dismiss, 3))

class ConfirmDialog(ModalView):
    title = StringProperty("")
    text = StringProperty("")
    callback = ObjectProperty(print)
    primary_color = ColorProperty(rgba("#528bff"))
    def __init__(self, **kw):
        super().__init__(**kw)

class CircularProgressIndicator(RelativeLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.size_hint = [None, None]
        self.width = dp(24)
        self.height = dp(24)
        Clock.schedule_once(self.render, .2)

    def render(self, _):
        self.ids.spinner.add_widget(Indicator())

class Indicator(Widget):
    line_color = ColorProperty(rgba("#0052D4"))
    bcolor = ColorProperty(rgba("#f2f2f2"))
    angle = NumericProperty(0)
    def __init__(self, **kw):
        super().__init__(**kw)
        self.size_hint = [None, None]
        self.__current_end = 0

        with self.canvas.before:
            self.paint0 = Color(rgba=self.bcolor)
            self.draw0 = Line(
                width = dp(1),
                ellipse = [self.x, self.y, self.width, self.height]
                )

            self.paint1 = Color(rgba=self.line_color)
            self.draw1 = Line(
                width = dp(1.5),
                ellipse = [self.x, self.y, self.width, self.height, 0, self.__current_end]
                )

        self.bind(pos=self.update)
        self.bind(size=self.update)
        Clock.schedule_interval(self.roll, .1)

    def roll(self, dtx):
        nu_angle = 0
        next_end = self.__current_end + 20
        if self.angle != 360:
            nu_angle = self.angle + 50
        
        if next_end > 360:
            next_end = 0

        self.angle = nu_angle
        self.__current_end = next_end
        self.draw1.ellipse = [self.x, self.y, self.width, self.height, 0, self.__current_end]


    def update(self, *args):
        self.draw0.ellipse = [self.x, self.y, self.width, self.height]
        self.draw1.ellipse = [self.x, self.y, self.width, self.height, 0, 120]


