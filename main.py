from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import pandas as pd
import numpy as np

class Container(BoxLayout):
    dataset = pd.read_csv('dataset.csv')
    def my_number(self):
        operation = self.ttext_input.text
        operation = operation.split(sep=' ')
        operation = int(operation[0]) + int(operation[1])
        self.ttext_output.text = str(operation)

    pass


class MyApp(App):
    def build(self):

        return Container()

if __name__ == "__main__":
    MyApp().run()