from flet import *
from utils.selectable_container import SelectableContainer
from utils import back
from utils.extras import *
import re

txtpass = "-"
form0 = "False"
form1 = "False"
form2 = "False" 
form3 = "False"

# UIclase
class SignupScreen(Container):
  def __init__(self, page: Page, myPyrebase):
    super().__init__()
    self.page = page

    page.title = "SignIn Authentication" #Title Page
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.scroll = ScrollMode.ADAPTIVE
    page.update()

    page.fonts = { #fonts
        "Poppins Bold":"fonts/poppins/Poppins-Bold.ttf",
        "Poppins SemiBold":"fonts/poppins/Poppins-SemiBold.ttf",
        "ChauPhilomeneOne Regular":"fonts/ChauPhilomeneOne/ChauPhilomeneOne-Regular.ttf",
        "ChauPhilomeneOne Italic":"fonts/ChauPhilomeneOne/ChauPhilomeneOne-Italic.ttf"
    }

    # Set highlight and unhighlight of terms
    def signin_highlight_link(e):
      # For lighnight
      e.control.style.color = selected_item
      e.control.update()

    def signin_unhighlight_link(e):
      e.control.style.color = base_color
      e.control.update()

    self.content = Column(
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
                      src='/images/ON_signIn_flot_under_complet.png',
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
                      
                      #THE CAPITALIZATION NOT WORKING ON 0.24.0 - - -
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
                    height=85,
                    width=390,
                    padding=padding.only(left=25, right=25),
                    border_radius=5,
                    content=TextField(
                      label="Contraseña",
                      height=80,
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
                  Divider(color="transparent", height=3),
                  
                  #for Register
                  Container(
                    margin=margin.only(left=20, right=20), 
                    padding=padding.only(left=25, right=25),
                    on_click=lambda e: register_user(e),
                    height=50,
                    width=340,
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
                  Divider(color="transparent", height=5),
                  #Txt for register
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
                          content=self.tValform,
                        ),
                      ],
                    ),
                  ),
                  
                  #Dou you have an account?
                  Container(
                    padding=padding.only(left=20, right=20),
                    content=Text(
                      "¿Ya tienes una cuenta? ",
                      disabled=False,
                      #max_lines=2,
                      text_align='center',
                      spans=[
                        TextSpan(" "),
                        TextSpan(
                          "Iniciar Sesión",
                          TextStyle(decoration=TextDecoration.NONE, weight=FontWeight.W_900,),
                          #on_click=lambda _: self.page.go('/terms'), #this work to going next page only

                          on_click=lambda _: self.page.go('/login'),
                          #url="https://google.com",
                          on_enter=lambda e: signin_highlight_link(e),
                          on_exit=lambda e: signin_unhighlight_link(e),
                      
                      #Events type examples for print in console
                          #on_click=lambda e: print(f"Clicked span: {e.control.uid}"),
                          #on_enter=lambda e: print(f"Estoy encima de terminos y condiciones: {e.control.uid}"),
                          #on_exit=lambda e: print(f"Estoy fuera de terminos y condiciones: {e.control.uid}"),
                        ),
                        TextSpan(".")
                      ],
                    ),
                  ),

                  #Divider(color="transparent", height=25),
                  Row(
                     height=40,
                     opacity=0,
                  )
                ]
              )
            ]
          )
        ) 
      ]
    )

  #pirebase4 for login/register
    def handle_sign_in_error():
        snack_bar = SnackBar(
            content=Text("El correo electrónico ya está asociado a una cuenta.", color=input_fill_color),
            bgcolor=hint_base_color_plus
        )
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()
    
    def register_user(e):
      global form0, form1, form2, form3
      
      usern = str(form0).strip()
      email = str(form1).strip()
      passw = str(form2).strip()
      
      if form0 == "False" or form1 == "False" or form2 == "False" or form3 == "False":
        self.go_to_valid()
        page.update()
      else:
        try:
          #print("User:",usern,"email:",email,"password:",passw)
          myPyrebase.register_user(usern, email, passw)
          usern, email, passw = '', '', ''
          page.go('/home')
          page.update()
        except:
          handle_sign_in_error()
          page.update()
          
    
    # payload = {
    #     "email": form1,
    #     "password": form2,
    #     "returnSecureToken": True
    # }
    
    # print("Payload being sent:", payload)

  #Return to loginIN
  def go_to_signup(self):
    self.page.go('/login')
    back.back_ = '/'

  def next_clicked(self, e):
        self.page.go("/") #change to next step VALID and submit

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
  tValform = create_text()

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

  #forPassword blur
  def textbox_shadow(self,e):
    global form2
    form2 = "False"

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
      form2 = e.control.value
    self.update()

  #forUSNAME
  def textbox_changed_usname(self,e):
    global form0
    form0 = "False"

    #NO working almost added event on blur with this condition . . . 
    #e.control.value = e.control.value.upper()  # Forzar a mayúsculas
    has_spaces = any(c.isspace() for c in e.control.value)

    if e.control.value != "" and not has_spaces:
      if len(e.control.value) < 8:
        self.tUser.color = foreground_color_error
        self.tUser.value = "❌ ¡El número de caracteres no es mayor a 8!."
      else:
        self.tUser.color = foreground_color_check
        self.tUser.value = "✅ Usuario valido." 
        form0 = e.control.value
    elif e.control.value == "":
      self.tUser.color = foreground_color_error
      self.tUser.value = "➖ ¡Campo vacio!."
    else:
      self.tUser.color = foreground_color_error
      self.tUser.value = "❌ ¡No puedes introducir  espacios!." 
    self.update()

  #forMAIL
  def textbox_changed_mail(self,e):
    global form1
    form1 = "False"

    has_spaces = any(c.isspace() for c in e.control.value)
    # pattern for valid mail
    #patron = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'  
    #New pattern
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if e.control.value != "" and not has_spaces:
      if not re.match(patron, e.control.value):
        self.tMail.color = foreground_color_error
        self.tMail.value = "❌ ¡No es un correo electrónico valido!."
      else:
        self.tMail.color = foreground_color_check
        self.tMail.value = "✅ Correo electrónico valido."
        form1 = e.control.value
    elif e.control.value == "":
      self.tMail.color = foreground_color_error
      self.tMail.value = "➖ ¡Campo vacio!."
    else:
      self.tMail.color = foreground_color_error
      self.tMail.value = "❌ ¡No puedes introducir  espacios!." 
    self.update()
  
  #Valid Mail
  def textbox_validpass(self,e):
    global form3
    form3 = "False"

    if e.control.value == txtpass and txtpass != "":
      self.validpass.color = foreground_color_check
      self.validpass.value = "✅ Correo electrónico verificado."
      form3 = e.control.value
    elif e.control.value == "":
      self.validpass.color = foreground_color_error
      self.validpass.value = "➖ ¡Campo vacio!."
    else:
      self.validpass.color = foreground_color_error
      self.validpass.value = "❌ El correo electrónico no coincide."
    self.update()

  #Verify if the four txtfields are valid
  def go_to_valid(self):

    if form0 != "False" and form1 != "False" and form2 != "False" and form3 != "False":
      self.tValform.color = foreground_color_check
      self.tValform.value = "✅ ¡Puedes registrarte!"
    else:
      self.tValform.color = foreground_color_error
      self.tValform.value = "❌ Alguno de los campos no son correctos"
    self.update()

