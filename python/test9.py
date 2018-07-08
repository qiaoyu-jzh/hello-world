#使用@property

class Screen():
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width=value

    @property
    def height(self):
        return  self._height

    @height.setter
    def height(self,value):
        self._height=value

    @property
    def resolution(self):
        return self._width*self._height

s=Screen()
s.height=768
s.width=1024
print("resolution = ",s.resolution)