import os
import kivy
from views import Screens
from theme import Size

kivy.require('1.0.7')
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.app import App

from kivy.core.window import Window

if os.name == 'posix':
    Window.fullscreen = 'auto'
    Window.always_on_top = True
    Window.show_cursor = False
else:
    Window.size = (Size.WIDTH, Size.HEIGHT)
    Window.borderless = True


class MainApp(App):

    def build(self):
        screen_manager = ScreenManager(transition=FadeTransition())
        for screen in Screens:
            screen_manager.add_widget(screen())
        return screen_manager


if __name__ == '__main__':
    MainApp().run()
