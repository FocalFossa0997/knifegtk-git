#!/usr/bin/python3
import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class AboutWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="About Knife")
        self.set_keep_above(True)
        self.set_resizable(False)

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.mlabel = Gtk.Label(label="Knife is a tool created by Focal Fossa. This tool allows you to easily kill processes.")
        self.box.pack_start(self.mlabel, True, True, 0)

        self.cbutton = Gtk.Button(label="Close")
        self.cbutton.connect("clicked", self.on_cbutton_pressed)
        self.box.pack_start(self.cbutton, True, True, 0)

    def on_cbutton_pressed(self, widget):
        self.hide()


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Knife")
        self.set_keep_above(True)
        self.set_resizable(False)

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.pidEntry = Gtk.Entry(placeholder_text="Process ID or name")
        self.box.pack_start(self.pidEntry, True, True, 0)

        self.killButton = Gtk.Button(label="Kill")
        self.killButton.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.killButton, True, True, 0)

        self.killallButton = Gtk.Button(label="Kill All")
        self.killallButton.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.killallButton, True, True, 0)

        self.xkillButton = Gtk.Button(label="Kill Using Mouse")
        self.xkillButton.connect("clicked", self.on_button4_clicked)
        self.box.pack_start(self.xkillButton, True, True, 0)

        self.aboutButton = Gtk.Button(label="About")
        self.aboutButton.connect("clicked", self.on_button3_clicked)
        self.box.pack_start(self.aboutButton, True, True, 0)

    def on_button1_clicked(self, widget):
        os.system("kill " + self.pidEntry.get_text())

    def on_button2_clicked(self, widget):
        os.system("killall " + self.pidEntry.get_text())

    def on_button3_clicked(self, widget):
        aw.show_all()
    
    def on_button4_clicked(self, widget):
        os.system("xkill")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
aw = AboutWindow()
aw.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
