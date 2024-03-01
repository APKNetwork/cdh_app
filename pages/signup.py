from flet import *
from utils.selectable_container import SelectableContainer
from utils import back
from utils.extras import *

class SignupScreen(UserControl):
  def __init__(self, page: Page):
    super().__init__()
    self.page = page

    page.title = "Welcome to CryDiagnoHealth" #Title Page
    #page.window_width = base_width
    #page.window_height = base_height
    page.fonts = { #fonts
        "Poppins Bold":"fonts/poppins/Poppins-Bold.ttf",
        "Poppins SemiBold":"fonts/poppins/Poppins-SemiBold.ttf",
        "ChauPhilomeneOne Regular":"fonts/ChauPhilomeneOne/ChauPhilomeneOne-Regular.ttf",
        "ChauPhilomeneOne Italic":"fonts/ChauPhilomeneOne/ChauPhilomeneOne-Italic.ttf"
    } 


  # Main function - - - 
  def build(self):
    return Column(
      controls=[
        SafeArea(
          content=Column(
            spacing=0,
            auto_scroll=False,
            scroll=ScrollMode.HIDDEN,
            alignment="spaceBetween",

            # alignment=MainAxisAlignment.CENTER,
            horizontal_alignment='center',
            controls=[

              Text(
              " Fecha de la Última Actualización: [11 - 02 - 2024] .",
                font_family="Poppins Bold",
                size=14,
                bgcolor=base_color,
                color=input_fill_color,
              ),
              Divider(height=10,color="TRANSPARENT", thickness=1),
              Text(
                  text_align='JUSTIFY',
                  spans=[
                    TextSpan(
                      "Bienvenido/a a",
                      TextStyle(font_family="Poppins SemiBold"),                  
                      spans=[
                        TextSpan(
                        " CryDiagnoHealth ",
                        TextStyle(font_family="ChauPhilomeneOne Regular", size=18),
                        ),
                        TextSpan(
                          ", una aplicación móvil diseñada para ayudar en la detección temprana de enfermedades patológicas en bebés a través del análisis de grabaciones de llanto. Antes de continuar utilizando nuestra aplicación, te pedimos que leas detenidamente estos términos del servicio. Al acceder y utilizar nuestra aplicación, aceptas cumplir con estos términos. Si no estás de acuerdo con alguno de estos términos, te recomendamos que dejes de usar la aplicación de inmediato.",
                          TextStyle(font_family="Poppins SemiBold"),
                        ),
                      ],
                    )
                  ],
              ),

              Divider(height=25,color=base_color),
              Text(
                "1. Uso de la Aplicación:",
                  font_family="Poppins Bold",
                  size=16,
                ),
              Text(
                  text_align='JUSTIFY',
                  #theme_style=TextThemeStyle.BODY_SMALL,
                  spans=[
                  TextSpan(" "),
                  TextSpan(
                    "• La aplicación",
                    TextStyle(font_family="Poppins SemiBold"),
                  ),
                  TextSpan(
                    " CryDiagnoHealth ",
                    TextStyle(font_family="ChauPhilomeneOne Regular", size=18),
                  ),
                  TextSpan(
                    "está destinada únicamente para uso personal y no comercial. No está permitido utilizar la aplicación para ningún propósito ilegal o no autorizado.",
                    TextStyle(font_family="Poppins SemiBold"),
                  ),
                  ]
              ),

              # Container(padding=padding.only(left=18,top=25),
              #   content=Row(
              #     controls=[
              #       Container(
              #         content=Image(
              #           src='assets/icons/back.png'
              #         )
              #       )
              #     ]
              #   )
              # ),
              # Container(
              #   height=120
              # ),
              # Image(
              #   src='assets/images/logo.png',
              #   # scale=0.5
              #   width=200
              # ),
              # Container(
              #   height=45
              # ),
              # Container(
              #   alignment=alignment.center,
              #   padding=padding.only(
              #     # left=20,
              #     # right=20,
              #     bottom=6),
              #   bgcolor="#CCe9e9e9",
              #   height=44,
              #   width=343,
              #   border=border.all(color='#1A000000',width=0.5,),
              #   border_radius=5,
              #   content=TextField(
              #     border=InputBorder.NONE,
              #     color='#262626',
              #     height=40,
              #     width=300,
              #     hint_text='Username',
              #     hint_style=TextStyle(
              #       color='#33000000',
              #       font_family='SF Pro Regula',
              #     ),
                
              #   )
              # ),
              # Container(
              #   height=10
              # ),
              # Container(
              #   alignment=alignment.center,
              #   padding=padding.only(
              #     left=0,
              #     # right=20,
              #     bottom=6),
              #   bgcolor="#CCe9e9e9",
              #   height=44,
              #   width=343,
              #   border=border.all(color='#1A000000',width=0.5,),
              #   border_radius=5,
              #   content=TextField(
              #     border=InputBorder.NONE,
              #     color='#262626',
              #     height=40,
              #     width=300,
              #     hint_text='Password',
              #     hint_style=TextStyle(
              #       color='#33000000',
              #       font_family='SF Pro Regula',
              #     ),
                
              #   )
              # ),
              # Container(
              #   height=18
              # ),
              # Row(
              #   width=345,
              #   alignment='end',
              #   controls=[
              #     Container(
              #       on_click=lambda _: print('forgot password'),
              #       content=Text("Forgot password?",
              #         color='#3797EF',
              #         font_family='SF Pro Medium',
              #         size=12,
              #         weight='w600',
              # ),
              #     )
              #   ]
              # ),
              # Container(
              #   height=30
              # ),
              
              # Container(
              #   on_click=lambda _: self.page.go('/login'),
              #   height=44,
              #   width=343,
              #   border_radius=5,
              #   # bgcolor='#3797EF',
              #   bgcolor='#803797EF',
              #   alignment=alignment.center,
              #   content= Text('Log in',
              #   color='white',
              #   font_family='SF Pro SemiBold',
              #   size=14,
              #   text_align='center'
              #   ),
              # ),
              # Container(
              #   height=30,
              # ),
              # Row(
              #   alignment='center',
              #   controls=[
              #     Image(
              #       src='/assets/images/fb.png',
              #     ),

              #     Container(
              #       on_click=lambda _: self.pg.go('/login'),
              #       content=Text('Log in with Facebook',
              #       color='#3797EF',
              #       font_family='SF Pro SemiBold',
              #       size=14,
              #       text_align='center'
              #       ),),
              #      ]
              #     ),

              # Container(height=40),
              # Container(
              #   padding=padding.symmetric(horizontal=20),  
              #   content = Row(
              #   alignment='spaceBetween',
              #   controls=[
              #     Container(height=0.1,width=132,bgcolor='#000000'),
              #     Text('OR',color='#66000000',size=12,font_family='SF Pro Semibold',weight=FontWeight.W_600),
              #     Container(height=0.1,width=132,bgcolor='#000000'),
              #   ]
              # ),
              # ),
              # Container(height=35),
              # Row(
              #     spacing=0,
              #     alignment='center',
              #     controls=[
              #       Text("Don't have an account?",
              #         color='#000000',
              #         font_family='SF Pro SemiBold',
              #         size=14,
              #         text_align='center',
              #         opacity=0.4
              #         ),Container(
              #             width=6
              #           ),
              #       Container(
              #         on_click = lambda _: self.pg.go('/signup'),
              #         content=Text("Sign up.",
              #         color='#3797EF',
              #         font_family='SF Pro Regular',
              #         size=14,
              #         text_align='center',
              #         ),
              #       )
              #     ]
              #   ),


              # Container(height=100),
              # Divider(thickness=0.2),
              # Container(height=10),

              #   Row(
              #     spacing=0,
              #     alignment='center',
              #     controls=[
              #       Text("Instagram from Meta",
              #         color='black',
              #         font_family='SF Pro SemiBold',
              #         size=12,
              #         text_align='center',
              #         opacity=0.4
              #         )
              #     ]
              #   ),
            ]
          )
        ) 
      ]
    )