from kivy.config import Config
Config.set("graphics", "width", "900")
Config.set("graphics", "height", "500")
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MainScreen(Widget):
    ...
class NganyaApp(App):
    def build(self):
        return MainScreen()

NganyaApp().run()
