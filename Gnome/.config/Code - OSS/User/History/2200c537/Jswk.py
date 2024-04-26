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
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.ToggleButton("gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay gay ")
        button.connect("clicked", self.on_open_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("goodbye")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_click_me_clicked(self, button):
        print('you are gayest')

    def on_open_clicked(self, button):
        print('you are gay')

    def on_close_clicked(self, button):
        print("gay")
        Gtk.main_quit()


win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()