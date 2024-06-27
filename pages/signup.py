from flet import *
from utils.selectable_container import SelectableContainer
from utils import back
from utils.extras import *
import re

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

  def create_text(size=10, weight=200, font_family='Poppins Bold', text_align='left', bgcolor='transparent', color='transparent'):
    return Text(
        '',
        size=size,
        weight=weight,
        font_family=font_family,
        text_align=text_align,
        bgcolor=bgcolor,
        color=color,
    )
  
  #Create the Text()
  tM = create_text()
  tm = create_text()
  tN = create_text()
  tC = create_text()
  nC = create_text()

  tMail = create_text()
  tUser = create_text()
  validpass = create_text()

  containerofocult = Container(
    content=Column(
      controls=[
        Container(
          content=tm,
        ),
        Container(
          content=tN,
        ),
        Container(
          content=tC,
        ),
        Container(
          content=nC,
        ),
      ],
    ),
  )
  txtpass = "--"
  form1 = form2 = form3 = form4 = "False"
  validform = "False"

  tM.visible = tm.visible = tN.visible = tC.visible = nC.visible = False
  containerofocult.visible = False

  #Def form to the password has changed
  def textbox_changed(self,e):

    global txtpass #for valid pass
    txtpass = e.control.value

    #If blank 
    has_spaces = any(c.isspace() for c in e.control.value)
    if e.control.value != "" and not has_spaces:
       
      mayusculas = len([c for c in e.control.value if c.isupper()])
      minusculas = len([c for c in e.control.value if c.islower()])
      numeros = len([c for c in e.control.value if c.isdigit()])
      has_special_chars = any(not c.isalnum() and not c.isspace() for c in e.control.value)
      
      #self.tM.value = self.tm.value = self.tN.value = self.tC.value = self.nC.value = ""
      self.tC.color = self.tN.color = self.tm.color = self.tM.color = self.nC.color = foreground_color
      self.tM.visible = self.tm.visible = self.tN.visible = self.tC.visible = self.nC.visible = self.containerofocult.visible = True
      self.nC.value = "❌ Número de caracteres."
      self.tM.value = "❌ Mayusculas."
      self.tm.value = "❌ Minusculas."
      self.tN.value = "❌ Numeros."
      self.tC.value = "❌ Caracteres Especiales."

      if len(e.control.value) > 7:
        self.nC.value = "✅ Número de caracteres."
      if mayusculas > 0:
         self.tM.value = "✅ Mayusculas."
      if minusculas > 0:
         self.tm.value = "✅ Minusculas."
      if numeros > 0:
         self.tN.value = "✅ Numeros."
      if has_special_chars:
        self.tC.value = "✅ Caracteres Especiales."
    elif has_spaces: #Intro blank spaces
      self.tM.color = foreground_color_error
      self.tM.value = "¡❌ No puedes introducir  espacios!."
      self.tm.value = self.tN.value = self.tC.value = self.nC.value = ""
    else:
      self.tM.color = foreground_color_error
      self.tM.value = "➖ ¡Campo vacio!."
      self.tm.value = self.tN.value = self.tC.value = self.nC.value = ""
    self.update()

  def textbox_shadow(self,e):
    global form3

    has_spaces = any(c.isspace() for c in e.control.value)
    mayusculas = len([c for c in e.control.value if c.isupper()])
    minusculas = len([c for c in e.control.value if c.islower()])
    numeros = len([c for c in e.control.value if c.isdigit()])
    has_special_chars = any(not c.isalnum() and not c.isspace() for c in e.control.value)

    self.tm.value = self.tN.value = self.tC.value = self.nC.value = ""
    self.tm.visible = self.tN.visible = self.tC.visible = self.nC.visible = self.containerofocult.visible = False
    self.tM.visible = True

    if mayusculas < 0 or minusculas < 0 or numeros < 0 or not has_special_chars or has_spaces:
      
      self.tM.color = foreground_color_error
      self.tM.value = "❌ ¡No es una contraseña valida!."
    elif e.control.value == "":
      self.tM.color = foreground_color_error
      self.tM.value = "➖ ¡Campo vacio!."
    else:
      self.tM.color = foreground_color_check
      self.tM.value = "✅ Contraseña valida." 
      form1 = "True"
    self.update()

  #forUSNAME
  def textbox_changed_usname(self,e):
    has_spaces = any(c.isspace() for c in e.control.value)

    if e.control.value != "" and not has_spaces:
      if len(e.control.value) < 8:
        self.tUser.color = foreground_color_error
        self.tUser.value = "❌ ¡El número de caracteres no es mayor a 8!."
      else:
        self.tUser.color = foreground_color_check
        self.tUser.value = "✅ Usuario valido." 
    elif e.control.value == "":
      self.tUser.color = foreground_color_error
      self.tUser.value = "➖ ¡Campo vacio!."
    else:
      self.tUser.color = foreground_color_error
      self.tUser.value = "❌ ¡No puedes introducir  espacios!." 
    self.update()


  #forMAIL
  def textbox_changed_mail(self,e):
    has_spaces = any(c.isspace() for c in e.control.value)
    # pattern for valid mail
    patron = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'  

    if e.control.value != "" and not has_spaces:
      if not re.match(patron, e.control.value):
        self.tMail.color = foreground_color_error
        self.tMail.value = "❌ ¡No es un correo electrónico valido!."
      else:
        self.tMail.color = foreground_color_check
        self.tMail.value = "✅ Correo electrónico valido."
    elif e.control.value == "":
      self.tMail.color = foreground_color_error
      self.tMail.value = "➖ ¡Campo vacio!."
    else:
      self.tMail.color = foreground_color_error
      self.tMail.value = "❌ ¡No puedes introducir  espacios!." 
    self.update()

  
  # D E P R E C A T E D - - - 
  def textbox_shadow_mail(self,e):
    if e.control.value != "":
      self.tMail.value=""
    else:
      self.tMail.color = foreground_color_error
      self.tMail.value = "➖ ¡Campo vacio!."
    self.update()

  
  #Valid Mail
  def textbox_validpass(self,e):
    if e.control.value == txtpass and txtpass != "":
      self.validpass.color = foreground_color_check
      self.validpass.value = "✅ Correo electrónico verificado."
    elif e.control.value == "":
      self.validpass.color = foreground_color_error
      self.validpass.value = "➖ ¡Campo vacio!."
    else:
      self.validpass.color = foreground_color_error
      self.validpass.value = "❌ El correo electrónico no coincide."
    self.update()


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
                  #Template from SignUp
                  Container(
                    alignment=alignment.top_center,
                    #border=border.all(6, colors.BLUE_600),
                    bgcolor="transparent",
                    width=650,
                    height='auto',
                    content=Image(
                      src='assets/images/ON_signIn_flot_under_complet.png',
                      scale=1,
                      width='auto',
                      height='auto',
                    ),
                  ),
                  Divider(color='transparent',height=20),
                  #Create an Account
                  Container(
                    padding=padding.only(left=20, right=20),
                    width='auto', 
                    height='auto',
                    content=Text(
                      "¡Crea tu Cuenta!",
                      text_align=TextAlign.CENTER,
                      font_family='Poppins Bold',
                      size=37,
                      color=base_color,
                      overflow=TextOverflow.VISIBLE,
                    )
                  ),
                  Divider(color='transparent',height=11),

                  #TextField Username
                  Container(
                    alignment=alignment.center,
                    #margin=margin.only(top=340),
                    bgcolor='transparent',
                    height=75,
                    width=390,
                    padding=padding.only(left=25, right=25),
                    border_radius=5,
                    content=TextField(
                      label="Nombre de Usuario",
                      height=77,
                      width=390,
                      text_size=14,
                      color=base_color,
                      bgcolor=filled_color_bg,
                      cursor_color=base_color,
                      selection_color=hint_base_color_plus_text,
                      focused_bgcolor=filled_color_bg_plus,
                      #border=border.all(color=base_color,width=1),
                      focused_color=foreground_color,
                      focused_border_width=3,
                      filled=True,
                      focused_border_color=foreground_color,
                      
                      border=InputBorder.NONE,
                      multiline=False,
                      capitalization=TextCapitalization.CHARACTERS,
                      input_filter=InputFilter(allow=True, regex_string="[A-Z,a-z,0-9, ]", replacement_string=""),

                      #Events
                      on_focus=lambda e: self.textbox_changed_usname(e),
                      on_blur=lambda e: self.textbox_changed_usname(e),
                      on_change=lambda e: self.textbox_changed_usname(e),
                      
                      
                      text_style=TextStyle(
                        color=base_color,
                        size=16,
                        font_family='Poppins Bold'
                      ),

                      helper_text="8 caracteres como mínimo.",
                      helper_style=TextStyle(
                        color=hint_base_color,
                        size=8,
                        font_family='Poppins SemiBold'
                      ),

                      label_style=TextStyle(
                        color=hint_base_color,
                        size=14,
                        font_family='Poppins SemiBold'
                      ),
                      #border=InputBorder.NONE,
                      hint_text="Username",
                      hint_style=TextStyle(
                        color=hint_base_color,
                        size=14,
                        font_family='Poppins SemiBold'
                      ),
                    ),
                  ),
                  Container(
                    visible='True',
                    bgcolor='transparent',
                    alignment=alignment.center_left,
                    padding=padding.only(left=25,right=25,top=-15),
                    width='390', 
                    height='auto',
                    content=Column(
                      controls=[
                        Container(
                          content=self.tUser,
                        ),
                      ],
                    ),
                  ),
                  Divider(color='transparent',height=5.2),


                  #TextField Email
                  Container(
                    alignment=alignment.center,
                    #margin=margin.only(top=340),
                    bgcolor='transparent',
                    height=75,
                    width=390,
                    padding=padding.only(left=25, right=25),
                    border_radius=5,
                    content=TextField(
                      label="Correo Electrónico",
                      height=77,
                      width=390,
                      text_size=14,
                      color=base_color,
                      bgcolor=filled_color_bg,
                      cursor_color=base_color,
                      selection_color=hint_base_color_plus_text,
                      focused_bgcolor=filled_color_bg_plus,
                      #border=border.all(color=base_color,width=1),
                      focused_color=foreground_color,
                      focused_border_width=3,
                      filled=True,
                      focused_border_color=foreground_color,
                      
                      border=InputBorder.NONE,
                      multiline=False,
                      capitalization=TextCapitalization.NONE,
                      #input_filter=InputFilter(allow=True, regex_string="[A-Z,a-z,0-9,.,@]", replacement_string=""),

                      #Events
                      on_focus=lambda e: self.textbox_changed_mail(e),
                      on_blur=lambda e: self.textbox_changed_mail(e),
                      on_change=lambda e: self.textbox_changed_mail(e),

                      text_style=TextStyle(
                        color=base_color,
                        size=16,
                        font_family='Poppins Bold'
                      ),

                      label_style=TextStyle(
                        color=hint_base_color,
                        size=14,
                        font_family='Poppins SemiBold'
                      ),
                      #border=InputBorder.NONE,
                      hint_text="Email",
                      hint_style=TextStyle(
                        color=hint_base_color,
                        size=14,
                        font_family='Poppins SemiBold'
                      ),
                    ),
                  ),
                  Container(
                    visible='True',
                    bgcolor='transparent',
                    alignment=alignment.center_left,
                    padding=padding.only(left=25,right=25,top=-20),
                    width='390', 
                    height='auto',
                    content=Column(
                      controls=[
                        Container(
                          content=self.tMail,
                        ),
                      ],
                    ),
                  ),
                  Divider(color='transparent',height=3.5),


                  #TextField Password
                  Container(
                    alignment=alignment.center,
                    bgcolor='transparent',
                    height=75,
                    width=390,
                    padding=padding.only(left=25, right=25),
                    border_radius=5,
                    content=TextField(
                      label="Contraseña",
                      height=70,
                      width=390,
                      text_size=14,
                      color=base_color,
                      bgcolor=filled_color_bg,
                      cursor_color=base_color,
                      selection_color=hint_base_color_plus_text,
                      focused_bgcolor=filled_color_bg_plus,
                      #border=border.all(color=base_color,width=1),
                      focused_color=foreground_color,
                      focused_border_width=3,
                      filled=True,
                      focused_border_color=foreground_color,

                      #Events
                      on_focus=lambda e: self.textbox_changed(e),
                      on_change=lambda e: self.textbox_changed(e),
                      on_blur=lambda e: self.textbox_shadow(e),

                      password=True,
                      border=InputBorder.NONE,
                      multiline=False,
                      #input_filter=InputFilter(allow=True, regex_string="[A-Z,a-z,0-9,!,#,$,%,&,',(,),*,+,-,.,/,:,;,<,=,>,,?,@,\,^,_,`,{,|,},~]", replacement_string=""),

                      helper_text="8 caracteres como mínimo.",
                      helper_style=TextStyle(
                        color=hint_base_color,
                        size=8,
                        font_family='Poppins SemiBold'
                      ),

                      text_style=TextStyle(
                        color=base_color,
                        size=16,
                        font_family='Poppins Bold'
                      ),
                      can_reveal_password=True,
                      label_style=TextStyle(
                        color=hint_base_color,
                        size=14,
                        font_family='Poppins SemiBold'
                      ),
                      #border=InputBorder.NONE,
                      hint_text="Password",
                      hint_style=TextStyle(
                        color=hint_base_color,
                        size=14,
                        font_family='Poppins SemiBold'
                      ),
                    ),
                  ),
                  Container(
                      visible='True',
                      bgcolor='transparent',
                      alignment=alignment.top_left,
                      padding=padding.only(left=25,right=25,top=-5),
                      #margin=margin.only(bottom=-15),
                      width='390', 
                      content=self.tM,
                  ),
                  Container(
                    alignment=alignment.top_left,
                    padding=padding.only(left=25,right=25),
                    width='390',
                    content=self.containerofocult,
                  ),
                  
                  
                  #TextField verify Password
                  Container(
                    alignment=alignment.center,
                    bgcolor='transparent',
                    height=75,
                    width=390,
                    padding=padding.only(left=25, right=25),
                    border_radius=5,
                    content=TextField(
                      label="Verifica tu contraseña",
                      height=70,
                      width=390,
                      text_size=14,
                      color=base_color,
                      bgcolor=filled_color_bg,
                      cursor_color=base_color,
                      selection_color=hint_base_color_plus_text,
                      focused_bgcolor=filled_color_bg_plus,
                      #border=border.all(color=base_color,width=1),
                      focused_color=foreground_color,
                      focused_border_width=3,
                      filled=True,
                      focused_border_color=foreground_color,

                      #Events
                      on_focus=lambda e: self.textbox_validpass(e),
                      on_change=lambda e: self.textbox_validpass(e),
                      on_blur=lambda e: self.textbox_validpass(e),

                      password=True,
                      border=InputBorder.NONE,
                      multiline=False,
                      #input_filter=InputFilter(allow=True, regex_string="[A-Z,a-z,0-9,!,#,$,%,&,',(,),*,+,-,.,/,:,;,<,=,>,,?,@,\,^,_,`,{,|,},~]", replacement_string=""),

                      text_style=TextStyle(
                        color=base_color,
                        size=16,
                        font_family='Poppins Bold'
                      ),
                      can_reveal_password=True,
                      label_style=TextStyle(
                        color=hint_base_color,
                        size=14,
                        font_family='Poppins SemiBold'
                      ),
                      #border=InputBorder.NONE,
                      hint_text="Password",
                      hint_style=TextStyle(
                        color=hint_base_color,
                        size=14,
                        font_family='Poppins SemiBold'
                      ),
                    ),
                  ),


                  #for Valid Pass
                  Container(
                    visible='True',
                    bgcolor='transparent',
                    alignment=alignment.center_left,
                    padding=padding.only(left=25,right=25,top=-15),
                    width='390', 
                    height='auto',
                    content=Column(
                      controls=[
                        Container(
                          content=self.validpass,
                        ),
                      ],
                    ),
                  ),
                  Divider(color="transparent", height=2),
                  
                  #for Register
                  Container(
                    margin=margin.only(left=20, right=20), 
                    on_click=lambda e: self.go_to_signup(),
                    height=55,
                    width=450,
                    border_radius=25,
                    bgcolor=base_color,
                    alignment=alignment.center,
                    content= Text('Registrarse',
                    font_family='Poppins SemiBold',
                    size=14,
                    color='white',
                    text_align='center'
                    ),
                  ),
                  #Divider(height=100,color="#AFA232"),



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
              #image_src='assets/images/solid_basecolor.png',
              #margin=margin.only(top=-20,left=-20,right=-20),
              #border=border.all(6, colors.RED_600),
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