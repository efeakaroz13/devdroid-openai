from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.label import MDLabel

kvstring = """
<OpeningScreen>:
	id:"welcome"
	
	
	FloatLayout:
			
		MDToolbar:
			title:"DevDroid"
			md_bg_color:app.theme_cls.primary_color
		
			pos_hint:{"top":1}
		MDLabel:
			text:""		

		MDLabel:
			text:"Welcome to DevDroid!"
			font_style:"H5"
			halign:"center"
			pos_hint:{"top":1.25}
	

		
				

<HomeScreen>:
	id:"home"
	BoxLayout:
		orientation:"vertical"
	
		MDToolbar:
			title:"DevDroid"
			pos_hint:{"top":1}
			md_bg_color:app.theme_cls.primary_color

		MDLabel:
			text:"Content"
		
"""
#Builder.load_string(kvstring)

class OpeningScreen(Screen):
	def __init__(self,**kwargs):
		toolbarthing = MDToolbar(title="DevDroid",background_hue="600",elevation=10)
		self.add_widget(toolbarthing)
class HomeScreen(Screen):
	pass

class DevDroid(MDApp):
	def build(self):
		sm = ScreenManager()
	
		self.theme_cls.primary_palette = "BlueGray"
		mybox = BoxLayout(orientation="vertical")
		toolbarthing = MDToolbar(title="DevDroid",md_bg_color=self.theme_cls.primary_color,background_hue="600",elevation=10)
		welcometext= MDLabel(text="Welcome to DevDroid!",halign="center")
		
		mybox.add_widget(welcometext)
		mybox.add_widget(toolbarthing)
		#OpeningScreen.add_widget(mybox)

		sm.add_widget(HomeScreen(name="home"))
		sm.add_widget(OpeningScreen(name="welcome"))
		sm.current="welcome"	
		return sm


DevDroid().run()
