class Pixel:
    def __init__(self, r=0, g=0, b=0, x=0, y=0):
        self._r = r
        self._g = g
        self._b = b
        self._x = x
        self._y = y

    def set_coords(self, x, y):
        self._x = x
        self._y = y
    def set_grayscale(self):
        gray_value = int((self._r + self._g + self._b) / 3)
        self._r = gray_value
        self._g = gray_value
        self._b = gray_value
    def print_pixel_info(self):
        if [self._r, self._g, self._b].count(0) == 2 and max(self._r, self._g, self._b) > 50:
            if max(self._r, self._g, self._b) == self._r:
                name = "Red"
            elif max(self._r, self._g, self._b) == self._g:
                name = "Green"
            else:
                name = "Blue"
            print("x:" , self._x, "y:", self._y, "Color:(", self._r,",", self._g, ",", self._b, ")" + " " + name)
        else:
            print("x:" , self._x, "y:", self._y, "Color:(", self._r,",", self._g, ",", self._b, ")")
def main():
    p1 = Pixel(250, 0, 0, 5, 6)
    p1.print_pixel_info()
    p1.set_grayscale()
    p1.print_pixel_info()

if __name__ == "__main__":
    main()
