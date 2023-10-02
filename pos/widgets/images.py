
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.properties import StringProperty, ListProperty

Builder.load_string('''
<CircleAvatar>:
    RelativeLayout:
        AsyncImage:
            id: proxy
            opacity: 0
            source: root.source
        BoxLayout:
            padding: dp(1.5)
            canvas.before:
                Color:
                    rgba: rgba("#f2f2f2")
                Ellipse:
                    size: self.size[0], self.size[1]
                    pos: self.pos
            Widget:
                canvas.after:
                    Color:
                        rgba: [1,1,1,1]
                    Ellipse:
                        size: self.size[0], self.size[1]
                        pos: self.pos
                        texture: proxy.texture

<AvatarStack>:
    RelativeLayout:
        id: rl
''')
class CircleAvatar(BoxLayout):
    source = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

class AvatarStack(BoxLayout):
    sources = ListProperty([])
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.bind(size=self.update_sizes)
        self.bind(pos=self.update_sizes)

        self._offset = .8

    def update_sizes(self, inst, val):
        for c in self.ids.rl.children:
            c.width = self.height
            c.pos = [self.pos[0]+self.size[0], 0]

    def on_sources(self, inst, sources):
        sx = self.height

        self.ids.rl.clear_widgets()
        for s in sources:
            ca = CircleAvatar()
            ca.size_hint_x = None
            ca.width = sx
            ca.source = s
            ca.pos_hint = {"x": self._offset}

            self._offset -= .1

            self.ids.rl.add_widget(ca)
