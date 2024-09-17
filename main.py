from kivy.app import App
from kivy.uix.label import Label

class MyFirstApp(App):
    def build(self):
        # This method is called when the app is built
        return Label(text="Hello, World!")

# Run the app
if __name__ == "__main__":
    MyFirstApp().run()
