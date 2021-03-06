#!/usr/bin/env python

"""
A GTK quick message popup program.

Allows users to quickly share messages with others on their own screen. Useful
for when you need to be silent but want to communicate with the person sitting
next to you, e.g. for games of hangman during lectures.

TODO: allow multi-lines
"""

__author__ = 'Ali Scott'

import pygtk
pygtk.require('2.0')
import gtk

import pango

X_PADDING = 40
Y_PADDING = 20
X_MARGIN = 60
FONT_FACE = 'lucida sans unicode'
FONT_SIZE = '62'
BG_COLOR = '#000'
TEXT_COLOR = '#fff'
OPACITY = 0.8


class QuickText:
    """
    Draws the window and handles the key events.
    """

    def __init__(self):
        """
        Sets up the window and the text area.
        """
        self.window = self._setup_window()
        self.textarea = self._setup_textarea()
        self.window.connect('destroy', gtk.main_quit)
        self.window.connect('key_press_event', self._on_key_press)
        self.textarea.connect('changed', self._text_changed)

        font_desc = pango.FontDescription(FONT_FACE + ' ' + FONT_SIZE)
        self.textarea.modify_font(font_desc)
        # layout used for finding pixel size of font
        self.layout = pango.Layout(gtk.Widget \
                                   .create_pango_context(self.window))
        self.layout.set_font_description(font_desc)

        (w, h) = self.layout.get_pixel_size()
        # set starting height of the text area to be the height of the font
        self.textarea.set_size_request(w, h)
        # add padding to the size of the window
        self.window.resize(w + X_PADDING, h + Y_PADDING)

        self.window.add(self.textarea)
        self.textarea.show()
        self.window.show()

    def _setup_window(self):
        """
        Styles the window.
        """
        w = gtk.Window(gtk.WINDOW_TOPLEVEL)
        w.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        w.set_decorated(False)
        w.set_has_frame(False)
        w.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse(BG_COLOR))
        w.set_opacity(OPACITY)
        return w

    def _setup_textarea(self):
        """
        Styles the text area.
        """
        t = gtk.Entry()
        t.set_alignment(0.5)
        t.set_has_frame(False)
        t.modify_base(gtk.STATE_NORMAL, gtk.gdk.color_parse(BG_COLOR))
        t.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse(BG_COLOR))
        t.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse(TEXT_COLOR))
        return t

    def _on_key_press(self, widget, event):
        """
        Handles key press events.
        Quits when the enter key is pressed.
        """
        if gtk.gdk.keyval_name(event.keyval) == 'Return':
            gtk.Widget.destroy(self.window)

    def _text_changed(self, widget):
        """
        Handles resizing of window when text is written.
        """
        # get size of text
        self.layout.set_text(self.textarea.get_text())
        (w, h) = self.layout.get_pixel_size()
        # resize window and text area to fit text and screen size
        max_width = gtk.gdk.screen_width() - X_MARGIN
        self.textarea.set_size_request(min(w, max_width - X_PADDING), h)
        self.window.resize(min(w + X_PADDING, max_width), h + Y_PADDING)

    def main(self):
        """
        Runs the program.
        """
        gtk.main()


def main():
    q = QuickText()
    q.main()

if __name__ == '__main__':
    main()
