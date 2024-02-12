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
class secondOnboardingScreen(UserControl):
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

    #Selector to return or next a page onboarding
    onboarding_button.controls.clear() #cleaning input
    page.update()

    onboarding_button.controls.append(
      Container(
          bgcolor=unselected_item,
          height=8,
          width=35,
          border_radius=10,
          alignment = alignment.center,
          padding= 15,
          #on_click=lambda e,i=x:changepage()
          on_click=lambda _: self.page.go('/onboarding'),
      ),
    )
    
    onboarding_button.controls.append(
      Container(
          bgcolor=base_color,
          height=8,
          width=20,
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
    self.page.go('/thirdOnboarding')
    back.back_ = '/'

  def build(self):
    print("deberia estar ahorita mismo en onboarding 2")
    return Column(
      scroll=ScrollMode.HIDDEN,
      height=940,
      # expand=True,
      # alignment="end",
      controls=[
        BP(
          SafeArea( #returning to the initapp
            expand=True,
            #bottom=False,

            content=Column(
              alignment="spaceBetween",
              spacing=0,
              controls=[
                 Column(
                    alignment="SpaceBetween",
              
                    # alignment=MainAxisAlignment.CENTER,
                    #horizontal_alignment='center',
                    controls=[
                    Divider(height=20, color="transparent"),
                    #Text on top - - -
                    #Image positions
                    Container(
                        bgcolor="transparent",
                        width=420,
                        height=420,
                        padding=padding.only(),
                        #self.lock
                        content=Image(
                            src='assets/images/recurso_4_forwh.png', #Picture one ob
                            scale=1.2,
                            width=100,
                            height=100,
                        )
                    ),
                    Container( #Generating lines dashed for scroll
                        padding=padding.only(),
                        height=40,
                        alignment=alignment.center,
                        #border=border.all(2, colors.GREEN_600),
                        content=onboarding_button, # The slider - - -
                    ),
                    Divider(height=30, color="transparent"),
                    Container(
                        Text(
                            value="Detección temprana de posibles patologías.",
                            font_family='Poppins SemiBold',
                            #text_align=TextAlign.CENTER,
                            size=26,
                            max_lines=2,
                            text_align="center",
                        ),
                        height=90,
                        alignment=alignment.bottom_center,
                        #border=border.all(4, colors.PURPLE_600),
                    ),
                    Divider(height=5, color="transparent"),
                    Container(
                        Text(
                            value="Contribuye a un diagnóstico oportuno a tavés del análisis de los llantos del bebé.",
                            font_family='Poppins SemiBold',
                            #text_align=TextAlign.CENTER,
                            size=14,
                            text_align="center",
                        ),
                        height=60,
                        alignment=alignment.top_center,
                        #border=border.all(4, colors.YELLOW_600),
                    ),
                    Divider(height=70, color="transparent"),
                  ],
                  horizontal_alignment="center",
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