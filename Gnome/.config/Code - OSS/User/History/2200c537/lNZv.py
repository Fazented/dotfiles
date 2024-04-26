import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ButtonWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="gay button")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_label("gay")
        button.connect("clicked", self.clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.ToggleButton("gay gay gay gay gay gay gay gay gay gay gay ")
        button.connect("clicked", self.clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.RadioButton.new_with_label_from_widget(None, "ufwhiuwrehiurfiuer")
        button.connect("clicked", self.clicked)
        hbox.pack_start(button, True, True, 0)

        button1 = Gtk.RadioButton.new_with_label_from_widget(None, "hi")
        button1.connect("toggled", self.clicked, "1")
        hbox.pack_start(button1, False, False, 0)

        
    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)

    def clicked(self, button):
        print('you are gay')


win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()