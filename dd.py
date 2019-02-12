from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
import threading
from time import sleep
from functools import partial
import socket

k = 10

hote = "127.0.0.1"
port = 15555
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))

print("Connection sur {}".format(port))

def gh(direction, h):
	global k
	socket.send(direction.encode())

class TestApp(App):

	def build(self):
		global k
		buttonc1 = partial(gh, "1")
		buttonc2 = partial(gh, "2")
		buttonc3 = partial(gh, "3")
		buttonc4 = partial(gh, "4")

		parent = FloatLayout()

		button0 = ToggleButton(text='tirer', size_hint=(.3, .3), group="tire" ,pos_hint={'x':.35, 'y':.35})

		button1 = ToggleButton(text='gauche', size_hint=(.3, .3), group="deplacement" ,pos_hint={'x':.05, 'y':.35})
		button1.bind(on_press=buttonc1)
		button2 = ToggleButton(text='droite', size_hint=(.3, .3), group="deplacement", pos_hint={'x':.65, 'y':.35})
		button2.bind(on_press=buttonc2)
		button3 = ToggleButton(text='avancer', size_hint=(.3, .3), group="deplacement" ,pos_hint={'x':.35, 'y':.05})
		button3.bind(on_press=buttonc3)
		button4 = ToggleButton(text='reculer', size_hint=(.3, .3), group="deplacement" ,pos_hint={'x':.35, 'y':.65})
		button4.bind(on_press=buttonc4)

		a = [button0, button1, button2, button3, button4]

		for i in a:
			parent.add_widget(i)

		return parent

TestApp().run()

