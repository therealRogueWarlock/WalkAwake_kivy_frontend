from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from WalkAwake import ComputerVisionManager

# camera
class Camera(Screen):
    name = 'camera'

    def __init__(self, **kw):
        super().__init__(**kw)
        self.computer_vision_manager = ComputerVisionManager()
        self.feed_path = "/home/sander/camera_feed"
        self.capture_path = "/home/sander/camera_capture"
        self.FPS = 15
        self.loop = None
        # testing
        self.img_counter_start = 97
        self.img_counter = self.img_counter_start
        self.img_counter_max = 303

    def on_pre_enter(self):
        # Start Camera Scheduler
        #self.computer_vision_manager.Start(self.feed_path)
        self.loop = Clock.schedule_interval(lambda dt: self.update_image_view(), 1/self.FPS)

    def on_pre_leave(self):
        # Stop Camera Scheduler
        #self.computer_vision_manager.Stop()
        pass

    def capture(self):
        # call model layer to capture image
        self.loop.cancel()
        self.computer_vision_manager.VerifyImage("sink", self.capture_path)

    def update_image_view(self):
        image_view = self.ids.imageView
        # testing
        self.img_counter += 1
        image_view.source = self.feed_path + "/image_capture.jpg"
        if self.img_counter == self.img_counter_max:
            self.img_counter = self.img_counter_start
