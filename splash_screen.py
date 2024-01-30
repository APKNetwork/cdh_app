

# D E P R E C A T E D on 22/01/24


from flet import *
from pages.forgot_password import ForgotPassword
from pages.initapp import main

from utils.extras import *

print("inicio en el MAIN de Splash_Screen")
print("creo que no se ejecuta")

class Main(UserControl):
    def __init__(self, page: Page,):
        super().__init__()
        page.window_title_bar_hidden = True
        page.window_frameless = True
        page.window_title_bar_buttons_hidden = True
        page.bgcolor = colors.TRANSPARENT
        page.window_bgcolor = colors.TRANSPARENT
        page.window_width = base_width
        page.window_height = base_height
        page.fonts = {
            "Poppins ThinItalic":"fonts/poppins/Poppins/ThinItalic.ttf",
            "Poppins Black":"fonts/poppins/Poppins-Black.ttf",
            "Poppins BlackItalic":"fonts/poppins/Poppins-BlackItalic.ttf",
            "Poppins Bold":"assets/fonts/poppins/Poppins-Bold.ttf",
            "Poppins BoldItalic":"fonts/poppins/Poppins-BoldItalic.ttf",
            "Poppins ExtraBold":"fonts/poppins/Poppins-ExtraBold.ttf",
            "Poppins ExtraBoldItalic":"fonts/poppins/Poppins-ExtraBoldItalic.ttf",
            "Poppins ExtraLight":"fonts/poppins/Poppins-ExtraLight.ttf",
            "Poppins ExtraLightItalic":"fonts/poppins/Poppins-ExtraLightItalic.ttf",
            "Poppins Italic":"fonts/poppins/Poppins-Italic.ttf",
            "Poppins Light":"fonts/poppins/Poppins-Light.ttf",
            "Poppins LightItalic":"fonts/poppins/Poppins-LightItalic.ttf",
            "Poppins Medium":"fonts/poppins/Poppins-Medium.ttf",
            "Poppins MediumItalic":"fonts/poppins/Poppins-MediumItalic.ttf",
            "Poppins Regular":"fonts/poppins/Poppins-Regular.ttf",
            "Poppins SemiBold":"fonts/poppins/Poppins-SemiBold.ttf",
            "Poppins SemiBoldItalic":"fonts/poppins/Poppins-SemiBoldItalic.ttf",
            "Poppins Thin":"fonts/poppins/Poppins-Thin.ttf",
        }
        #page.add(ft.ElevatedButton("I'm a floating button!"))

        page.fonts = {

        }
        self.page = page
        self.init_helper()

    def init_helper(self,):
        self.page.on_route_change = self.on_route_change
        self.page.go('/initapp')

    def on_route_change(self,route):
        new_page = {
            "/initapp" : main,
            "/forgotpassword" : ForgotPassword
        }[self.page.route](self.page)

        self.page.views.clear()
        self.page.views.append(
            View(
                route,
                [new_page]
            )
        )
app(target=Main, assets_dir='assets')