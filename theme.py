class Colour():
    def rgb_to_scaled(red: int, green: int, blue: int):
        return (red / 255.0, green / 255.0, blue / 255.0)
    
    def rgba_to_scaled(red: int, green: int, blue: int, alpha: int):
        return (red / 255.0, green / 255.0, blue / 255.0, alpha / 100.0)

    BACKGROUND = rgb_to_scaled(62, 139, 175)    # 3E8BAF
    PRIMARY = rgb_to_scaled(0, 0, 0)            # 000000
    ACCENT = rgb_to_scaled(83, 50, 37)          # 533225
    
    ENABLED = rgba_to_scaled(200, 200, 200, 100)    # C8C8C8
    DISABLED = rgba_to_scaled(141, 141, 141, 60)    # 8D8D8D
    
    INVISIBLE = (0, 0, 0, 0)

class Text():
    XL = '72sp'
    LG = '36sp'
    NM = '24sp'
    SM = '18sp'


class Size():
    WIDTH = 800
    HEIGHT = 480


class Icons():
    PATH = './views/icons'
    HOME = f'{PATH}/home.png'
    BACK = f'{PATH}/back_arrow.png'
    SETTINGS = f'{PATH}/settings.png'

    CONFIRM = f'{PATH}/plus.png'
    CANCEL = f'{PATH}/cancel.png'

    PLUS = f'{PATH}/plus.png'
    SOUND_OFF = f'{PATH}/sound_off.png'

    ROUND_BUTTON_ENABLED = f'{PATH}/day_enabled.png'
    ROUND_BUTTON_DISABLED = f'{PATH}/day_disabled.png'
