from flet import *
from utils.selectable_container import SelectableContainer
from utils import back
from utils.extras import *

class HomeScreen(Container):
    def __init__(self, page: Page, myPyrebase):
        super().__init__(expand=True)  # Hacemos que el HomeScreen se expanda
        self.page = page

        page.title = "Graba con Cariño, Graba con Amor"  # Título de la página
        page.update()

        # page.fonts = { #fonts
        #   "Poppins Bold":"fonts/poppins/Poppins-Bold.ttf",
        #   "Poppins SemiBold":"fonts/poppins/Poppins-SemiBold.ttf",
        #   "ChauPhilomeneOne Regular":"fonts/ChauPhilomeneOne/ChauPhilomeneOne-Regular.ttf",
        #   "ChauPhilomeneOne Italic":"fonts/ChauPhilomeneOne/ChauPhilomeneOne-Italic.ttf"
        # }

        # Contenedor principal que se expande
        self.content = Container(
            SafeArea(
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER, # Text on top boarding      
                alignment=MainAxisAlignment.SPACE_EVENLY,
                #scroll=ScrollMode.ADAPTIVE,
                controls=[
                    Container(expand=1,content=Text("Header",font_family='ChauPhilomeneOne Regular',size=200),border=border.all(10,colors.GREY_900)),
                    Container(
                        expand=3,
                        border=border.all(10,colors.GREEN_900),
                        content=Column(
                            alignment=MainAxisAlignment.SPACE_EVENLY,
                            controls=[
                                TextButton(text="Botón 1", on_click=lambda e: print("Botón 1 clicado")),
                                TextButton(text="Botón 2", on_click=lambda e: print("Botón 2 clicado")),
                                TextButton(text="Botón 3", on_click=lambda e: print("Botón 3 clicado")),
                                TextButton(text="Botón 4", on_click=lambda e: print("Botón 4 clicado")),
                                TextButton(text="Botón 5", on_click=lambda e: print("Botón 5 clicado")),
                                TextButton(text="Botón 6", on_click=lambda e: print("Botón 6 clicado")),
                                TextButton(text="Botón 7", on_click=lambda e: print("Botón 7 clicado")),
                                TextButton(text="Botón 8", on_click=lambda e: print("Botón 8 clicado")),
                            ],
                        ),
                    ),
                    Container(expand=1, content=Text("Footer"),border=border.all(10,colors.BROWN_900)),
                ],
            )
          ),
          width=650,
        expand=True,  # Esto permitirá que el contenedor se expanda en altura según el dispositivo
        bgcolor=colors.BLUE_900,  # Color de fondo
        alignment=alignment.center,  # Alinear contenido al centro
        #padding=0,  # Eliminar padding
        margin=-10,
        )
