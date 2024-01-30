

# O N  A N D  E X A M P L E - I N V A L I D #


from flet import *
from utils.views import views_handler
from pages.initapp import main

def main(page: Page):

  def route_change(route):
    page.views.clear()
    page.views.append(
      views_handler(page)[page.route]
    )

  print("Es raro, entré en indexer nuevo")

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

  page.on_route_change = route_change
  page.go('/initapp')


app(target=main,  assets_dir="assets")