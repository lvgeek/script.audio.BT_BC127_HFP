# Licence: GPL v.3 http://www.gnu.org/licenses/gpl.html
# XBMC connection to BC127 Bluetooth interface 
# Sparkfun Product: https://www.sparkfun.com/products/11924
# lvgeek: https://github.com/lvgeek

import calendar
import datetime
import sys
import os
import xbmc
import xbmcgui
import xbmcaddon
import socket
import threading
import time



###################################################################################################
###################################################################################################
# Initialization
###################################################################################################
###################################################################################################
KEY_BUTTON_BACK = 275
KEY_KEYBOARD_ESC = 61467

ACTION_PARENT_DIR = 9
ACTION_PREVIOUS_MENU = 10
ACTION_NAV_BACK = 92

TEXT_ALIGN_LEFT = 0
TEXT_ALIGN_RIGHT = 1
TEXT_ALIGN_CENTER_X = 2
TEXT_ALIGN_CENTER_Y = 4
TEXT_ALIGN_RIGHT_CENTER_Y = 5
TEXT_ALIGN_CENTER_X_CENTER_Y = 6

# Get global paths
addon = xbmcaddon.Addon(id = "script.audio.BT_BC127_HFP")
resourcesPath = os.path.join(addon.getAddonInfo('path'),'resources') + '/'
clientScript = os.path.join(addon.getAddonInfo('path'),'resources','jamboree_client.py')
mediaPath = os.path.join(addon.getAddonInfo('path'),'resources','media') + '/'

# Open socket for communication with the gpio-manager UDP server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addonW = 1280
addonH = 720

# Buttons Configuration
BUTTON_H        =105
BUTTON_W        =105

# Label
currentPhNum=xbmcgui.ControlLabel(BUTTON_W*5, BUTTON_H*2, BUTTON_W*4, BUTTON_H*2,
                                '', 'font40_title', '0xffffffff')
currentPhNum1=xbmcgui.ControlLabel(BUTTON_W*5, BUTTON_H*1, BUTTON_W*4, BUTTON_H*2,
                                '', 'font13', '0xffffffff')
#CurrentArtist=xbmcgui.ControlLabel(10, addonH-80, 800, 70,
#                                '', 'font30_title', '0xffffffff')
#CurrentTitle=xbmcgui.ControlLabel(addonW-790, addonH-80, 800, 70,
#                                '', 'font30_title', '0xffffffff', alignment=1)

def phonenumber(value):
    phone = '(%s) %s - %s' %(value[0:3],value[3:6],value[6:10])
    return phone
###################################################################################################
###################################################################################################
# Temperature update thread
###################################################################################################
###################################################################################################
class updateThreadClass(threading.Thread):
    def run(self):
        self.shutdown = False

        while not self.shutdown:
            #currentRssi = int(xbmcgui.Window(10000).getProperty('Radio.RSSI'))
            #Radio_SendCommand(self, "update_rds")

            # Set labels
            currentPhNum.setLabel(phonenumber(currentPhNum1.getLabel()))
#            CurrentArtist.setLabel(str(xbmc.getInfoLabel[xbmc.MusicPlayer.Artist]))
#            CurrentTitle.setLabel(str(xbmc.getInfoLabel[xbmc.MusicPlayer.Title]))
#           currentVolume.setLabel("volume: " + str(xbmcgui.Window(10000).getProperty('Radio.Volume')))

            # Don't kill the CPU
            time.sleep(0.1)

class PhoneHPF(xbmcgui.WindowDialog):
    def __init__(self):
        # Background
        #self.w = self.getWidth()
        #self.h = self.getHeight()
        self.w = addonW
        self.h = addonH
        self.background=xbmcgui.ControlImage(0, 0, self.w, self.h-40, mediaPath + "Carbon-Fiber-9.jpg")
        self.addControl(self.background)

        # top and bottom images
        #self.addControl(xbmcgui.ControlImage(0, 0, self.w, 90, mediaPath + "top_bar.png"))
        #self.addControl(xbmcgui.ControlImage(0, self.h - 90, self.w, 90, mediaPath + "bottom_bar.png"))

        # phone logo
        self.addControl(xbmcgui.ControlImage(self.w - 90, 0, 90, 90, mediaPath + "phoneW.png"))
        self.addControl(xbmcgui.ControlLabel(
            self.w/2 - 150, 25,
            300, 100,
            "Phone",
            textColor='0xffffffff',
            font='font30_title',
            alignment=TEXT_ALIGN_CENTER_X))

    
        # Invisible button used to control focus
        self.buttonfocus = xbmcgui.ControlButton(500, 0, 1, 1, "")
        self.addControl(self.buttonfocus)
        self.setFocus(self.buttonfocus)

        # Home button
        self.button_home=xbmcgui.ControlButton(0, 0, 83, 83,
                                                "",
                                                "floor_buttonFO.png",
                                                "floor_button.png",
                                                0,
                                                0)
        self.addControl(self.button_home)
        self.addControl(xbmcgui.ControlImage(0, 0, 83, 83,
                                                mediaPath + "icon_home.png"))

        # Back button
        self.button_back_img=xbmcgui.ControlImage(self.w - 90, self.h - 130, 83, 83,
                                                "icon_back_w.png")
        self.button_back=xbmcgui.ControlButton(self.w - 90, self.h - 130, 83, 83,
                                                "",
                                                "floor_buttonFO.png",
                                                "floor_button.png",
                                                0,
                                                0)
        self.addControl(self.button_back)
        self.addControl(self.button_back_img)

        # Dialing Buttons
        self.button1=xbmcgui.ControlButton(BUTTON_W, BUTTON_H, BUTTON_W, BUTTON_H,
                                                "1",
                                                "floor_buttonFO.png",
                                                "floor_button.png",
                                                0,
                                                0,TEXT_ALIGN_CENTER_X_CENTER_Y)
        self.addControl(self.button1)
        self.button2=xbmcgui.ControlButton(BUTTON_W*2, BUTTON_H, BUTTON_W, BUTTON_H,
                                                "2",
                                                "floor_buttonFO.png",
                                                "floor_button.png",
                                                0,
                                                0,TEXT_ALIGN_CENTER_X_CENTER_Y)
        self.addControl(self.button2)
        self.button3=xbmcgui.ControlButton(BUTTON_W*3, BUTTON_H, BUTTON_W, BUTTON_H,
                                                "3",
                                                "floor_buttonFO.png",
                                                "floor_button.png",
                                                0,
                                                0,TEXT_ALIGN_CENTER_X_CENTER_Y)
        self.addControl(self.button3)
        self.button4=xbmcgui.ControlButton(BUTTON_W, BUTTON_H*2, BUTTON_W, BUTTON_H,
                                                "4",
                                                "floor_buttonFO.png",
                                                "floor_button.png",
                                                0,
                                                0,TEXT_ALIGN_CENTER_X_CENTER_Y)
        self.addControl(self.button4)
        self.button5=xbmcgui.ControlButton(BUTTON_W*2, BUTTON_H*2, BUTTON_W, BUTTON_H,
                                                "5",
                                                "floor_buttonFO.png",
                                                "floor_button.png",
                                                0,
                                                0,TEXT_ALIGN_CENTER_X_CENTER_Y)
        self.addControl(self.button5)
        self.button6=xbmcgui.ControlButton(BUTTON_W*3, BUTTON_H*2, BUTTON_W, BUTTON_H,
                                                "6",
                                                "floor_buttonFO.png",
                                                "floor_button.png",
                                                0,
                                                0,TEXT_ALIGN_CENTER_X_CENTER_Y)
        self.addControl(self.button6)
        self.button7=xbmcgui.ControlButton(BUTTON_W, BUTTON_H*3, BUTTON_W, BUTTON_H,
                                                "7",
                                                "floor_buttonFO.png",
                                                "floor_button.png",
                                                0,
                                                0,TEXT_ALIGN_CENTER_X_CENTER_Y)
        self.addControl(self.button7)
        self.button8=xbmcgui.ControlButton(BUTTON_W*2, BUTTON_H*3, BUTTON_W, BUTTON_H,
                                                "8",
                                                "floor_buttonFO.png",
                                                "floor_button.png",
                                                0,
                                                0,TEXT_ALIGN_CENTER_X_CENTER_Y)
        self.addControl(self.button8)
        self.button9=xbmcgui.ControlButton(BUTTON_W*3, BUTTON_H*3, BUTTON_W, BUTTON_H,
                                                "9",
                                                "floor_buttonFO.png",
                                                "floor_button.png",
                                                0,
                                                0,TEXT_ALIGN_CENTER_X_CENTER_Y)
        self.addControl(self.button9)
        self.button0=xbmcgui.ControlButton(BUTTON_W*2, BUTTON_H*4, BUTTON_W, BUTTON_H,
                                                "0",
                                                "floor_buttonFO.png",
                                                "floor_button.png",
                                                0,
                                                0,TEXT_ALIGN_CENTER_X_CENTER_Y)
        self.addControl(self.button0)
        self.buttoncall=xbmcgui.ControlButton(BUTTON_W*1, BUTTON_H*5, BUTTON_W*2, BUTTON_H,
                                                "CALL",
                                                "floor_buttonFO.png",
                                                "floor_button.png",
                                                0,
                                                0,TEXT_ALIGN_CENTER_X_CENTER_Y)
        self.addControl(self.buttoncall)

        self.buttonbacksp=xbmcgui.ControlButton(BUTTON_W*3, BUTTON_H*5, BUTTON_W, BUTTON_H,
                                                "<--",
                                                "floor_buttonFO.png",
                                                "floor_button.png",
                                                0,
                                                0,TEXT_ALIGN_CENTER_X_CENTER_Y)
        self.addControl(self.buttonbacksp)
        self.buttonstar=xbmcgui.ControlButton(BUTTON_W*5, BUTTON_H*4, BUTTON_W*3, BUTTON_H,
                                                "Phone Book",
                                                "floor_buttonFO.png",
                                                "floor_button.png",
                                                0,
                                                0,TEXT_ALIGN_CENTER_X_CENTER_Y)
        self.addControl(self.buttonstar)
        self.buttonpnd=xbmcgui.ControlButton(BUTTON_W*5, BUTTON_H*5, BUTTON_W*3, BUTTON_H,
                                                "Edit PhoneBook",
                                                "floor_buttonFO.png",
                                                "floor_button.png",
                                                0,
                                                0,TEXT_ALIGN_CENTER_X_CENTER_Y)
        self.addControl(self.buttonpnd)




		# Add Labels
        self.addControl(currentPhNum)
        self.addControl(currentPhNum1)
        currentPhNum1.setVisible(False)
#        self.addControl(CurrentArtist)
#        self.addControl(CurrentTitle)


        # Start update thread
        self.updateThread = updateThreadClass()
        self.updateThread.start()

        # Store original window ID
        self.prevWindowId = xbmcgui.getCurrentWindowId()
        
        # Go to x11 skin page
        xbmc.executebuiltin("XBMC.ActivateWindow(1112)")
        
        self.setFocus(self.buttonfocus)

    def onAction(self, action):
        # Escape key
        buttonCode = action.getButtonCode()
        actionID = action.getId()
        if (actionID in (ACTION_PREVIOUS_MENU, ACTION_NAV_BACK, ACTION_PARENT_DIR)):
            strWndFnc = "XBMC.ActivateWindow(10000)"
            xbmc.executebuiltin(strWndFnc)
            # stop the temp thread
            sock.close()
            self.updateThread.shutdown = True
            self.updateThread.join()
            self.close()

    def onControl(self, controlID):
        # Back button
        if controlID == self.button_back:
            strWndFnc = "XBMC.ActivateWindow(%i)" % self.prevWindowId
            xbmc.executebuiltin(strWndFnc)
            # stop the temp thread
            sock.close()
            self.updateThread.shutdown = True
            self.updateThread.join()
            self.close()
        
        # HOME button
        if controlID == self.button_home:
            strWndFnc = "XBMC.ActivateWindow(10000)"
            xbmc.executebuiltin(strWndFnc)
            # stop the temp thread
            sock.close()
            self.updateThread.shutdown = True
            self.updateThread.join()
            self.close()

        # Keypad Buttons
        if controlID == self.button1:
            currentPhNum1.setLabel(str(currentPhNum1.getLabel()) + '1')
        if controlID == self.button2:
            currentPhNum1.setLabel(str(currentPhNum1.getLabel()) + '2')
        if controlID == self.button3:
            currentPhNum1.setLabel(str(currentPhNum1.getLabel()) + '3')
        if controlID == self.button4:
            currentPhNum1.setLabel(str(currentPhNum1.getLabel()) + '4')
        if controlID == self.button5:
            currentPhNum1.setLabel(str(currentPhNum1.getLabel()) + '5')
        if controlID == self.button6:
            currentPhNum1.setLabel(str(currentPhNum1.getLabel()) + '6')
        if controlID == self.button7:
            currentPhNum1.setLabel(str(currentPhNum1.getLabel()) + '7')
        if controlID == self.button8:
            currentPhNum1.setLabel(str(currentPhNum1.getLabel()) + '8')
        if controlID == self.button9:
            currentPhNum1.setLabel(str(currentPhNum1.getLabel()) + '9')
        if controlID == self.button0:
            currentPhNum1.setLabel(str(currentPhNum1.getLabel()) + '0')
        if controlID == self.buttonbacksp:
            currentPhNum1.setLabel(str(currentPhNum1.getLabel())[:-1])


'''
seek_right
seek_left
tune_xx.x
volume_xx
toggle_mute
get_frequency
'''
def Radio_SendCommand(self, command):
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    # Send request to server
    sock.sendto("radio_" + command + "\0", (UDP_IP, UDP_PORT))

    # Get reply from server
    data, addr = sock.recvfrom(1024)

    return data
    

# Start the Addon
dialog = PhoneHPF()
dialog.doModal()
sock.close()
del dialog
del addon
