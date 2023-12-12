from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from model.managers import GenericManager
from WalkAwake.CameraModule import ComputerVisionManager


class Camera(Screen):
    name = 'camera'

    # Live Feed - Not Yet Implemented
    FPS: int
    
    # Capture Image
    capture_path: str
    target: str
    is_capturing: bool
    loop: object

    # Verify Image
    targets: list[str]
    computer_vision_manager: ComputerVisionManager

    def __init__(self, **kw):
        super().__init__(**kw)
        self.computer_vision_manager = ComputerVisionManager()

        self.FPS = 15 # Framerate for Live Feed

        self.capture_path = 'data/' # Location to store image

        # To be moved to a config file
        self.targets = ['Sink', 'Toilet', 'Toothbrush', 'Refrigerator']

        self.is_capturing = False

    def on_enter(self):
        self.target = self.targets[1] # Add Random Index
        self.ids.TargetText.text = f'Target: {self.target}'

    def on_leave(self):
        self.loop.cancel()  # type: ignore

    def verify_image(self):
        # Verify Image through Backend
        result = self.computer_vision_manager.VerifyImage(self.target)

        # Hide Spinner
        self.ids.ProcessingSpinner.active = False

        self.is_capturing = False

        # Show User whether the Image was correct
        if result == 1: # 1 -> Error
            self.ids.TargetText.text = f'No {self.target} found, try again!'
        else: # 0 -> Alles Gut
            self.ids.TargetText.text = f'{self.target} found, have a great day!'
            
            # Stop the Alarm
            GenericManager().alarms.stop_alarm()

            # Navigate to Home after a short delay
            Clock.schedule_once(lambda dt: self.go_home(), 3)

    def go_home(self):
        self.manager.current = 'home'

    def capture(self) -> None:
        if self.is_capturing:
            # Blocks accidental multi-tapping
            return None
        
        # Ensure another picture isn't taken before processing the first
        self.is_capturing = True

        # Set the image path
        self.ids.ImageView.source = f'{self.capture_path}/image_capture.jpg'

        # Start an Update Loop for Background Image
        self.loop = Clock.schedule_interval(lambda dt: self.update_image_view(), 1)

        # Call Verify Image once without stealing focus
        Clock.schedule_once(lambda dt: self.verify_image(), 0)

        # Visual Updates
        self.ids.ProcessingSpinner.active = True

    def update_image_view(self):
        self.ids.ImageView.reload()
