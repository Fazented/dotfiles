import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class GtkWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Button Tests")
        self.set_border_width(10)
        self.set_default_size(400, 250)

        #hbox = Gtk.Box(spacing=6)
        #self.add(hbox)



        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Button Tests"

        button = Gtk.Button()
        icon = Gio.ThemedIcon(name="mail-send-receive-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button.add(image)
        hb.pack_end(button)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        button = Gtk.Button()
        button.add(
            Gtk.Arrow(arrow_type=Gtk.ArrowType.LEFT, shadow_type=Gtk.ShadowType.NONE)
        )
        box.add(button)

        button = Gtk.Button.new_from_icon_name("pan-end-symbolic", Gtk.IconSize.MENU)
        box.add(button)

        hb.pack_start(box)




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