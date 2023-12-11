from kivy.uix.screenmanager import Screen
from kivy.clock import Clock


# camera
class Camera(Screen):
    name = 'camera'

    def __init__(self, **kw):
        super().__init__(**kw)

        self.FPS = 15
        # testing
        self.img_counter_start = 97
        self.img_counter = self.img_counter_start
        self.img_counter_max = 303

    def on_pre_enter(self):
        # Start Camera Scheduler
        pass
        # Clock.schedule_interval(lambda dt: self.update_image_view(), 1/self.FPS)

    def on_pre_leave(self):
        # Stop Camera Scheduler
        pass

    def capture(self):
        # call model layer to capture image
        pass

    def update_image_view(self):
        image_view = self.ids.imageView
        # testing
        self.img_counter += 1
        image_view.source = f"C:/Users/sande/Pictures/Screenshots/Screenshot ({self.img_counter}).png"
        if self.img_counter == self.img_counter_max:
            self.img_counter = self.img_counter_start
