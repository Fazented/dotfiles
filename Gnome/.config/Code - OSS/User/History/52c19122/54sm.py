import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class GtkWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Button Tests")
        self.set_border_width(10)

        #hbox = Gtk.Box(spacing=6)
        #self.add(hbox)

        def button():
            self.button = Gtk.Button(label="button")
            self.button.connect("clicked", self.on_button_clicked)
            self.add(self.button)

        button()

    def on_button_clicked(self, widget):
        print("Hello World")

win = GtkWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()