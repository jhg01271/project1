from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Interface(FloatLayout):
    def display_information(self):
        data=self.ids.textInput.text
        self.ids.label.text=data

class ProjectApp(App):
    pass

ProjectApp().run()