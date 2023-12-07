class Colour():
    def rgb_to_scaled(red: int, green: int, blue: int) -> tuple[float, float, float]: # type: ignore
        return (red / 255.0, green / 255.0, blue / 255.0)
    
    def rgba_to_scaled(red: int, green: int, blue: int, alpha: int) -> tuple[float, float, float, float]: # type: ignore
        return (red / 255.0, green / 255.0, blue / 255.0, alpha / 100.0)

    BACKGROUND: tuple[float, float, float] = rgb_to_scaled(62, 139, 175)    # 3E8BAF
    PRIMARY: tuple[float, float, float] = rgb_to_scaled(0, 0, 0)            # 000000
    ACCENT: tuple[float, float, float] = rgb_to_scaled(83, 50, 37)          # 533225
    
    ENABLED: tuple[float, float, float, float] = rgba_to_scaled(200, 200, 200, 100)    # C8C8C8
    DISABLED: tuple[float, float, float, float] = rgba_to_scaled(141, 141, 141, 60)    # 8D8D8D
    
    INVISIBLE: tuple[float, float, float, float] = (0, 0, 0, 0)

class Text():
    XL = '72sp'
    LG = '36sp'
    NM = '24sp'
    SM = '18sp'


class Size():
    WIDTH: int = 800
    HEIGHT: int = 480


class Icons():
    # Default Path for Icons
    PATH: str = './views/icons'

    # Screen Icons
    HOME: str = f'{PATH}/home.png'
    SETTINGS: str = f'{PATH}/settings.png'
    
    # Arrows
    NEXT: str = f'{PATH}/arrow_right.png'
    BACK: str = f'{PATH}/arrow_left.png'

    # Prompts
    CONFIRM: str = f'{PATH}/confirm.png'
    CANCEL: str = f'{PATH}/cancel.png'

    # Interaction
    ADD: str = f'{PATH}/plus.png'
    SOUND_OFF: str = f'{PATH}/sound_off.png'
    DROPDOWN: str = f'{PATH}/dropdown.png'

    # Days
    ROUND_BUTTON_ENABLED: str = f'{PATH}/day_enabled.png'
    ROUND_BUTTON_DISABLED: str = f'{PATH}/day_disabled.png'
