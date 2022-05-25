__version__ = "0.1"

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager

from random import *

class ScreenManager(ScreenManager):
    pass

class TestApp(App):
    def build(self):
        self.screenManager = ScreenManager()
        self.switchTo('korean')
        return self.screenManager

    def switchTo(self, name):
        self.screenManager.current = name
        if name == 'korean':
            self.vocab = choice(vocabs)
            self.screenManager.ids["2"].text = self.vocab[0]
        else:
            self.screenManager.ids["1"].text = self.vocab[1]


with open("main.kv") as f:
    kv = f.read()
    Builder.load_string(kv)

vocabs = []
isFirstLine = True
for line in open("vocabs.csv", encoding='UTF-8'):
    if isFirstLine:
        isFirstLine = False
        continue
    items = line.strip().split(',')
    vocabs.append((items[0], items[1], items[2], items[3]))

TestApp().run()