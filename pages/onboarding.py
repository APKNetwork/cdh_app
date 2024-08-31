from flet import *
# from utils.selectable_container import SelectableContainer
from utils import back
from utils.extras import *


# NON usable on - v
# Define a link style dict.
link_style = {
    "height": 50,
    "focused_border_color": base_color,
    "border_radius": 5,
    "cursor_height": 16,
    "cursor_color": "white",
    "content_padding": 10,
    "border_width": 1.5,
    "text_size": 14,
    "label_style": TextStyle(color=base_color),
}
# Define a link class...
class Link(TextField):
    def __init__(self, label: str, value: str, page: Page):
        super().__init__(
            value=value,
            read_only=True,
            label=label,
            on_focus=self.selected,
            **link_style,
        )

        self.page = page

    # Define a method to show snackbar for copied event
    def selected(self, event: TapEvent = None):
        self.page.snack_bar = SnackBar(
            Text(f"Copied {self.label}!"), show_close_icon=True, duration=2000
        )

        self.page.snack_bar.open = True
        self.page.update()

def changepage(e,i): #Def to the buttons apply
    #Clear all listdata
    pass

onboarding_button = Row( #Put the buttons separated
    alignment=alignment.center,
    scroll='auto',
)

# Main class to re-direction views
class OnboardingScreen(Container):
  def __init__(self, page: Page, myPyrebase):
    super().__init__(expand=True)
    self.page = page

    page.title = "Welcome to CryDiagnoHealth" #Title Page
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    print("pase a page update")
    page.update()
    # page.fonts = { #fonts
    #     "Poppins Bold":"/fonts/poppins/Poppins-Bold.ttf",
    #     "Poppins SemiBold":"/fonts/poppins/Poppins-SemiBold.ttf"
    # }

    # Detectar altura de la ventana para ajustar el layout
    screen_height = page.window.height
    #   - - -print("screen_height:",screen_height * 1.2)
    is_small_screen = screen_height * 1.2 < 600
    if not screen_height != 0:
       is_small_screen = False
    #   - - -print("is small screen",is_small_screen)
    
    # Ajustes condicionales
    column_alignment = MainAxisAlignment.SPACE_BETWEEN if not is_small_screen else MainAxisAlignment.START
    column_scroll_mode = ScrollMode.ALWAYS if is_small_screen else None
    #   - - -print("column_alig",column_alignment,"   and scrollmode",column_scroll_mode)
    
    #Selector to return a page onboarding
    onboarding_button.controls.clear() #cleaning input
    page.update()
    
    onboarding_button.controls.append(
      Container(
          bgcolor=base_color,
          height=8,
          width=20,
          border_radius=10,
          alignment = alignment.center,
          padding= 15,
          #on_click=lambda e,i=x:changepage()
          on_click=lambda _: self.page.go('/onboarding'),
      ),
    )
    
    onboarding_button.controls.append(
      Container(
          bgcolor=unselected_item,
          height=8,
          width=35,
          border_radius=10,
          alignment = alignment.center,
          padding= 15,
          on_click=lambda _: self.page.go('/secondOnboarding'),
      ),
    )

    onboarding_button.controls.append(
      Container(
          bgcolor=unselected_item,
          height=8,
          width=35,
          border_radius=10,
          alignment = alignment.center,
          padding= 15,
          on_click=lambda _: self.page.go('/thirdOnboarding'),
      )
    )
    page.update()

    self.content = Container(
        SafeArea( #returning to the initapp
          content=Column(
            horizontal_alignment=CrossAxisAlignment.CENTER, # Text on top boarding      
            #alignment=MainAxisAlignment.SPACE_BETWEEN,
            alignment=column_alignment, 
            scroll=column_scroll_mode, #depende el size activa o no
            #scroll=ScrollMode.ALWAYS,  # Habilitar scroll siempre
            controls=[
              Container(
                border=border.all(5,colors.RED_900),
                expand=0.25, #TOP 1 UNI
                content=Column(
                  alignment=MainAxisAlignment.SPACE_EVENLY,
                  horizontal_alignment=CrossAxisAlignment.CENTER,
                  controls=[ 
                  Divider(height=0, color="transparent"),
                  #Text on top - - -
                  Row(
                    wrap=True, # Wrap to the over posit ion
                    run_spacing=-15, #Espacio de separacion al hacer WRAPPING
                    spacing=0, #Espacio entre Container
                    alignment=MainAxisAlignment.CENTER,
                    #vertical_alignment=CrossAxisAlignment.CENTER, # Text on top boarding      
                      controls=[
                      Container(
                        #border=border.all(4x, colors.PINK_600),
                        content=Text(
                          value=" Bienvenido a ",
                          #text_align="left",
                          text_align=TextAlign.START,
                          font_family="Poppins Bold",
                          size=22,
                          max_lines=1,
                        )
                      ),
                      Container(
                        content=Image(
                          src='/icons/iconbear_left_base_three_shadow.png',
                          scale=1,
                          width=155,
                          fit=ImageFit.FILL,
                        ),
                      ),
                    ]
                  ),
                ],
              )
            ),
            Container(
              border=border.all(5,colors.YELLOW_900),
              expand=0.7, #IMAGE and DASHED BUTTONS 4 UNI
              content=Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[ 
                    #Image positions
                    Row(
                      width=450,
                      alignment=MainAxisAlignment.CENTER,
                      controls=[
                        Container(
                        expand=True,
                        #border=border.all(4, colors.PINK_600),
                        content=Image(
                            src='/images/recurso_2_forwh_1.png', #Picture one ob
                            scale=1,
                            #height=526,
                            #fit=ImageFit.FIT_WIDTH,
                            #expand=True,
                        ),
                        padding=padding.only(top=-20),
                      )
                      ]
                  ),
                  Divider(height=0, color="transparent"),
                  Container( #Generating lines dashed for scroll
                    #border=border.all(4, colors.GREEN_600),
                    padding=padding.only(),
                    height=28,
                    width=450,
                    alignment=alignment.top_center,
                    #border=border.all(2, colors.GREEN_600),
                    content=onboarding_button, # The slider - - -
                  ),
                ]
              )
            ),
            Container(
              border=border.all(5,colors.GREEN_900),
              expand=0.5, #TEXT 1 UNI
              content=Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[ 
                  Divider(height=0, color="transparent"),
                  Container(
                      Text(
                          value="Registra llantos de bebés con precisión.",
                          font_family='Poppins SemiBold',
                          #text_align=TextAlign.CENTER,
                          size=26,
                          text_align="center",
                      ),
                      #padding=padding.only(top=-30),
                      margin=margin.only(left=20, right=20),
                      height="auto",
                      width=450,
                      alignment=alignment.bottom_center,
                      #border=border.all(4, colors.PURPLE_600),
                  ),
                  #Divider(height=0, color="transparent"),
                  Container(
                      Text(
                          value="Detecta y graba de manera clara y precisa los sonidos para un análisis efectivo.",
                          font_family='Poppins SemiBold',
                          #text_align=TextAlign.CENTER,
                          size=14,
                          text_align="center",
                      ),
                      #padding=padding.only(top=-30),
                      margin=margin.only(left=20, right=20),
                      height="auto",
                      width=450,
                      #border=border.all(5, colors.BLUE_600),
                      alignment=alignment.top_center,
                      #border=border.all(4, colors.YELLOW_600),
                  ),   
                ]
              )
            ),
            Container(
              border=border.all(5,colors.PURPLE_900),
              expand=0.25, #BUTTON 1 UNI
              # horizontal_alignment=CrossAxisAlignment.CENTER, # Text on top boarding      
              # alignment=MainAxisAlignment.CENTER,
              content=Column(
                alignment=MainAxisAlignment.SPACE_EVENLY,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[ 
                  #Divider(height=15, color="transparent"),
                  Row(
                    width=480,
                    height='auto',
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                      Container(  
                        width=450,                 
                          on_click=lambda e: self.switch_page(),
                          border_radius=25,
                          expand=True,
                          bgcolor=base_color,
                          alignment=alignment.center,
                          content=Text('Siguiente',
                            color='white',
                            font_family='Poppins SemiBold',
                            size=15,
                            text_align='center'
                            ),
                          margin=margin.only(left=20, right=20),
                          padding=padding.only(left=25, right=25, top=10, bottom=10),
                          ),
                          #Divider(height=30, color="transparent"),
                      ],
                  ),
                  Divider(height=30, color="transparent"),
                ]
              )
            )
          ],
        ),
      ),
      width=650,
      expand=True,  # Esto permitirá que el contenedor se expanda en altura según el dispositivo
      alignment=alignment.center,  # Alinear contenido al centro
      #padding=0,  # Eliminar padding
      margin=-10,
    )


  def switch_page(self):
    self.page.go('/secondOnboarding')
    back.back_ = '/'

#print("estoy en onboarding 1")