import os # Differentiate between Linux and Windows

# Kivy
import kivy
kivy.require('2.0.0')
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.clock import mainthread
from kivymd.app import MDApp

# Self Made
from model.managers import GenericManager
from views import Screens
from theme import Size


def kivy_setup():
    # Development Settings
    if os.name == 'posix': # Linux
        Window.fullscreen = 'auto'
        Window.always_on_top = True
        Window.show_cursor = False
    else: # Non Linux
        # Immitate the Look and Feel of the Hardware Device
        Window.size = (Size.WIDTH, Size.HEIGHT)
        Window.borderless = True


class MainApp(MDApp):
    def build(self):
        # Colour Palettes
        self.theme_cls.primary_palette = 'LightBlue'
        self.theme_cls.accent_palette = 'Brown'

        # Screenmanager
        self.screen_manager = ScreenManager()

        # Transitions
        self.screen_manager.transition.duration = .15

        # Setup of Screens
        for screen in Screens:
            self.screen_manager.add_widget(screen())

        # Interrupt Callback
        GenericManager().callbacks\
            .registerCallback('trigger_alarm', self.go_to_wakeup)

        return self.screen_manager


    # Forces function to run
    # on Kivy Main Thread
    @mainthread
    def go_to_wakeup(self):
        self.screen_manager.current = 'wakeup'


if __name__ == '__main__': # Startup
    kivy_setup()
    MainApp().run()
