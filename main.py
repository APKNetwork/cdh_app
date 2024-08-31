from flet import *
from utils.views import views_handler
from utils.extras import *
from db.flet_pyrebase import PyrebaseWrapper
import os
import json

print("Inicio del script")

def main(page: Page):

  page.title = "Welcome to CryDiagnoHealth" #Title Page
  # page.horizontal_alignment = CrossAxisAlignment.CENTER
  # page.scroll = ScrollMode.ADAPTIVE
  # page.update()
  myPyrebase = PyrebaseWrapper(page)

  def route_change(route):
    page.views.clear()
    page.views.append(
      views_handler(page, myPyrebase)[page.route] #added myparebase
    )

    def page_resize(e):
      print("New page size:", page.window.width, page.window.height)
    page.on_resized = page_resize

    # Configuraciones de alineación y estilo
    page.views[0].horizontal_alignment = CrossAxisAlignment.CENTER
    page.views[0].vertical_alignment = MainAxisAlignment.START
    
    # Configuración de la ventana
    page.theme_mode = ThemeMode.LIGHT #Switch the dark ver to deep-purple
    #page.window.maximized = True  # Maximizar la ventana para que ocupe toda la altura disponible
    
    page.window.width = 420  # Establecer el ancho en 600 píxeles
    # Calcular la altura aproximada del dispositivo
    screen_height = page.window.height  # Obtener la altura actual de la ventana, esta es relativa y se calcula en proporcion de apertura
    page.window.height = screen_height * 1.2  # Establecer la altura al 120% del alto disponible
    # page.window.resizable = False  # Desactiva el cambio de tamaño

    page.window.shadow = True
    page.window.center()
    page.window.title_bar_hidden = False
    page.window.frameless = False
    page.window.title_bar_buttons_hidden = False
    page.window.bgcolor = colors.TRANSPARENT
    
    # Habilitar scroll
    #page.views[0].scroll = ScrollMode.ALWAYS  # Habilitar scroll siempre
    
    page.update()

    # page.theme_mode = ThemeMode.SYSTEM 


    page.fonts = {
      "Poppins ThinItalic":"/fonts/poppins/Poppins/ThinItalic.ttf",
      "Poppins Black":"/fonts/poppins/Poppins-Black.ttf",
      "Poppins BlackItalic":"/fonts/poppins/Poppins-BlackItalic.ttf",
      "Poppins Bold":"/fonts/poppins/Poppins-Bold.ttf",
      "Poppins BoldItalic":"/fonts/poppins/Poppins-BoldItalic.ttf",
      "Poppins ExtraBold":"/fonts/poppins/Poppins-ExtraBold.ttf",
      "Poppins ExtraBoldItalic":"/fonts/poppins/Poppins-ExtraBoldItalic.ttf",
      "Poppins ExtraLight":"/fonts/poppins/Poppins-ExtraLight.ttf",
      "Poppins ExtraLightItalic":"/fonts/poppins/Poppins-ExtraLightItalic.ttf",
      "Poppins Italic":"/fonts/poppins/Poppins-Italic.ttf",
      "Poppins Light":"/fonts/poppins/Poppins-Light.ttf",
      "Poppins LightItalic":"/fonts/poppins/Poppins-LightItalic.ttf",
      "Poppins Medium":"/fonts/poppins/Poppins-Medium.ttf",
      "Poppins MediumItalic":"/fonts/poppins/Poppins-MediumItalic.ttf",
      "Poppins Regular":"/fonts/poppins/Poppins-Regular.ttf",
      "Poppins SemiBold":"/fonts/poppins/Poppins-SemiBold.ttf",
      "Poppins SemiBoldItalic":"/fonts/poppins/Poppins-SemiBoldItalic.ttf",
      "Poppins Thin":"/fonts/poppins/Poppins-Thin.ttf",
      "ChauPhilomeneOne Regular":"fonts/ChauPhilomeneOne/ChauPhilomeneOne-Regular.ttf",
      "ChauPhilomeneOne Italic":"fonts/ChauPhilomeneOne/ChauPhilomeneOne-Italic.ttf",
    }



  page.on_route_change = route_change
  print("")
  #print("estoy justo iniciando la ejecución")
  print("Después de definir page.on_route_change")

  # | - - - The methods for first run - - - |
  # obtain the local json write
  def get_local_storage(key):
    try:
        if os.path.exists("local_storage.json"):
            with open("local_storage.json", "r") as f:
                data = json.load(f)
                return data.get(key)
    except Exception as e:
        print(f"Error reading local_storage.json: {e}")
    return None

  print("Después de definir get_local_storage")

  #if not set the json local
  def set_local_storage(key, value):
    data = {}
    try:
        if os.path.exists("local_storage.json"):
            with open("local_storage.json", "r") as f:
                data = json.load(f)
        data[key] = value
        with open("local_storage.json", "w") as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Error writing to local_storage.json: {e}")
  
  print("Después de definir set_local_storage")

  # if the first run
  def is_first_run():
    # Verificar si el archivo local_storage.json ya existe y si first_run está marcado como True
    try:
        if os.path.exists("local_storage.json"):
            with open("local_storage.json", "r") as f:
                data = json.load(f)
                return data.get("first_run", True)
    except Exception as e:
        print(f"Error reading local_storage.json: {e}")
    return True

  print("Después de definir is_first_run")
  
  # if the user logged_in
  def is_user_logged_in():
    print("parece ser que estoy en logged_in")
    token = myPyrebase.check_token()
    print("ya revise el token")
    #token = get_local_storage("firebase_token")
    if token:
        print("el token existe lo que quiere decir que ya se habia logueado antes")
        return True
    print("no existe conexion actual - - - ")
    return False
  
  print("Después de definir is_user_logged_in")
  

  # # And the tree logic its this if ROOT MAIN . 
  # if is_first_run():
  #   set_local_storage("first_run", False) # Marcar como False después del primer arranque
  #   page.go('/onboarding') # going to onboarding_screens ->
  #   print("Es la primer ejecución del programa!. . .")
  # elif is_user_logged_in():
  #   page.go('/home') # going to func on pyrebase to homescreen
  #   print("El token es valido, usted ya estaba logueada!. . .")
  # else:
  #   page.go('/')
  #   print("El programa ya se habia ejecutado con anterioridad!. . .")

  page.go('/onboarding')
  print("Después de la lógica principal")

  
  # obsolet
  # -> page.go('/onboarding') # going to onboarding_screens ->
  #page.go('/') # skip to logged_out
  # page.go('/login')
  # page.go('/profile')


app(target=main, port=8000, assets_dir="assets")
print("Después de iniciar la aplicación")