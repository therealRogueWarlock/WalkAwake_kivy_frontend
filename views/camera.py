from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from threading import Thread
import time
from theme import Icons
# from WalkAwake.CameraModule import ComputerVisionManager


# camera
class Camera(Screen):
    name = 'camera'

    capture_path: str
    FPS: int
    loop: object
    targets: list[str]
    target: str
    is_capturing: bool

    def __init__(self, **kw):
        super().__init__(**kw)
        # self.computer_vision_manager = ComputerVisionManager()

        self.capture_path = "data/"
        self.FPS = 15

        self.targets = ["Sink", "Toilet", "Toothbrush", "Refrigerator"]
        self.is_capturing = False

    def on_enter(self):
        self.target = self.targets[1]
        self.ids.TargetText.text = "Target: " + self.target

    def on_leave(self):

        self.loop.cancel() # type: ignore

    def verify_image(self):
        start = time.time() # TESTING

        result = ''#self.computer_vision_manager.VerifyImage(self.target)
        self.ids.ProcessingSpinner.active = False

        print("Result from verify " + str(result))
        print("Verify image time : " + str(time.time() - start))

        self.is_capturing = False
        if result == 1:
            self.ids.TargetText.text = f"No {self.target} found, try again !"
        else:
            self.ids.TargetText.text = f"{self.target} found, have a grate day!"
            Clock.schedule_once(lambda dt: self.go_home(), 3)

    def go_home(self):
        self.manager.current = "home"

    def capture(self):
        if self.is_capturing:
            return
        
        # Ensure another picture isn't taken before processing the first
        self.is_capturing = True

        # Set the image path
        self.ids.ImageView.source = self.capture_path + "/image_capture.jpg"

        # Start an Update Loop for Background Image
        self.loop = Clock.schedule_interval(lambda dt: self.update_image_view(), 1)

        # Testing / Debugging
        start = time.time()

        # Call Verify Image once without stealing focus
        Clock.schedule_once(lambda dt: self.verify_image(), 0)

        # Visual Updates
        self.ids.TargetText.text = "!Target: " + self.target
        self.ids.ProcessingSpinner.active = True

        # Testing / Debugging
        print("after thread time : " + str(time.time() - start))


    def update_image_view(self):
        self.ids.ImageView.reload()
