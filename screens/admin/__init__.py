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
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from . database import *
import bcrypt

class Admin(MDScreen):
    def __init__(self,**kwargs):
        super(Admin,self).__init__(**kwargs)
        self.layout=MDFloatLayout()
        self.add_widget(self.layout)

    def Clean(self):
        self.ids.usename.text=""
        self.ids.email.text=""
        self.ids.password.text=""
        self.ids.password2.text=""

    def submit(self):
        name=self.ids.usename.text
        email=self.ids.email.text
        password=self.ids.password.text
        password2=self.ids.password2.text
        if name!="" and password!="":
            if password==password2:
                password = bytes(password, 'utf-8')
                password = bcrypt.hashpw(password, bcrypt.gensalt(14))
                conn = sqlite3.connect(r'screens\admin\db.sqlite3', check_same_thread=False)
                c = conn.cursor()
                sql = 'SELECT * FROM adminregister WHERE name=?'
                num=c.execute(sql, (name,))
                conn.commit()
                myresult =c.fetchall()
                if (len(myresult)) == 0:
                    c.execute("""INSERT INTO adminregister (name, email,password) values (?,?,?)""",(name,email,password))
                    conn.commit()
                    self.ids.usename.text=""
                    self.ids.email.text=""
                    self.ids.password.text=""
                    self.ids.password2.text=""
                    new=('created new admin: '+str(name))
                    MDApp.get_running_app().Message(new)
                else:
                    self.ids.usename.text=""
                    self.ids.email.text=""
                    self.ids.password.text=""
                    self.ids.password2.text=""
                    MDApp.get_running_app().Message('admin already exists') 
            else:
                MDApp.get_running_app().Message('password does not match')    
        else:
            MDApp.get_running_app().Message('invalid Please try again')


    def display_name(self,name):
        c=MDApp.get_running_app().Admindata()
        sql = 'SELECT * FROM adminregister WHERE name=?'
        c.execute(sql, (name,))
        conn.commit()
        myresult =c.fetchall()
        for i in myresult:
            self.ids.usename.text=i[0]
            self.ids.email.text=i[1]

    def Updateprofile(self):
        
        name=self.ids.usename.text
        email=self.ids.email.text
        password=self.ids.password.text
        password2=self.ids.password2.text
        if name!="" and password!="":
            if password==password2:
                c=MDApp.get_running_app().Admindata()
                conn.execute('''UPDATE adminregister SET name = ? ,email = ? ,password = ? WHERE name = ?''', (name,email,password,name))            
                conn.commit()
                self.ids.usename.text=""
                self.ids.email.text=""
                self.ids.password.text=""
                self.ids.password2.text="" 
                MDApp.get_running_app().Message('updated successfully')
                MDApp.get_running_app().switch_screen('profile')

            else:
                MDApp.get_running_app().Message('password does not match')    
        else:
            MDApp.get_running_app().Message('invalid Please try again')





def hash_password(password, version=1, salt=None):
    if version == 1:
        if salt == None:
            salt = uuid.uuid4().hex[:16]
        hashed = salt + hashlib.sha1( salt + password).hexdigest()
        # generated hash is 56 chars long
        return hashed
    # incorrect version ?
    return None


       

        


    


Builder.load_file('admin.kv')
