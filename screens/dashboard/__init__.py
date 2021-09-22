from logging import RootLogger, root
from kivymd.uix.screen import MDScreen
from kivymd.uix.behaviors import HoverBehavior
from kivymd.theming import ThemableBehavior
from kivymd.uix.button import MDIconButton
from kivy.properties import NumericProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRoundFlatIconButton
from kivymd.app import MDApp

import os
from kivy.uix.popup import Popup
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatIconButton,MDRaisedButton,MDFillRoundFlatButton,MDFlatButton
import csv

class Home(MDScreen):
    def __init__(self,**kwargs):
        super(Home,self).__init__(**kwargs)
        self.layout=MDFloatLayout()
        self.add_widget(self.layout)


    
    


Builder.load_file('dashboard.kv')
