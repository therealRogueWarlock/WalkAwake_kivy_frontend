import os
import kivy
from views import Screens
from theme import Size, Colours

kivy.require('2.0.0')
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from kivymd.app import MDApp

def kivy_setup():
    # Development stuff
    if os.name == 'posix': # Linux
        Window.fullscreen = 'auto'
        Window.always_on_top = True
        Window.show_cursor = False
        print(kivy.Config.set('input', 'mouse', ''))
    else: # Not Linux
        Window.size = (Size.WIDTH, Size.HEIGHT)
        Window.borderless = True

    # Window.clearcolor = Colour.BACKGROUND


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'LightBlue'
        self.theme_cls.accent_palette = 'Brown'

        # Screenmanager
        screen_manager = ScreenManager()
        screen_manager.transition.duration = .15
        for screen in Screens:
            screen_manager.add_widget(screen())
        return screen_manager


if __name__ == '__main__':
    kivy_setup()
    MainApp().run()
