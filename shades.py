from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.properties import BooleanProperty, StringProperty, NumericProperty, ListProperty, ObjectProperty
from kivy.factory import Factory
from kivy.core.window import Window



Builder.load_file('shade.kv')

class RetailApp(App):
    def build(self):
        return sm

class shade1(Screen):
    pass
class shade2(Screen):
    pass
class shade3(Screen):
    pass
class shade4(Screen):
    pass
class shade5(Screen):
    pass
class shade6(Screen):
    pass
class shade7(Screen):
    pass
class shade8(Screen):
    pass

class Electronics(Screen):
    pass
class finish(Screen):
    pass

class help1(Screen):
    pass

class selection(Screen):
    def __init__(self,**kwargs):
        super(selection, self).__init__(**kwargs)
        #self.stal.bind(on_press=self.op)
        #self.stal.bind(on_release=self.op)
    def op(self,*largs):
        if self.stal.text == 'nokia':
            self.stall.text = "S1"
        elif self.stal.text == "samsung":
            self.stall.text = "S2"
        elif self.stal.text == "apple":
            self.stall.text = "S3"
        else:
            self.stall.text = self.stal.text
    def op1(self, *largs):
        if self.stall.text == 'S1':
            self.stal.text = "nokia"
        elif self.stall.text == "S2":
            self.stal.text = "samsung"
        elif self.stall.text == "S3":
            self.stal.text = "apple"
        else:
            self.stal.text = 'company'
        
       
        
    
    
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)

                        
class shades(Screen):
    def __init__(self, **kwargs):
        super(shades, self).__init__(**kwargs)
        
        
sm=ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Electronics(name='Electronics'))

sm.add_widget(shades(name='shades'))
sm.add_widget(shade1(name='shade1'))
sm.add_widget(shade2(name='shade2'))
sm.add_widget(shade3(name='shade3'))
sm.add_widget(shade4(name='shade4'))
sm.add_widget(shade5(name='shade5'))
sm.add_widget(shade6(name='shade6'))
sm.add_widget(shade7(name='shade7'))
sm.add_widget(shade8(name='shade8'))
sm.add_widget(finish(name='finish'))
sm.add_widget(selection(name='selection'))
sm.add_widget(help1(name='help'))




    
if __name__ == '__main__':
    RetailApp().run()
