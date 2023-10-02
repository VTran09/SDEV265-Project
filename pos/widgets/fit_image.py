# from kivy.graphics.context_instructions import Color
from kivy.graphics import Color, RoundedRectangle
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.widget import Widget


class FitImage(BoxLayout):
    source = StringProperty("")
    radius = ListProperty([1])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.container = Container()
        
        Clock.schedule_once(self._late_init)

    def _late_init(self, *args):
        self.add_widget(self.container)
    
    def on_source(self, inst, source):
        self.container.source = source
    
    def on_radius(self, inst, val):
        self.container.radius = val


class Container(Widget):
    source = StringProperty("")
    radius = ListProperty([1])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.image = AsyncImage()
        with self.canvas:
            self.canvas.clear()
            Color(1, 1, 1)
            self.draw = RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius)
        
        self.bind(size=self.adjust_size)
        self.bind(pos=self.adjust_size)


    def on_source(self, inst, source):
        self.image.source = source
        self.adjust_size()

    def on_radius(self, inst, radius):
        self.draw.radius = radius

    def adjust_size(self, *args):
        (par_x, par_y) = self.parent.size

        if par_x == 0 or par_y == 0:
            with self.canvas:
                self.canvas.clear()
            return

        par_scale = par_x / par_y

        (img_x, img_y) = self.image.texture.size
        img_scale = img_x / img_y

        if par_scale > img_scale:
            (img_x_new, img_y_new) = (img_x, img_x / par_scale)
        else:
            (img_x_new, img_y_new) = (img_y * par_scale, img_y)

        crop_pos_x = (img_x - img_x_new) / 2
        crop_pos_y = (img_y - img_y_new) / 2

        subtexture = self.image.texture.get_region(crop_pos_x, crop_pos_y, img_x_new, img_y_new)

        self.draw.texture = subtexture
        self.draw.size = (par_x, par_y)

