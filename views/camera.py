from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
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
        self.targets = ["sink", "toilet", "toothbrush", "refrigerator"]
        self.target = None
        # testing
        self.img_counter_start = 97
        self.img_counter = self.img_counter_start
        self.img_counter_max = 303

    def on_pre_enter(self):
        self.target = self.targets[1]
        self.ids.TargetText.text = "Target " + self.target
        # Start Camera Scheduler
        self.ids.ImageView.source = self.capture_path + "/image_capture.jpg"
        #self.computer_vision_manager.Start(self.feed_path)
        #self.loop = Clock.schedule_interval(lambda dt: self.update_image_view(), 1/self.FPS)

    def on_pre_leave(self):
        # Stop Camera Scheduler
        #self.computer_vision_manager.Stop()
        pass

    def capture(self):
        # call model layer to capture image
        #self.loop.cancel()
        result = self.computer_vision_manager.VerifyImage(self.target, self.capture_path)
        print("Result from verify " + str(result))

        self.ids.ImageView.source = Icons.ADD
        self.ids.ImageView.source = self.capture_path + "/image_capture.jpg"

    def update_image_view(self):
        pass
