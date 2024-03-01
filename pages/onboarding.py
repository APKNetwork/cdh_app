from flet import *
# from utils.selectable_container import SelectableContainer
from utils.base import BasePage as BP
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
class OnboardingScreen(UserControl):
  def __init__(self, page: Page):
    super().__init__()
    self.page = page

    page.title = "Welcome to CryDiagnoHealth" #Title Page
    #page.window_width = base_width
    #page.window_height = base_height
    page.fonts = { #fonts
        "Poppins Bold":"fonts/poppins/Poppins-Bold.ttf",
        "Poppins SemiBold":"fonts/poppins/Poppins-SemiBold.ttf"
    }

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

  def switch_page(self):
    self.page.go('/secondOnboarding')
    back.back_ = '/'

  def build(self):
    print("deberia estar ahorita mismo en onboarding uno")
    return Column(
      controls=[
        BP(
          SafeArea( #returning to the initapp
            expand=True,
            content=Column(
              alignment="spaceBetween",
              spacing=0,
              controls=[
                 Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER, # Text on top boarding      
                    alignment=MainAxisAlignment.CENTER,
                    controls=[ 
                    Divider(height=0, color="transparent"),
                    #Text on top - - -
                    Row(
                      wrap=True, # Wrap to the over posit ion
                      run_spacing=-15, #Espacio de separacion al hacer WRAPPING
                      spacing=0, #Espacio entre Container
                      alignment=MainAxisAlignment.CENTER,
                      vertical_alignment=CrossAxisAlignment.CENTER, # Text on top boarding      
                        controls=[
                        Container(
                          #border=border.all(4x, colors.PINK_600),
                          content=Text(
                            value=" Bienvenido a ",
                            #text_align="left",
                            text_align=TextAlign.START,
                            font_family='Poppins Bold',
                            size=22,
                            max_lines=1,
                          )
                        ),
                        Container(
                          content=Image(
                            src='assets/icons/iconbear_left_base_three_shadow.png',
                            scale=1,
                            width=155,
                            fit=ImageFit.FILL,
                          ),
                        ),
                      ]
                    ),
                    #Image positions
                    Row(
                       width=500,
                       alignment=MainAxisAlignment.CENTER,
                       controls=[
                          Container(
                          expand=True,
                          #border=border.all(4, colors.PINK_600),
                          content=Image(
                              src='ass ets/images/recurso_2_forwh.png', #Picture one ob
                              scale=1.2,
                              #expand=True,
                          )
                        )
                       ]
                    ),
                    Container( #Generating lines dashed for scroll
                        #border=border.all(4, colors.GREEN_600),
                        padding=padding.only(),
                        height=40,
                        alignment=alignment.center,
                        #border=border.all(2, colors.GREEN_600),
                        content=onboarding_button, # The slider - - -
                    ),
                    Divider(height=15, color="transparent"),
                    Container(
                        Text(
                            value="Registra llantos de bebés con precisión.",
                            font_family='Poppins SemiBold',
                            #text_align=TextAlign.CENTER,
                            size=26,
                            text_align="center",
                        ),
                        height="auto",
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
                        height="auto",
                        #border=border.all(5, colors.BLUE_600),
                        alignment=alignment.top_center,
                        #border=border.all(4, colors.YELLOW_600),
                    ),
                    Divider(height=40, color="transparent"),
                  ],
                ),
                Row(
                  controls=[
                    Container(
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
                    padding=padding.only(left=25, right=25, top=10, bottom=10),
                    ),
                  ], alignment="endBetween",
                  #padding=padding.only(bottom=20,left=45,right=45),
                ), 
              ],
            ),
          )
        )
      ]
    )