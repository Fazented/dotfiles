import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello World")

        def button(x):
            self.button = Gtk.Button(label="button")
            self.button.connect("clicked", self.on_button_clicked)
            self.add(self.button)

        button(x)

    def on_button_clicked(self, widget):
        print("Hello World")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()