#property学习代码
class Screen(object):
    def __init__(self):
        pass
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width

tanlge = Screen()
tanlge.height = 90
tanlge.width = 60
print(tanlge.resolution)