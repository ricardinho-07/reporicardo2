from kivy.app import App
from kivy.uix.button import Button
class myapp(App):
    def build(self):
        return Button(text="hello world")
    
if __name__ == "main":
    myapp().run()2