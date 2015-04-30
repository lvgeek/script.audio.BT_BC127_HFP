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
        self.setGeometry(1200, 600, 5, 8)
        self.set_controls()
        self.set_navigation()
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)

    def set_controls(self):
        """Set up UI controls"""
        self.phone_number = pyxbmct.Label('', 'font18')
        self.placeControl(self.phone_number, 1, 4, rowspan=2, columnspan=3)
        self.button1 = pyxbmct.Button('1')
        self.placeControl(self.button1, 0, 0)
        self.connect(self.button1, self.set_phone)
        self.button2 = pyxbmct.Button('2')
        self.placeControl(self.button2, 0, 1)
        self.connect(self.button2, self.set_phone)
        self.button3 = pyxbmct.Button('3')
        self.placeControl(self.button3, 0, 2)
        self.connect(self.button3, self.set_phone)
        self.button4 = pyxbmct.Button('4')
        self.placeControl(self.button4, 1, 0)
        self.connect(self.button4, self.set_phone)
        self.button5 = pyxbmct.Button('5')
        self.placeControl(self.button5, 1, 1)
        self.connect(self.button5, self.set_phone)
        self.button6 = pyxbmct.Button('6')
        self.placeControl(self.button6, 1, 2)
        self.connect(self.button6, self.set_phone)
        self.button7 = pyxbmct.Button('7')
        self.placeControl(self.button7, 2, 0)
        self.connect(self.button7, self.set_phone)
        self.button8 = pyxbmct.Button('8')
        self.placeControl(self.button8, 2, 1)
        self.connect(self.button8, self.set_phone)
        self.button9 = pyxbmct.Button('9')
        self.placeControl(self.button9, 2, 2)
        self.connect(self.button9, self.set_phone)
        self.button0 = pyxbmct.Button('0')
        self.placeControl(self.button0, 3, 1)
        self.connect(self.button0, self.set_phone)
        self.call_button = pyxbmct.Button('Call')
        self.placeControl(self.call_button, 4, 0)
        self.connect(self.call_button, self.set_phone)
        self.close_button = pyxbmct.Button('Close')
        self.placeControl(self.close_button, 0, 7)
        self.connect(self.close_button, self.close)
#        self.hello_buton = pyxbmct.Button('Hello')
#        self.placeControl(self.hello_buton, 3, 1)
#        self.connect(self.hello_buton, lambda:xbmc.executebuiltin('Notification(Hello {0}!, Welcome to PyXBMCt.)'.format(self.name_field.getText())))

    def set_navigation(self):
        """Set up keyboard/remote navigation between controls."""
#        self.name_field.controlUp(self.hello_buton)
#        self.name_field.controlDown(self.hello_buton)
#        self.close_button.controlLeft(self.hello_buton)
#        self.close_button.controlRight(self.hello_buton)
#        self.hello_buton.setNavigation(self.name_field, self.name_field, self.close_button, self.close_button)
#        self.setFocus(self.name_field)

    def set_phone(self):
        try:
            if self.getFocus() == self.button1:
                self.phone_number.setLabel(str(self.phone_number.getLabel()) + '1')
            elif self.getFocus() == self.button2:
                self.phone_number.setLabel(str(self.phone_number.getLabel()) + '2')
            elif self.getFocus() == self.button3:
                self.phone_number.setLabel(str(self.phone_number.getLabel()) + '3')
            elif self.getFocus() == self.button4:
                self.phone_number.setLabel(str(self.phone_number.getLabel()) + '4')
            elif self.getFocus() == self.button5:
                self.phone_number.setLabel(str(self.phone_number.getLabel()) + '5')
            elif self.getFocus() == self.button6:
                self.phone_number.setLabel(str(self.phone_number.getLabel()) + '6')
            elif self.getFocus() == self.button7:
                self.phone_number.setLabel(str(self.phone_number.getLabel()) + '7')
            elif self.getFocus() == self.button8:
                self.phone_number.setLabel(str(self.phone_number.getLabel()) + '8')
            elif self.getFocus() == self.button9:
                self.phone_number.setLabel(str(self.phone_number.getLabel()) + '9')
            elif self.getFocus() == self.button0:
                self.phone_number.setLabel(str(self.phone_number.getLabel()) + '0')
        except (RuntimeError, SystemError):
            pass


if __name__ == '__main__':
    myaddon = MyAddon('Bluetooth Phone Interface')
    myaddon.doModal()
    del myaddon
