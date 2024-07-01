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
class secondOnboardingScreen(Container):
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

    self.content = Column(
      controls=[
        SafeArea( #returning to the initapp
          #expand=True,
          content=Column(
            alignment="spaceBetween",
            spacing=0,
            controls=[
                Column(              
                  # - - wrap=True, # Wrap to the over posit ion
                  #run_spacing=-15, #Espacio de separacion al hacer WRAPPING
                  # - - spacing=0, #Espacio entre Container
                  horizontal_alignment=CrossAxisAlignment.CENTER, # Text on top boarding      
                  alignment=MainAxisAlignment.CENTER,
                  controls=[
                    Divider(height=0, color="transparent"),
                    #Text on top - - -
                    #Image positions 
                    Row(
                      width=480,
                      alignment=MainAxisAlignment.CENTER,
                      controls=[
                        Container(
                            expand=True,
                            content=Image(
                                src='/images/recurso_4_forwh.png', #Picture one ob
                                scale=1.1,
                            ),
                            padding=padding.only(top=-5),
                          )
                        ]
                    ),
                    Divider(height=4, color="transparent"),
                    Container( #Generating lines dashed for scroll
                        padding=padding.only(),
                        height=28,
                        alignment=alignment.top_center,
                        #border=border.all(2, colors.GREEN_600),
                        content=onboarding_button, # The slider - - -
                    ),
                    Divider(height=12, color="transparent"),
                    Container(
                        Text(
                            value="Detección temprana de posibles patologías.",
                            font_family='Poppins SemiBold',
                            #text_align=TextAlign.CENTER,
                            size=26,
                            text_align="center",
                        ),
                        padding=padding.only(top=-30),
                        margin=margin.only(left=20, right=20),
                        height="auto",
                        width=450,
                        alignment=alignment.bottom_center,
                        #border=border.all(4, colors.PURPLE_600),
                    ),
                    #Divider(height=5, color="transparent"),
                    Container(
                        Text(
                            value="Contribuye a un diagnóstico oportuno a tavés del análisis de los llantos del bebé.",
                            font_family='Poppins SemiBold',
                            #text_align=TextAlign.CENTER,
                            size=14,
                            text_align="center",
                        ),
                        height="auto",
                        margin=margin.only(left=20, right=20),
                        width=450,
                        alignment=alignment.top_center,
                        #border=border.all(4, colors.YELLOW_600),
                    ),
                    Divider(height=19, color="transparent"),
                    Row(
                      width=480,
                      height='auto',
                      alignment=MainAxisAlignment.CENTER,
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
                        margin=margin.only(left=20, right=20),
                        padding=padding.only(left=25, right=25, top=10, bottom=10),
                        ),
                      ],
                    #padding=padding.only(bottom=20,left=45,right=45),
                    ), 
                    Row(
                     height=40,
                     opacity=0,
                  )
                  ],
              ),
            ]
          )
        )
      ]   
    )

  def switch_page(self):
    self.page.go('/thirdOnboarding')
    back.back_ = '/'
