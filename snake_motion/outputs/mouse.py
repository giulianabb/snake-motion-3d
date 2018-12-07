from pynput import mouse

class LeftClick(Exception): pass
class RightClick(Exception): pass

class Mouse:

    __listener = None
    __on_mouse_click = None

    def on_click(self, x, y, button, pressed):
        if (pressed):
            if button == mouse.Button.left:
                self.__on_mouse_click(isLeft = True)
            elif button == mouse.Button.right:
                self.__on_mouse_click(isLeft = False)

    def __init__(self, on_mouse_click):
        self.__on_mouse_click = on_mouse_click
        self.__listener = mouse.Listener(on_click = self.on_click)
        self.__listener.start()

    def finalize(self):
        self.__listener.stop()
        self.__listener = None
