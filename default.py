# -*- coding: utf-8 -*-
# Licence: GPL v.3 http://www.gnu.org/licenses/gpl.html
# This is an XBMC addon using PyXBMCt framework.
# XBMC connection to BC127 Bluetooth interface 
# Sparkfun Product: https://www.sparkfun.com/products/11924
# lvgeek: https://github.com/lvgeek

import os
import xbmc
import xbmcgui
import xbmcaddon
import pyxbmct.addonwindow as pyxbmct


class MyAddon(pyxbmct.AddonFullWindow):
    def __init__(self, title=''):
        """Class constructor"""
        super(MyAddon, self).__init__(title)
        screenx = self.getWidth()
        screeny = self.getHeight()
        self.setGeometry(screenx, screeny, 5, 9)
        self.set_controls()
        self.set_navigation()
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)

    def set_controls(self):
        """Set up UI controls"""
        self.1_button = pyxbmct.Button('1')
        self.placeControl(self.1_button, 0, 0)

#        self.2_button = pyxbmct.Button('2')
#        self.placeControl(self.1_button, 0, 2)
#        self.3_button = pyxbmct.Button('3')
#        self.placeControl(self.1_button, 0, 3)
#        self.4_button = pyxbmct.Button('4')
#        self.placeControl(self.1_button, 1, 0)
#        self.close_button = pyxbmct.Button('Close')
#        self.placeControl(self.close_button, 4, 0)
#        self.connect(self.close_button, self.close)
#        self.hello_buton = pyxbmct.Button('Hello')
#        self.placeControl(self.hello_buton, 3, 1)
#        self.connect(self.hello_buton, lambda:
#            xbmc.executebuiltin('Notification(Hello {0}!, Welcome to PyXBMCt.)'.format(self.name_field.getText())))

    def set_navigation(self):
        """Set up keyboard/remote navigation between controls."""
        self.name_field.controlUp(self.hello_buton)
        self.name_field.controlDown(self.hello_buton)
        self.close_button.controlLeft(self.hello_buton)
        self.close_button.controlRight(self.hello_buton)
        self.hello_buton.setNavigation(self.name_field, self.name_field, self.close_button, self.close_button)
        self.setFocus(self.name_field)

if __name__ == '__main__':
    myaddon = MyAddon('Bluetooth Phone Interface')
    myaddon.doModal()
    del myaddon
