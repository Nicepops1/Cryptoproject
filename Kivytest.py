from kivy.config import Config

Config.set("graphics", "resizable" , 1)
Config.set("graphics","width", 500)
Config.set("graphics","height", 200)
Config.set('graphics',"borderless", 1)

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget

class MyApp(App):

	def build(self):
		main_al = AnchorLayout(anchor_x = "center", anchor_y = "top")
		inside_bx = BoxLayout(orientation = 'horizontal', size_hint = (1,.15), spacing = 75)
		inside_bx.add_widget( Label(text = "Username"))
		inside_bx.add_widget( Button(text = "+", size_hint = (.4,1)))
		triple_bx = BoxLayout(orientation = "horizontal")
		triple_bx.add_widget( Button(text = "[]", on_press = self.fullscreen_press))
		triple_bx.add_widget( Button(text = "_", on_press = self.btnhide_press))
		triple_bx.add_widget( Button(text = "X", on_press = self.btnclose_press))
		inside_bx.add_widget( triple_bx)
		main_al.add_widget(inside_bx)
	
		return main_al

	def fullscreen_press(self, instance):
		Window.maximize()

	def drag_press(self,instance):
		Window.grab_mouse()

	def btnclose_press(self, instance):
		Window.close()

	def btnhide_press(self, instance):
		Window.minimize()

if __name__ =="__main__":
	MyApp().run()