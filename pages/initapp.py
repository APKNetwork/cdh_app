from flet import *
from utils.colors import *
from utils.extras import *
from utils.onboarding import boarding_change

class Index(Container):
    def __init__(self, page: Page):
        super().__init__()

        page.title = "Welcome to CryDiagnoHealth" #Title Page
        page.fonts = { #fonts
            "Poppins Bold":"fonts/poppins/Poppins-Bold.ttf"
        }
        #page.add(Image(src=f"/images/logo_wh_cdh_splash.png"))
        row = Row(wrap=True,scroll='always',expand=True)
        page.add(row)

        self.expand = True
        self.offset = transform.Offset(0,0,)
        self.content = Container(
            height=base_height,
            width=base_width,
            bgcolor=base_color,
            border_radius=br,
            clip_behavior=ClipBehavior.ANTI_ALIAS,
            expand=True,
            content=Stack(
                controls=[
                    Row(
                        Container(
                            height=base_height,
                            width=base_width,
                            left=10,
                            top=-200,
                            content=Image(
                                src='assets/images/onboarding_4.png',
                                scale=0.9,
                                width=100,
                                height=100,
                            )
                        ),
                        Container(
                            height=base_height,
                            width=base_width,
                            padding=padding.only(top=30,left=10,right=10),
                            content=Column(
                                controls=[
                                    Container(height=20),
                                    Container(
                                        margin=margin.only(left=20),
                                        content=Text(
                                            value="¡Bienvenido a                          !",
                                            font_family='Poppins Bold',
                                            size=20,
                                        )
                                    )
                                ]
                            )
                        ),
                        Container(
                            height=base_height,
                            width=base_width,
                            padding=padding.only(top=0,left=60,right=10),
                            content=Column(
                                controls=[
                                    Container(height=160),
                                    Container(
                                        margin=margin.only(left=60)
                                    )
                                ]
                            )
                        )
                    ),
                ]
            )
        )        
        #self.bgcolor = deepurple