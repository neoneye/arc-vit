import unittest
from color_xy import color_to_xy, xy_to_color

def color_to_xy_wrap(color: int, color_count: int, offset: float) -> (int, int):
    (x, y) = color_to_xy(color, color_count, offset)
    xi = int(x * 1000.0)
    yi = int(y * 1000.0)
    return (xi, yi)

def xy_to_color_wrap(xy: (int, int), color_count: int, offset: float) -> int:
    (x, y) = xy
    xf = float(x) / 1000.0
    yf = float(y) / 1000.0
    return xy_to_color((xf, yf), color_count, offset)

class TestColorXY(unittest.TestCase):
    def test_color_to_xy_without_offset(self):
        offset = 0.0
        # 0 degrees
        self.assertEqual(color_to_xy_wrap(0, 4, offset), (1000, 0))
        # 90 degrees
        self.assertEqual(color_to_xy_wrap(1, 4, offset), (0, 1000))
        # 180 degrees
        self.assertEqual(color_to_xy_wrap(2, 4, offset), (-1000, 0))
        # 270 degrees
        self.assertEqual(color_to_xy_wrap(3, 4, offset), (0, -1000))
        # 45 degrees
        self.assertEqual(color_to_xy_wrap(1, 8, offset), (707, 707))

    def test_color_to_xy_with_offset(self):
        offset = 0.5 # same as rotating by 180 degrees
        # 0 degrees
        self.assertEqual(color_to_xy_wrap(0, 4, offset), (-1000, 0))
        # 90 degrees
        self.assertEqual(color_to_xy_wrap(1, 4, offset), (0, -1000))
        # 180 degrees
        self.assertEqual(color_to_xy_wrap(2, 4, offset), (1000, 0))
        # 270 degrees
        self.assertEqual(color_to_xy_wrap(3, 4, offset), (0, 1000))

    def test_xy_to_color_without_offset(self):
        offset = 0.0
        # 0 degrees
        self.assertEqual(xy_to_color_wrap((1000, 0), 4, offset), 0)
        # 90 degrees
        self.assertEqual(xy_to_color_wrap((0, 1000), 4, offset), 1)
        # 180 degrees
        self.assertEqual(xy_to_color_wrap((-1000, 0), 4, offset), 2)
        # 270 degrees
        self.assertEqual(xy_to_color_wrap((0, -1000), 4, offset), 3)
        # 45 degrees
        self.assertEqual(xy_to_color_wrap((707, 707), 8, offset), 1)

    def test_xy_to_color_with_offset(self):
        offset = 0.5 # same as rotating by 180 degrees
        # 0 degrees
        self.assertEqual(xy_to_color_wrap((-1000, 0), 4, offset), 0)
        # 90 degrees
        self.assertEqual(xy_to_color_wrap((0, -1000), 4, offset), 1)
        # 180 degrees
        self.assertEqual(xy_to_color_wrap((1000, 0), 4, offset), 2)
        # 270 degrees
        self.assertEqual(xy_to_color_wrap((0, 1000), 4, offset), 3)

if __name__ == '__main__':
    unittest.main()
