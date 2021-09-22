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
import csv



class Table(MDScreen):
    def __init__(self,**kwargs):
        super(Table,self).__init__(**kwargs)
        self.layout=MDFloatLayout()
        self.add_widget(self.layout)
        
        
        


    
        
        

    
        

    
               
        
Builder.load_file('table.kv')
  
 


    


