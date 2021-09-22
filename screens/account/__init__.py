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
from kivymd.uix.button import MDFloatingActionButtonSpeedDial,MDFillRoundFlatButton
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import sqlite3
try:
    conn = sqlite3.connect(r'screens\user\db.sqlite3', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT * FROM userregister")
    myresult =c.fetchall()

    conn2 = sqlite3.connect(r'screens\admin\db.sqlite3', check_same_thread=False)
    c2 = conn2.cursor()
    c2.execute("SELECT * FROM adminregister")
    myresult2 =c2.fetchall()
except :
    print("no tables")

class Account(MDScreen):
    def __init__(self,**kwargs):
        super(Account,self).__init__(**kwargs)
        self.layout=MDFloatLayout()
        self.add_widget(self.layout)

   

    def callback(self, instance):
        if instance.icon == "account":
            MDApp.get_running_app().switch_screen('user')
        if instance.icon == "account-tie":         
            MDApp.get_running_app().switch_screen('admin')

    
      


       

        


    


Builder.load_file('account.kv')
