
from app import App
from kivy.utils import QueryDict, rgba
from kivy.metrics import dp, sp
from kivy.properties import ColorProperty, ListProperty

from .view import MainWindow

class MainApp(App):
    theme = "light"
    color_primary = ColorProperty(rgba("#3B0BFB"))
    color_secondary = ColorProperty(rgba("#65DDB2"))
    color_tertiary = ColorProperty(rgba("#F27373"))
    color_alternate = ColorProperty(rgba("#EFF9FF"))
    color_primary_bg = ColorProperty(rgba("#FFFFFF"))
    color_secondary_bg = ColorProperty(rgba("#EFEFEF"))
    color_primary_text = ColorProperty(rgba("#000000"))
    color_secondary_text = ColorProperty(rgba("#A4A4A4"))

    fonts = QueryDict()
    fonts.size = QueryDict()
    fonts.size.h1 = dp(24)
    fonts.size.h2 = dp(22)
    fonts.size.h3 = dp(18)
    fonts.size.h4 = dp(16)
    fonts.size.h5 = dp(14)
    fonts.size.h6 = dp(12)

    fonts.heading = 'assets/fonts/Inter/Inter-Bold.otf'
    fonts.subheading = 'assets/fonts/Inter/Inter-Regular.otf'
    fonts.body = 'assets/fonts/Inter/Inter-ExtraLight.otf'

    def build(self):
        return MainWindow()

    def toggle_theme(self):
        if self.theme == "dark":
            self.color_primary = ColorProperty(rgba("#4E2FE3"))
            self.color_secondary = ColorProperty(rgba("#3FD0B6"))
            self.color_tertiary = ColorProperty(rgba("#E35588"))
            self.color_alternate = ColorProperty(rgba("#BF2FE3"))
            self.color_primary_bg = ColorProperty(rgba("#33313F"))
            self.color_secondary_bg = ColorProperty(rgba("#3B3947"))
            self.color_primary_text = ColorProperty(rgba("#FFFFFF"))
            self.color_secondary_text = ColorProperty(rgba("#3B3947"))
        else:
            color_primary = ColorProperty(rgba("#3B0BFB"))
            color_secondary = ColorProperty(rgba("#65DDB2"))
            color_tertiary = ColorProperty(rgba("#F27373"))
            color_alternate = ColorProperty(rgba("#EFF9FF"))
            color_primary_bg = ColorProperty(rgba("#FFFFFF"))
            color_secondary_bg = ColorProperty(rgba("#EFEFEF"))
            color_primary_text = ColorProperty(rgba("#000000"))
            color_secondary_text = ColorProperty(rgba("#A4A4A4"))
