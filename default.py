# Import necessary modules
import xbmc
import pyxbmct.addonwindow as pyxbmct

# Create a class for our UI
class MyAddon(pyxbmct.AddonDialogWindow):

    def __init__(self, title=''):
        """Class constructor"""
        # Call the base class' constructor.
        super(MyAddon, self).__init__(title)
        # Set width, height and the grid parameters
        self.setGeometry(300, 230, 4, 2)
        # Call set controls method
        self.set_controls()
        # Call set navigation method.
        self.set_navigation()
        # Connect Backspace button to close our addon.
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)

    def set_controls(self):
        """Set up UI controls"""
        # Image control
        image = pyxbmct.Image('xbmc-logo.png')
        self.placeControl(image, 0, 0, rowspan=2, columnspan=2)
        # Text label
        label = pyxbmct.Label('Your name:')
        self.placeControl(label, 2, 0)
        # Text edit control
        self.name_field = pyxbmct.Edit('')
        self.placeControl(self.name_field, 2, 1)
        # Close button
        self.close_button = pyxbmct.Button('Close')
        self.placeControl(self.close_button, 3, 0)
        # Connect close button
        self.connect(self.close_button, self.close)
        # Hello button.
        self.hello_buton = pyxbmct.Button('Hello')
        self.placeControl(self.hello_buton, 3, 1)
        # Connect Hello button.
        self.connect(self.hello_buton, lambda:
            xbmc.executebuiltin('Notification(Hello {0}!, Welcome to PyXBMCt.)'.format(self.name_field.getText())))

    def set_navigation(self):
        """Set up keyboard/remote navigation between controls."""
        self.name_field.controlUp(self.hello_buton)
        self.name_field.controlDown(self.hello_buton)
        self.close_button.controlLeft(self.hello_buton)
        self.close_button.controlRight(self.hello_buton)
        self.hello_buton.setNavigation(self.name_field, self.name_field, self.close_button, self.close_button)
        # Set initial focus.
        self.setFocus(self.name_field)

if __name__ == '__main__':
    myaddon = MyAddon('PyXBMCt Example')
    myaddon.doModal()
    del myaddon
