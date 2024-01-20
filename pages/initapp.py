from flet import *
from utils.colors import *
from utils.extras import *
from utils.onboarding import boarding_change

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

# Define a onboarding page...
class LandingPage(View):
    def __init__(self, page: Page):
        super().__init__(route="/landing", padding=35)

        self.page = page

        page.title = "Welcome to CryDiagnoHealth" #Title Page
        # Define a var for lock icon
        self.lock = Icon(name="lock", scale=Scale(4))

        # Define a button to route to profile
        self.button = Container(
            border_radius=25,
            expand=True,
            bgcolor=base_color,
            content=Text("Siguiente", color=input_fill_color, size=15, font_family='Poppins SemiBold'),
            padding=padding.only(left=25, right=25, top=10, bottom=10),
            alignment=alignment.center,
            on_click=lambda _: page.go("/secondOnboarding"),
        )

        #print("Hola, imprimo pero si muestro paso")
        # Define the list of controls for this view
        self.controls = [
            SafeArea(
                expand=True,
                bottom=False,
                
                content=Column(
                    alignment="spaceBetween",
                    controls=[
                        Column(
                            alignment="spaceBetween",
                            controls=[
                                Divider(height=10, color="transparent"),
                                #Text on top - - -
                                Container( # Text on top boarding      
                                    alignment=alignment.center,
                                    padding=padding.only(left=-38),
                                    #wrap=True,                          
                                    # border=border.all(4, colors.PINK_600),
                                    content=Row(
                                        alignment="center",
                                        wrap=True, # Wrap to the over position
                                        spacing=60,
                                        controls=[
                                            Text(
                                                value="Bienvenido a  ",
                                                #text_align="left",
                                                text_align=TextAlign.START,
                                                font_family='Poppins Bold',
                                                size=22,
                                                max_lines=1,
                                            ),
                                            Image(
                                                src='assets/icons/iconbear_left_base.png',
                                                scale=2.2,
                                                width=100,
                                                fit=ImageFit.FILL,
                                            ),
                                        ]
                                    )
                                ),
                                
                                #Image positions
                                Container(
                                    # border=border.all(4, colors.BLUE_600),
                                    bgcolor="transparent",
                                    width=400,
                                    height=400,
                                    padding=padding.only(top=-50),
                                    #self.lock
                                    content=Image(
                                        src='assets/images/recurso_2.png', #Picture one ob
                                        scale=1.2,
                                        width=100,
                                        height=100,
                                    )
                                ),

                                Divider(height=0, color="transparent"),
                                Container( #Generating lines dashed for scroll
                                    # border=border.all(4, colors.GREEN_600),
                                    padding=padding.only(top=-70),
                                    alignment=alignment.center,
                                    #border=border.all(2, colors.GREEN_600),
                                    content=onboarding_button, # The slider - - -
                                ),
                                Text(
                                    value="Registra llantos de bebés con precisión.",
                                    font_family='Poppins SemiBold',
                                    #text_align=TextAlign.CENTER,
                                    size=26,
                                    max_lines=2,
                                    text_align="center",
                                ),
                                Divider(height=5, color="transparent"),
                                Text(
                                    value="Detecta y graba de manera clara y precisa los sonidos para un análisis efectivo.",
                                    font_family='Poppins SemiBold',
                                    #text_align=TextAlign.CENTER,
                                    size=14,
                                    text_align="center",
                                ),
                            ],
                            horizontal_alignment="center",
                        ),
                        Row(controls=[self.button], alignment="spaceBetween"),
                    ],
                ),
            )
        ]


# Define a second onboarding page...
class SecondPage(View):
    def __init__(self, page: Page):
        super().__init__(route="/secondOnboarding", padding=35)

        self.page = page
        page.update()

        page.title = "Welcome to CryDiagnoHealth" #Title Page
        # Define a var for lock icon
        self.lock = Icon(name="lock", scale=Scale(4))

        # Define a button to route to profile
        self.button = Container(
            border_radius=25,
            expand=True,
            bgcolor=base_color,
            content=Text("Siguiente", color=input_fill_color, size=15, font_family='Poppins SemiBold'),
            padding=padding.only(left=25, right=25, top=10, bottom=10),
            alignment=alignment.center,
            on_click=lambda _: page.go("/thirdOnboarding"),
        )

        #print("Hola, imprimo pero si muestro paso")
        # Define the list of controls for this view
        self.controls = [
            SafeArea(
                expand=True,
                bottom=False,
                
                content=Column(
                    alignment="spaceBetween",
                    controls=[
                        Column(
                            alignment="spaceBetween",
                            controls=[
                                Divider(height=20, color="transparent"),
                                
                                #Image positions
                                Container(
                                    bgcolor="transparent",
                                    width=400,
                                    height=400,
                                    padding=padding.only(top=-50),
                                    #self.lock
                                    content=Image(
                                        src='assets/images/recurso_4.png', #Picture one ob
                                        scale=1.2,
                                        width=100,
                                        height=100,
                                    )
                                ),

                                Divider(height=40, color="transparent"),
                                Container( #Generating lines dashed for scroll
                                    padding=padding.only(top=-70),
                                    alignment=alignment.center,
                                    #border=border.all(2, colors.GREEN_600),
                                    content=onboarding_button, # The slider - - -
                                ),
                                Text(
                                    value="Detección temprana de posibles patologías.",
                                    font_family='Poppins SemiBold',
                                    #text_align=TextAlign.CENTER,
                                    size=26,
                                    max_lines=2,
                                    text_align="center",
                                ),
                                Divider(height=5, color="transparent"),
                                Text(
                                    value="Contribuye a un diagnóstico oportuno a tavés del análisis de los llantos del bebé.",
                                    font_family='Poppins SemiBold',
                                    #text_align=TextAlign.CENTER,
                                    size=14,
                                    text_align="center",
                                ),
                            ],
                            horizontal_alignment="center",
                        ),
                        Row(controls=[self.button], alignment="spaceBetween"),
                    ],
                ),
            )
        ]


# Define a third onboarding page...
class ThirdPage(View):
    def __init__(self, page: Page):
        super().__init__(route="/thirdOnboarding", padding=35)

        self.page = page

        global onpage
        onpage = 1
        page.update()

        page.title = "Welcome to CryDiagnoHealth" #Title Page
        # Define a var for lock icon
        self.lock = Icon(name="lock", scale=Scale(4))

        # Define a button to route to profile
        self.button = Container(
            border_radius=25,
            expand=True,
            bgcolor=base_color,
            content=Text("¡Vamos!", color=input_fill_color, size=15, font_family='Poppins SemiBold'),
            padding=padding.only(left=25, right=25, top=10, bottom=10),
            alignment=alignment.center,
            on_click=lambda _: page.go("/profile"), # GO TO THE LOGIN METHOD
        )

        #print("Hola, imprimo pero si muestro paso")
        # Define the list of controls for this view
        self.controls = [
            SafeArea(
                expand=True,
                bottom=False,
                
                content=Column(
                    alignment="spaceBetween",
                    controls=[
                        Column(
                            alignment="spaceBetween",
                            controls=[
                                Divider(height=20, color="transparent"),
                                
                                #Image positions
                                Container(
                                    bgcolor="transparent",
                                    width=400,
                                    height=400,
                                    padding=padding.only(top=-50),
                                    #self.lock
                                    content=Image(
                                        src='assets/images/may_menu_1.png', #Picture one ob
                                        scale=1.2,
                                        width=100,
                                        height=100,
                                    )
                                ),

                                Divider(height=30, color="transparent"),
                                Container( #Generating lines dashed for scroll
                                    padding=padding.only(top=-70),
                                    alignment=alignment.center,
                                    #border=border.all(2, colors.GREEN_600),
                                    content=onboarding_button, # The slider - - -
                                ),
                                Text(
                                    value="Navegación sencilla y amigable.",
                                    font_family='Poppins SemiBold',
                                    #text_align=TextAlign.CENTER,
                                    size=26,
                                    max_lines=2,
                                    text_align="center",
                                ),
                                Divider(height=5, color="transparent"),
                                Text(
                                    value="Una interfaz fácil de usar que te guiará paso a paso en la detección y diagnóstico.",
                                    font_family='Poppins SemiBold',
                                    #text_align=TextAlign.CENTER,
                                    size=14,
                                    text_align="center",
                                ),
                            ],
                            horizontal_alignment="center",
                        ),
                        Row(controls=[self.button], alignment="spaceBetween"),
                    ],
                ),
            )
        ]


def main(page: Page):
    # Define page related settings
    page.theme_mode = ThemeMode.LIGHT
    page.title = "Welcome to CryDiagnoHealth" #Title Page
    page.fonts = { #fonts
        "Poppins Bold":"fonts/poppins/Poppins-Bold.ttf",
        "Poppins SemiBold":"fonts/poppins/Poppins-SemiBold.ttf"
    }

    onpage = 0

    # Define a method to handle page routing
    def router(route):
        page.views.clear()
        onboarding_button.controls.clear()

        if page.route == "/landing":
            landing = LandingPage(page)
            page.views.append(landing)
            onpage = 0 #for print correct variable

        if page.route == "/secondOnboarding":
            secondOnboarding = SecondPage(page)
            page.views.append(secondOnboarding)
            onpage = 1

        if page.route == "/thirdOnboarding":
            thirdOnboarding = ThirdPage(page)
            page.views.append(thirdOnboarding)
            onpage = 2

        for x in range(3):
            if x == onpage:
                onboarding_button.controls.append(
                    Container(
                        bgcolor=base_color,
                        height=8,
                        width=20,
                        border_radius=10,
                        alignment = alignment.center,
                        padding= 15,
                        on_click=lambda e,i=x:changepage()
                    )        
                )
            else:
                onboarding_button.controls.append(
                    Container(
                        bgcolor=unselected_item,
                        height=8,
                        width=35,
                        border_radius=10,
                        alignment = alignment.center,
                        padding= 15,
                        on_click=lambda e,i=x:changepage()
                    )        
                )

        page.update()

    page.on_route_change = router
    page.go("/landing")

app(target=main, assets_dir="assets")