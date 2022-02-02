from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import time

from filesharer import FileSharer
import webbrowser

Builder.load_file("frontend.kv")


class CameraScreen(Screen):  # This is called boilerplate code. Just copied & pasted

    def start(self):
        """Starts the camera and changes the Button text"""
        self.ids.camera.play = True
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """Stops the camera and changes the button text"""
        self.ids.camera.play = False
        self.ids.camera.texture = None

    def capture(self):
        """Creates a unique file path with the current timestamp in the files dir"""
        self.file_path = "files/" + time.strftime("%Y%m%d-%H%M%S") + ".png"
        self.ids.camera.export_to_png(self.file_path)
        self.manager.current = "image_screen"
        self.manager.current_screen.ids.img.source = self.file_path

class ImageScreen(Screen):
    link_error_message = "Generate a URl first!"
    def create_link(self):
        """Accesses the photo filepath, uploads it to the web and inserts the link
        in the Label widget"""
        # filepath = App.get_running_app().root.ids.camera_screen.filepath
        # filesharer = FileSharer(filepath=filepath)
        self.url = "www.google.com"
        self.ids.link.text = "Filestack currently unavailable"

    def copy_link(self):
        """Copy link into the clipboard available for posting"""
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_error_message

    def open_link(self):
        """Open link with the default browser"""
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_error_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()


