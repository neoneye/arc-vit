import math

def angle_to_xy(angle: float, offset: float) -> (float, float):
    """Convert from radians to obfuscated (x, y) tupple.

    The `angle` must be in the range [0.0, 1.0].
    
    The `offset` must be in the range [0.0, 1.0].
    Provide an offset to obfuscate by rotating. offset=0 is no obfuscation.

    The returned values are in the range [0.0, 1.0].
    """
    
    radians = (angle + offset) % 1.0
    x = math.cos(radians * math.tau)
    y = math.sin(radians * math.tau)
    return (x, y)

def color_to_xy(color: int, color_count: int, offset: float) -> (float, float):
    """Convert from color value to obfuscated (x, y) tupple.

    The `color` must be in the range [0, color_count-1].
    
    The `offset` must be in the range [0.0, 1.0].
    Provide an offset to obfuscate. offset=0 is no obfuscation.

    The returned values are in the range [0.0, 1.0].
    """

    angle = color / float(color_count)
    return angle_to_xy(angle, offset)

def xy_to_color(xy: (float, float), color_count: int, offset: float) -> int:
    """Convert from obfuscated (x, y) tupple to deobfuscated color value.

    The `xy` tupple must be in the range [-1.0, 1.0].
    
    The `offset` must be in the range [0.0, 1.0].
    Provide an offset to deobfuscate. offset=0 is no deobfuscation.
    
    The `color_count` is the number of colors. typical 10.

    The returned value is in the range [0, color_count - 1].
    """
    
    (x, y) = xy
    angle = ((math.atan2(y, x) / math.tau) - offset) % 1.0
    value = math.floor(angle * color_count)
    return int(value)
