import kivy
from views import Screens

kivy.require('1.0.7')
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App

from kivy.core.window import Window

Window.fullscreen = true
Window.always_on_top = true
Window.show_cursor = false

class MainApp(App):

    def build(self):
        screen_manager = ScreenManager()
        for screen in Screens:
            screen_manager.add_widget(screen())
        return screen_manager


if __name__ == '__main__':
    MainApp().run()

