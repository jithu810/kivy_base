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
from kivymd.uix.button import MDRoundFlatIconButton,MDRectangleFlatButton
from kivymd.app import MDApp
from kivymd.uix.progressbar import MDProgressBar
from kivy.properties import StringProperty

from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.uix.chip import MDChip
from kivymd.uix.filemanager import MDFileManager
from kivy.core.window import Window

from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from kivymd.uix.button import MDRoundFlatIconButton,MDRectangleFlatButton
from . database import *

import os
import sqlite3
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
db_file = os.path.join(BASE_DIR, "db.sqlite3")
conn = sqlite3.connect(db_file, check_same_thread=False)
c = conn.cursor()
c.execute("SELECT * FROM history ORDER BY id DESC")
myresult =c.fetchall()


class Cloud(MDScreen):
    state = StringProperty("stop")

    def __init__(self,**kwargs):
        super(Cloud,self).__init__(**kwargs)
        global table_no,clicked
        self.layout=MDFloatLayout()
        self.add_widget(self.layout)
        self.data_tables = MDDataTable(
            # MDDataTable allows the use of size_hint
            size_hint=(0.98, 0.85),
            pos_hint={'x':.01,'y':.06},
            use_pagination=True,
            check=True,
            column_data=[
                ("name", dp(105)),
                ("date", dp(105)),
                ("time", dp(105))
            ],
            sorted_on="Schedule",
            sorted_order="ASC",
            elevation=2
        )
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)
        check2= ("alert-circle", [1, 0, 0, 1], "Offline")

        
        for x in myresult:
            self.data_tables.row_data.insert(len(self.data_tables.row_data),(x[1],x[2],x[3]))
        self.table_no=len(self.data_tables.row_data)+1
        self.layout.add_widget(self.data_tables)


    def Update(self):
        self.data_tables.row_data.clear()
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        db_file = os.path.join(BASE_DIR, "db.sqlite3")
        conn = sqlite3.connect(db_file, check_same_thread=False)
        c = conn.cursor()
        c.execute("SELECT * FROM history ORDER BY id DESC")
        check=(
                                "checkbox-marked-circle",
                                [39 / 256, 174 / 256, 96 / 256, 1],
                                "Online",
                            )
        myresult =c.fetchall()
        for x in myresult:
            self.data_tables.row_data.insert(len(self.data_tables.row_data),(x[1],x[2],x[3]))

        
        

    
        

    def delete_data(self):
        myquery = {"_id":clicked}
        table.delete_one(myquery)
        print(clicked+str(":is deleted"))

    
    def on_row_press(self, instance_table, instance_row):
        pass

    def on_check_press(self, instance_table, current_row):
        global clicked
        clicked=(current_row[0])
        print(current_row)

    def sort_on_signal(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: l[1][2]
            )
        )

    def sort_on_schedule(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: sum(
                    [int(l[1][-2].split(":")[0])*60,
                    int(l[1][-2].split(":")[1])]
                )
            )
        )

    def sort_on_team(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: l[1][-1]
            )
        )

    

    

        
       

       

        


    


Builder.load_file('cloud.kv')
