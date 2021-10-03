import sys
import os
from kivy.lang import Builder
from kivy.config import Config
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(base_path, relative_path)

from kivy.core.audio import SoundLoader
from kivy.uix.progressbar import ProgressBar

from kivy.core.window import Window
from kivy.clock import Clock
from kivy import utils
from kivy.animation import Animation
from kivy.resources import resource_add_path
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, SlideTransition, WipeTransition, FadeTransition, FallOutTransition, NoTransition
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

import sqlite3

resource_add_path(resource_path(os.path.join('screens', 'mainpage')))
resource_add_path(resource_path(os.path.join('screens', 'cloud')))
resource_add_path(resource_path(os.path.join('screens', 'login')))
resource_add_path(resource_path(os.path.join('screens', 'account')))
resource_add_path(resource_path(os.path.join('screens', 'dashboard')))
resource_add_path(resource_path(os.path.join('screens', 'settings')))
resource_add_path(resource_path(os.path.join('data', 'fonts')))
resource_add_path(resource_path(os.path.join('screens', 'admin')))
resource_add_path(resource_path(os.path.join('screens', 'user')))
resource_add_path(resource_path(os.path.join('screens', 'profile')))
resource_add_path(resource_path(os.path.join('screens', 'table')))
resource_add_path(resource_path(os.path.join('screens', 'messages')))

resource_add_path(resource_path(os.path.join('sound')))






class Software(MDApp):
    title = "title"
    icon = 'icon.ico'
    use_kivy_settings = False
    color_theme = 'light'
    bg_color = ListProperty([29 / 255, 29 / 255, 29 / 255, 1])
    tile_color = ListProperty([40 / 255, 40 / 255, 40 / 255, 1])
    raised_button_color = ListProperty([52 / 255, 52 / 255, 52 / 255, 1])
    text_color = ListProperty([1, 1, 1, 1])
    title_text_color = ListProperty([1, 1, 1, 1])
    accent_color = ListProperty([0.5, 0.7, 0.5, 1])
    app_font = StringProperty(
        resource_path(
            os.path.join(
                'data',
                'fonts',
                'Code2000',
                'CODE2000.ttf')))
    cursor_width = NumericProperty(5)
    home_icon = StringProperty('home')
    home_icon_tooltip = StringProperty('Back')
    add_icon = StringProperty('plus-circle-outline')
    add_icon_tooltip = StringProperty('Create new')
    search_icon = StringProperty('magnify')
    search_icon_tooltip = StringProperty('Search')

    def open_settings(self, *largs):
        self.mainmenu.ids.settings_button.trigger_action()

    def build(self):
        Window.fullscreen = 'auto'
        self.theme_cls.primary_palette = "Green"
        self.themes = {
            'dark': self.color_theme_dark,
            'light': self.color_theme_light,
        }
        self.transitions = {
            'slide': SlideTransition,
            'wipe': WipeTransition,
            'fade': FadeTransition,
            'fall out': FallOutTransition,
            'none': NoTransition
        }
        if getattr(sys, 'frozen', False):
            pass        
        else:
            from screens import mainpage,cloud,login,settings,account,dashboard,admin,user,profile,table,messages
        self.sm = ScreenManager()
        self.mainpage = mainpage.Mainpage()
        self.cloud=cloud.Cloud()
        self.login=login.Login()
        self.settings=settings.Settings()
        self.account=account.Account()
        self.home=dashboard.Home()
        self.user=user.User()
        self.admin=admin.Admin()
        self.profile=profile.Profile()
        self.table=table.Table()
        self.messages=messages.Messages()
        self.screens = {
            'login':self.login,
            'mainpage': self.mainpage,
            'settings':self.settings,
            'cloud':self.cloud,
            'account':self.account,
            'home':self.home,
            'user':self.user,
            'admin':self.admin,
            'profile':self.profile,
            'table':self.table,
            'messages':self.messages
        }
        self.sm.switch_to(self.login)

        return self.sm

    @property
    def click_sound(self):
        click = SoundLoader.load("sound/click.wav")
        click.play()

  

    def choosefile(self):
        self.mainpage.file_manager_open()


    def switch_screen(self, screen_name):
        print("swithing screen:"+str(screen_name))
        self.sm.switch_to(self.screens.get(screen_name))

    def progress(self):
        self.progress_bar = ProgressBar()
        self.popup_loading = Popup(title ='loading page',content = self.progress_bar)
        self.popup_loading.bind(on_open = self.open)
        self.popup_loading.open()

    def Message(self,message):
        layout = GridLayout(cols = 1, padding = 10) 
        popupLabel = Label(text=str(message))
        closeButton = Button(text = "Close") 
        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)   
        self.popup = Popup(title='message',
    content=layout,
    size_hint=(None, None), size=(400, 400))
        self.popup.open()
        closeButton.bind(on_press = self.popup.dismiss)


    def on_start(self):
        self.login.dispatch("on_enter")

    def color_theme_dark(self):
        self.theme_cls.theme_style="Dark"

    def color_theme_light(self):
        self.theme_cls.theme_style="Light"

    def User(self):
        self.mainpage.ids.user.disabled = True
        self.mainpage.ids.history.disabled = True


    def Admin(self):
        self.mainpage.ids.user.disabled = False
        self.mainpage.ids.history.disabled = False
    

    def Username(self,name,user):
        self.mainpage.person.text=str(name)
        try:
            for count,filename in enumerate(os.listdir("data/profile/"+str(name))): 
                photo="data/profile/"+str(name)+ "/"+filename
            isFile = os.path.isfile(photo) 
            if isFile:
                self.profile.image.source=photo
                self.mainpage.image.source=photo
            else:
                self.profile.image.source="data/images/default1.png"
                self.mainpage.image.source="data/images/default1.png"
        except :
            self.profile.image.source="data/images/default1.png"
            self.mainpage.image.source="data/images/default1.png"

        self.profile.Board(name,user)


    def transition_changed(self, user_settings):
        try:
            self.root.transition = self.transitions.get(
        user_settings.get('page_transition'))()
        except BaseException:
            self.root.transition = SlideTransition()

    def open(self, instance):
        Clock.schedule_interval(self.next, 1 / 25)

    def next(self, dt):
        if self.progress_bar.value>= 100:
            self.popup_loading.dismiss()
        self.progress_bar.value += 3

    def Admindata(self):
        conn = sqlite3.connect(r'screens\admin\db.sqlite3', check_same_thread=False)
        c = conn.cursor()
        return c

    def Userdata(self):
        conn = sqlite3.connect(r'screens\user\db.sqlite3', check_same_thread=False)
        c = conn.cursor()
        return c

  

    






    
      

      


if __name__ == '__main__':
    Software().run()
