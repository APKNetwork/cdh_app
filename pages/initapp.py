from flet import *
from utils.colors import *
from utils.extras import *
from utils.onboarding import boarding_change

class Index(Container):
    def __init__(self, page: Page):
        super().__init__()

        page.title = "Welcome to CryDiagnoHealth" #Title Page
        page.fonts = { #fonts
            "Poppins Bold":"fonts/poppins/Poppins-Bold.ttf",
            "Poppins SemiBold":"fonts/poppins/Poppins-SemiBold.ttf"
        }
        #page.add(Image(src=f"/images/logo_wh_cdh_splash.png"))
        row = Row(wrap=True,scroll='always',expand=True)
        page.add(row)

        self.expand = True
        self.offset = transform.Offset(0,0,)

        
        self.main_content = Column(
            controls=[
                Container(
                    height=btn_height-10,
                    width=btn_width-150,
                    border_radius=25,
                    bgcolor=input_fill_color,
                    alignment=alignment.center,
                    content=Text(
                        value='Siguiente',
                        font_family='Poppins SemiBold',
                        size=15,
                        color=font_color,
                    )
                )
            ]
        )

        self.content = Container(
            height=base_height,
            width=base_width,
            bgcolor=base_color,
            border_radius=br,
            clip_behavior=ClipBehavior.ANTI_ALIAS,
            expand=True,
            content=Stack(
                controls=[
                    Container(
                        height=base_height,
                        width=base_width,
                        left=0,
                        top=-210,
                        content=Image(
                            src='assets/images/onboarding_4.png', #Picture one ob
                            scale=0.8,
                            width=100,
                            height=100,
                        )
                    ),
                    Container(
                        height=base_height,
                        width=base_width,
                        alignment=alignment.center,
                        padding=padding.only(top=30,left=10,right=10),
                        content=Column(
                            controls=[
                                Container(height=20),
                                Container( #Text on top boarding
                                    #border=border.all(4, colors.PINK_600),
                                    margin=margin.only(left=40),
                                    content=Text(
                                        value="¡Bienvenido a                                 !",
                                        font_family='Poppins Bold',
                                        text_align=TextAlign.CENTER,
                                        size=20,
                                    )
                                ),
                                Container( #onboarding 1
                                    #border=border.all(4, colors.BLUE_600),
                                    margin=margin.only(left= 165,top=-80), #Modificar cuando se pueda cambiar logo sin oso
                                    content=Image(
                                        src='assets/images/logo_whout_bear.png',
                                        scale=0.8,
                                        width=200,
                                    )
                                ),
                                Container( #Text onboarding
                                    border=border.all(4, colors.PINK_600),
                                    height=base_height-600,
                                    width=base_width,
                                    padding=padding.only(top=260,left=25,right=25),
                                    content=Column(
                                        controls=[
                                            Container( #Generating lines dashed for scroll
                                                alignment=alignment.center,
                                                border=border.all(2, colors.GREEN_600),
                                                content=onboarding_button,
                                            ),
                                            Container(
                                                alignment=alignment.center,
                                                height=70,
                                                border=border.all(4, colors.BLUE_600),
                                                padding=padding.only(left=50,right=50),
                                                content=Text(
                                                    value="Registra llantos de bebés con precisión.",
                                                    font_family='Poppins SemiBold',
                                                    text_align=TextAlign.CENTER,
                                                    size=20,
                                                    #max_lines=2,
                                                )
                                            ),
                                            Container( #Legend onboard
                                                alignment=alignment.center,
                                                margin=margin.only(top=-10),
                                                content=Text(
                                                    value="Detecta y graba de manera clara y precisa los sonidos para un análisis efectivo.",
                                                    font_family='Poppins SemiBold',
                                                    text_align=TextAlign.CENTER,
                                                    size=12,
                                                )
                                            )
                                        ]
                                    )
                                ),
                                Container( #Legend onboarding
                                    padding=20,
                                    alignment=alignment.center,
                                    content=self.main_content #going to main content

                                )
                            ]
                        )
                    )
                ]
            )
        )

onboarding_button = Row(
    alignment=alignment.center,
    scroll='auto',

)
for x in range(3):
    onboarding_button.controls.append(
        Container(
            bgcolor=selected_item, height=5, width=10, border_radius=3, alignment = alignment.center, padding= 15,
        )        
    )
        #self.bgcolor = deepurple