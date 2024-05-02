from flet import *
from utils.selectable_container import SelectableContainer
from utils import back
from utils.extras import *

class SignupScreen(UserControl):
  def __init__(self, page: Page):
    super().__init__()
    self.page = page

    page.title = "SignIn Authentication" #Title Page
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
      tight=20,
      #vertical_alignment=CrossAxisAlignment.START,
      horizontal_alignment=CrossAxisAlignment.CENTER,
      #alignment=MainAxisAlignment.SPACE_BETWEEN,
      alignment=MainAxisAlignment.START,
      controls=[
        SafeArea(
          minimum = None,          
          content=Column(
            alignment=MainAxisAlignment.START,
            expand=True,
            spacing=0,
            controls=[
              Column(
              #margin=margin.only(top=-20,left=-20,right=-20),
              horizontal_alignment=CrossAxisAlignment.CENTER, # Text on top boarding      
              alignment=MainAxisAlignment.START,
                controls=[
                  #Divider(heig
                  # ht=25, color="transparent"),
                  Container(
                    Stack(
                      [
                        Container(
                          #top=20,
                          border=border.all(6, colors.YELLOW_600),
                          width=650,
                          height=1000,
                          bgcolor="transparent",
                        ),
                        Container(
                          alignment=alignment.top_center,
                          border=border.all(6, colors.YELLOW_600),
                          bgcolor="transparent",
                          width=650,
                          height=377,
                          content=Image(
                            src='assets/images/ON_signIn_flot_under_complet.png',
                            scale=1,
                            width='auto',
                            height='auto',
                          ),
                        ),
                        # Column(
                        #   controls=[
                        #     Container(
                        #       Stack(
                        #         [
                        #           Container(
                        #             width=40,
                        #             height=40,
                        #             left=30,
                        #             right=30,
                        #             alignment=alignment.center,
                        #             border=border.all(6,colors.LIGHT_BLUE_ACCENT_400)
                        #           ),
                        #         ]
                        #       ),
                        #       width=400,
                        #       height=400,
                        #     )
                        #   ]
                        # ),
                        Container(
                          #alignment=alignment.bottom_left,
                           #fit='PASS_THROUGH',
                          # bgcolor="transparent",
                          # width=650,
                          #alignment=alignment.top_center,
                          #margin=margin.only(top=340),
                          bgcolor="#CCe9e9e9",
                          height=44,
                          width=343,
                          left=30,
                          right=30,
                          border=border.all(color='#1A000000',width=0.5,),
                          border_radius=5,
                          content=TextField(
                            border=InputBorder.NONE,
                            color='#C4A6A6',
                            height=40,
                            width=300,
                            hint_text='Username',
                            hint_style=TextStyle(
                              color='#33000000',
                              font_family='SF Pro Regula',
                            ),
                          ),
                        ),
                        # Container(
                        #   border=border.all(6, colors.RED_600),
                        #   alignment=alignment.top_center,
                        #   #padding=padding.only(top=-5,bottom=-30),
                        #   bgcolor="transparent",
                        #   width=650,
                        #   height=377,
                        #   #margin=margin.only(top=150),
                        #   content=Image(
                        #     src='assets/images/ON_signIn_flot_under.png',
                        #     scale=1,
                        #     width='auto',
                        #     height='auto',
                        #   ),
                        # ),
                        # Container(
                        #   alignment=alignment.top_center,
                        #   #border_radius.only(top=20),
                        #   border_radius= border_radius.only(top_left=40,top_right=40),
                        #   width=600,
                        #   height=400,
                        #   #bgcolor=input_fill_color,s
                        #   bgcolor="#f23fff",
                        #   top=260,
                        # ),
                      ],
                      #top=0,
                    ),
                    width=600,
                    alignment=alignment.top_center,
                    #image_src='assets/images/solid_basecolor.png',
                    #margin=margin.only(top=-20,left=-20,right=-20),
                    border=border.all(6, colors.RED_600),
                    ),
                #   Divider(height=25, color="transparent"),
                #   Container(
                #     content=Row(
                #       controls=[
                #         Container(
                #           bgcolor="transparent",
                #           width=450,
                #           height=300,
                #           content=Text(
                #             '¡Bienvenido!',
                #             font_family="Poppins Bold",
                #             size=18,
                #             color=base_color,
                #             #text_align='START',
                #             text_align=TextAlign.LEFT,
                #           )
                #         )
                #       ]
                #     )
                #   ),
                #   Container(
                #   alignment=alignment.center,
                #   padding=padding.only(bottom=6),
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
            ]
          )
        ) 
      ]
    )