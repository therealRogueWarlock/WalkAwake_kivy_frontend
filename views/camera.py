from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from threading import Thread
import time
from theme import Icons
from WalkAwake.CameraModule import ComputerVisionManager


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
        self.targets = ["Sink", "Toilet", "Toothbrush", "Refrigerator"]
        self.target = None

        # testing
        self.img_counter_start = 97
        self.img_counter = self.img_counter_start
        self.img_counter_max = 303

    def on_enter(self):
        self.target = self.targets[1]
        self.ids.TargetText.text = "Target: " + self.target
        # Start Camera Scheduler
        # self.computer_vision_manager.Start(self.feed_path)

    def on_leave(self):
        # Stop Camera Scheduler
        # self.computer_vision_manager.Stop()
        self.loop.cancel()

    def verify_image(self):
        start = time.time()
        result = self.computer_vision_manager.VerifyImage(self.target, self.capture_path)
        self.ids.ProcessingSpinner.active = False
        print("Result from verify " + str(result))
        print("Verify image time : " + str(time.time() - start))
        if result == 1:
            self.ids.TargetText.text = f"No {self.target} found, try again !"
        else:
            self.ids.TargetText.text = f"{self.target} found!!!"
            Clock.schedule_once(lambda dt: self.go_home(), 1)

    def go_home(self):
        self.manager.current = "home"

    def capture(self):
        self.ids.ProcessingSpinner.active = True
        self.ids.ImageView.source = self.capture_path + "/image_capture.jpg"
        self.loop = Clock.schedule_interval(lambda dt: self.update_image_view(), 1)
        start = time.time()
        Clock.schedule_once(lambda dt: self.verify_image(), 0)
        self.ids.TargetText.text = "!Target: " + self.target
        print("after thread time : " + str(time.time() - start))

    def update_image_view(self):
        self.ids.ImageView.reload()
