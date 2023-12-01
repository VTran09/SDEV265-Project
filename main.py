
from os.path import dirname, join

from kivy.garden.iconfonts import register

from app import MainApp

register(
    "FeatherIcons",
    join(dirname(__file__), "assets/fonts/feather/feather.ttf"),
    join(dirname(__file__), "assets/fonts/feather/feather.fontd"),
    )

MainApp().run()
