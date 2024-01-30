from flet import *
from utils.views import views_handler
from utils.extras import *

def main(page: Page):

  def route_change(route):
    page.views.clear()
    page.views.append(
      views_handler(page)[page.route]
    )

    page.theme_mode = ThemeMode.LIGHT #Switch the dark ver to deep-purple
    #page.theme_mode = ThemeMode.SYSTEM 

    page.window_title_bar_hidden = True
    page.window_frameless = True
    page.window_title_bar_buttons_hidden = True
    page.bgcolor = colors.TRANSPARENT
    page.window_bgcolor = colors.TRANSPARENT
    #page.window_width = 400
    #page.window_height = 2000

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
  
  # page.navigation_bar = NavigationBar(
  #       destinations=[
  #           NavigationDestination(icon=icons.EXPLORE, label="Explore"),
  #           NavigationDestination(icon=icons.COMMUTE, label="Commute"),
  #           NavigationDestination(
  #               icon=icons.BOOKMARK_BORDER,
  #               selected_icon=icons.BOOKMARK,
  #               label="Explore",
  #           ),
  #       ]
  #   )


  page.on_route_change = route_change
  print("")
  print("estoy justo iniciando la ejecución")
  # -> page.go('/onboarding') # going to onboarding_screens ->
  page.go('/') # skip to logged_out
  # page.go('/login')
  # page.go('/profile')

app(target=main,  assets_dir="assets")