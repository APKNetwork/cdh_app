from flet import *
from utils import back
from utils.selectable_container import SelectableContainer
from utils.base import BasePage as BP

from flet import *
from utils.selectable_container import SelectableContainer
from utils import back
from utils.extras import *

class LoginScreen(UserControl):
  def __init__(self, page: Page):
    super().__init__()
    self.page = page

    page.title = "Inicia Sesión" #Title Page
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
            alignment="spaceBetween",
            spacing=0,
            controls=[
              Column(
              horizontal_alignment=CrossAxisAlignment.CENTER, # Text on top boarding      
              alignment=MainAxisAlignment.CENTER,
                controls=[
                  #Divider(height=25, color="transparent"),
                  Container(
                    Stack(
                        [
                         Container(
                          padding=padding.only(top=-5,bottom=-30),
                          bgcolor="transparent",
                          width=450,
                          height=300,
                          content=Image(
                            #src='assets/images/reg_flot_1_forwh.png',
                            src='assets/images/ON_Login_flot_under.png',
                            scale=1.2,
                            width=100,
                            height=100,
                          ),
                        ),
                      ]
                    ),
                    width=650,
                    height=377,
                    #bgcolor=base_color,
                    image_src='assets/images/ON_Login_flot.png',
                    #margin=margin.only(left=-20,right=-20,top=-20),
                  ),
                  Divider(height=25, color="transparent"),
                  Container(
                    content=Row(
                      controls=[
                        Container(
                          bgcolor="transparent",
                          width=450,
                          height=300,
                          content=Text(
                            '¡Bienvenido!',
                            font_family="Poppins Bold",
                            size=18,
                            color=base_color,
                            #text_align='START',
                            text_align=TextAlign.LEFT,
                          )
                        )
                      ]
                    )
                  ),
                  Container(
                  alignment=alignment.center,
                  padding=padding.only(bottom=6),
                  bgcolor="#CCe9e9e9",
                  height=44,
                  width=343,
                  border=border.all(color='#1A000000',width=0.5,),
                  border_radius=5,
                  content=TextField(
                    border=InputBorder.NONE,
                    color='#262626',
                    height=40,
                    width=300,
                    hint_text='Username',
                    hint_style=TextStyle(
                      color='#33000000',
                      font_family='SF Pro Regula',
                    ),
                  )
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
            ]
          )
        ) 
      ]
    )
# class LoginScreen(UserControl):
#   def __init__(self, pg):
#     super().__init__()
#     self.pg = pg
#     self.login_button = Container(
#                 on_click=lambda e: self.switch_page(),
#                 height=44,
#                 width=343,
#                 border_radius=5,
#                 # bgcolor='#3797EF',
#                 bgcolor='#803797EF',
#                 alignment=alignment.center,
#                 content= Text('Log in',
#                 color='white',
#                 font_family='SF Pro SemiBold',
#                 size=14,
#                 text_align='center'
#                 ),
#               )
#   def switch_page(self):
#     self.pg.go('/home')
#     back.back_ = '/login'
           
#   def enable_login(self,e):
#     val = e.control.value
#     if len(val) >= 8:
#       self.login_button.bgcolor = '#3797EF'
#       # self.login_button.on_click=lambda e: self.switch_page(),
#       # self.login_button.on_click= self.switch_page,
#       self.login_button.update()
#     else:  
#       # self.login_button.on_click = None
#       self.login_button.bgcolor = '#803797EF'
#       self.login_button.update()

#   def build(self):
#     return Column(
#       controls=[
#         BP(
#           content=Column(
#             spacing=0,

#             # alignment=MainAxisAlignment.CENTER,
#             horizontal_alignment='center',
#             controls=[
#               Container(padding=padding.only(left=18,top=25),
#                 content=Row(
#                   controls=[
#                     Container(
#                       on_click=lambda _: self.page.go(back.back_),
#                       content=Image(
#                         src='assets/icons/back.png'
#                       )
#                     )
#                   ]
#                 )
#               ),
#               Container(
#                 height=120
#               ),
#               Image(
#                 src='assets/images/logo.png',
#                 # scale=0.5
#                 width=200
#               ),
#               Container(
#                 height=45
#               ),
#               Container(
#                 alignment=alignment.center,
#                 padding=padding.only(
#                   # left=20,
#                   # right=20,
#                   bottom=6),
#                 bgcolor="#CCe9e9e9",
#                 height=44,
#                 width=343,
#                 border=border.all(color='#1A000000',width=0.5,),
#                 border_radius=5,
#                 content=TextField(
#                   border=InputBorder.NONE,
#                   color='#262626',
#                   height=40,
#                   width=300,
#                   hint_text='Username',
#                   hint_style=TextStyle(
#                     color='#33000000',
#                     font_family='SF Pro Regula',
                    
#                   ),
                
#                 )
#               ),
#               Container(
#                 height=10
#               ),
#               Container(
#                 alignment=alignment.center,
#                 padding=padding.only(
#                   left=0,
#                   # right=20,
#                   bottom=6),
#                 bgcolor="#CCe9e9e9",
#                 height=44,
#                 width=343,
#                 border=border.all(color='#1A000000',width=0.5,),
#                 border_radius=5,
#                 content=TextField(
#                   password=True,
#                   # can_reveal_password=True,
#                   on_change=self.enable_login,
#                   border=InputBorder.NONE,
#                   color='#262626',
#                   height=40,
#                   width=300,
#                   hint_text='Password',
#                   hint_style=TextStyle(
#                     color='#33000000',
#                     font_family='SF Pro Regula',
               
#                   ),
                
#                 )
#               ),
#               Container(
#                 height=18
#               ),
#               Row(
#                 width=345,
#                 alignment='end',
#                 controls=[
#                   Container(
#                     on_click=lambda _: print('forgot password'),
#                     content=Text("Forgot password?",
#                       color='#3797EF',
#                       font_family='SF Pro Medium',
#                       size=12,
#                       weight='w600',
#               ),
#                   )
#                 ]
#               ),
#               Container(
#                 height=30
#               ),
              
#               self.login_button,
#               Container(
#                 height=30,
#               ),
#               Row(
#                 alignment='center',
#                 controls=[
#                   Image(
#                     src='/assets/images/fb.png',
#                   ),

#                   Container(
#                     on_click=lambda _: self.pg.go('/login'),
#                     content=Text('Log in with Facebook',
#                     color='#3797EF',
#                     font_family='SF Pro SemiBold',
#                     size=14,
#                     text_align='center'
#                     ),),
#                    ]
#                   ),

#               Container(height=40),
#               Container(
#                 padding=padding.symmetric(horizontal=20),  
#                 content = Row(
#                 alignment='spaceBetween',
#                 controls=[
#                   Container(height=0.1,width=132,bgcolor='#000000'),
#                   Text('OR',color='#66000000',size=12,font_family='SF Pro Semibold',weight=FontWeight.W_600),
#                   Container(height=0.1,width=132,bgcolor='#000000'),
#                 ]
#               ),
#               ),
#               Container(height=35),
#               Row(
#                   spacing=0,
#                   alignment='center',
#                   controls=[
#                     Text("Don't have an account?",
#                       color='#000000',
#                       font_family='SF Pro SemiBold',
#                       size=14,
#                       text_align='center',
#                       opacity=0.4
#                       ),Container(
#                           width=6
#                         ),
#                     Container(
#                       on_click = lambda _: self.pg.go('/signup'),
#                       content=Text("Sign up.",
#                       color='#3797EF',
#                       font_family='SF Pro Regular',
#                       size=14,
#                       text_align='center',
#                       ),
#                     )
#                   ]
#                 ),


#               Container(height=100),
#               Divider(thickness=0.2),
#               Container(height=10),

#                 Row(
#                   spacing=0,
#                   alignment='center',
#                   controls=[
#                     Text("Instagram from Meta",
#                       color='black',
#                       font_family='SF Pro SemiBold',
#                       size=12,
#                       text_align='center',
#                       opacity=0.4
#                       )
#                   ]
#                 ),
              

#             ]
#           )
#         )
#       ]
#     )