from flet import *
from utils.selectable_container import SelectableContainer
from utils.base import BasePage as BP
from utils import back
from utils.extras import *

class LoggedOutScreen(UserControl):
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

    page.window_min_height = 300
    #page.scroll = "adaptative"
    page.scroll = "False"
    page.update()

  def go_to_login(self):
    self.page.go('/login')
    back.back_ = '/'
  print("estoy en logged_out mandado por onboardings")

  def go_to_signup(self):
    self.page.go('/signup')
    back.back_ = '/'

  #Main function - - -
  def build(self):

    #Funcions for terms and privacy
    def close_dlg(e):
        dlg_modal.open = False
        self.page.update()

    
    def on_hover_select(e):
      e.control.style.bgcolor = base_color  if e.data == "true" else "TRANSPARENT"
      e.control.style.color = input_fill_color  if e.data == "true" else font_color 
      e.control.update()

    dlg_modal = AlertDialog(
        modal=True,
        #adaptative=True, revisar para ios cuppertino
        title=Text("POR FAVOR LEA DETENIDAMENTE NUESTROS TERMINOS Y CONDICIONES DEL SERVICIO.",
          font_family="Poppins Bold",
          text_align='JUSTIFY',
          size=20,
          ),
        content=Column(
          # alignment=MainAxisAlignment.CENTER,
          auto_scroll=False,
          scroll=ScrollMode.HIDDEN,
          alignment="spaceBetween",
          horizontal_alignment='JUSTIFY',
          #width=MainAxisAlignment,
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
            Text(
                '• Te comprometes a proporcionar información precisa y completa al registrarte en la aplicación y a mantener actualizados tus datos personales.',
                font_family="Poppins SemiBold",
                text_align="JUSTIFY",
            ),
            Divider(height=15,color="TRANSPARENT"),
            Text(
              "2. Recopilación y Uso de Datos:",
                font_family="Poppins Bold",
                size=16,
              ),
            Text(
              "• Al utilizar nuestra aplicación, aceptas que recopilemos cierta información personal, incluidas las grabaciones de llanto de los bebés y los datos personales de los usuarios.",
              font_family="Poppins SemiBold",
              text_align="JUSTIFY",
            ),
            Text(
              '• La información recopilada se utiliza para mejorar la funcionalidad de la aplicación, realizar análisis estadísticos y proporcionar servicios personalizados.',
              font_family="Poppins SemiBold",
              text_align="JUSTIFY",
            ),
            Text(
              '• Nos comprometemos a proteger la privacidad y seguridad de tus datos personales de acuerdo con nuestra política de privacidad.',
              font_family="Poppins SemiBold",
              text_align="JUSTIFY",
            ),
            Divider(height=15,color="TRANSPARENT"),
            Text(
              "3. Propiedad Intelectual:",
                font_family="Poppins Bold",
                size=16,
              ),
            Text(
              text_align='JUSTIFY',
              spans=[
                TextSpan(
                  '• Todos los derechos de propiedad intelectual relacionados con la aplicación, incluidos los derechos de autor, marcas comerciales y derechos de bases de datos, son propiedad de ',
                  TextStyle(font_family="Poppins SemiBold"),
                ),
                TextSpan(
                  "CryDiagnoHealth Team Support",
                  TextStyle(font_family="ChauPhilomeneOne Regular", size=18),
                ),
                TextSpan(" o de sus licenciantes. ",TextStyle(font_family="Poppins SemiBold")),
              ]
            ),
            Text(
              text_align='JUSTIFY',
              spans=[
                TextSpan(' '),
                TextSpan(
                  '• No se permite la reproducción, distribución o modificación de ningún contenido de la aplicación sin el consentimiento previo por escrito de ',
                  TextStyle(font_family="Poppins SemiBold"),
                ),
                TextSpan(" "),
                TextSpan(
                  "CryDiagnoHealth Team Support",
                  TextStyle(font_family="ChauPhilomeneOne Regular", size=18),
                ),
                TextSpan(". ",TextStyle(font_family="Poppins SemiBold")),
              ]
            ),
            Divider(height=15,color="TRANSPARENT"),
            Text(
              "4. Responsabilidad y Exención de Garantías:",
                font_family="Poppins Bold",
                size=16,
              ),
            Text(
              text_align='JUSTIFY',
              spans=[
                TextSpan(
                  '• ',
                  TextStyle(font_family="Poppins SemiBold"),
                ),
                TextSpan(
                  "CryDiagnoHealth Team Support",
                  TextStyle(font_family="ChauPhilomeneOne Regular", size=18),
                ),
                TextSpan(" no garantiza la disponibilidad, precisión o fiabilidad de la aplicación en todo momento. El uso de la aplicación es bajo tu propio riesgo.",TextStyle(font_family="Poppins SemiBold")),
              ]
            ),
            Text(
              text_align='JUSTIFY',
              spans=[
                TextSpan(
                  '• ',
                  TextStyle(font_family="Poppins SemiBold"),
                ),
                TextSpan(
                  "CryDiagnoHealth Team Support",
                  TextStyle(font_family="ChauPhilomeneOne Regular", size=18),
                ),
                TextSpan(" no se hace responsable de cualquier daño directo, indirecto, incidental, especial o consecuente derivado del uso o la imposibilidad de uso de la aplicación.",TextStyle(font_family="Poppins SemiBold")),
              ]
            ),
            Divider(height=15,color="TRANSPARENT"),
            Text(
              "5. Modificaciones y Terminación:",
                font_family="Poppins Bold",
                size=16,
              ),
            Text(
              text_align='JUSTIFY',
              spans=[
                TextSpan(
                  '• ',
                  TextStyle(font_family="Poppins SemiBold"),
                ),
                TextSpan(
                  "CryDiagnoHealth Team Support",
                  TextStyle(font_family="ChauPhilomeneOne Regular", size=18),
                ),
                TextSpan(" se reserva el derecho de modificar, suspender o descontinuar cualquier aspecto de la aplicación en cualquier momento y sin previo aviso.",TextStyle(font_family="Poppins SemiBold")),
              ]
            ),
            Text(
              '• Nos reservamos el derecho de terminar tu acceso a la aplicación en caso de violación de estos términos del servicio.',
              font_family="Poppins SemiBold",
              text_align="JUSTIFY",
            ),
            Divider(height=15,color="TRANSPARENT"),
            Text(
              "6. Ley Aplicable y Jurisdicción:",
                font_family="Poppins Bold",
                size=16,
              ),
            Text(
              '• Estos términos del servicio se rigen por las leyes del país de México y cualquier disputa relacionada con estos términos estará sujeta a la jurisdicción exclusiva de los tribunales del mismo.',
              font_family="Poppins SemiBold",
              text_align="JUSTIFY",
            ),
            Divider(height=15,color="TRANSPARENT"),
            Text(
              "7. Cambios en los Términos del Servicio:",
                font_family="Poppins Bold",
                size=16,
              ),
            Text(
              '• Nos reservamos el derecho de actualizar o modificar estos términos del servicio en cualquier momento sin previo aviso. Se te notificará sobre cualquier cambio significativo a través de la aplicación o por otros medios.',
              font_family="Poppins SemiBold",
              text_align="JUSTIFY",
            ),
            Divider(height=25, color=base_color),
            Text(
              text_align='JUSTIFY',
              spans=[
                TextSpan(
                  'Al utilizar la aplicación ',
                  TextStyle(font_family="Poppins SemiBold"),
                ),
                TextSpan(
                  "CryDiagnoHealth",
                  TextStyle(font_family="ChauPhilomeneOne Regular", size=18),
                ),
                TextSpan(" aceptas cumplir con estos términos del servicio. Si tienes alguna pregunta o inquietud sobre estos términos, no dudes en ponerte en contacto con nosotros a través de ",TextStyle(font_family="Poppins SemiBold")),
                TextSpan(
                  "support@service.crydiagnohealt.com",
                  TextStyle(font_family="ChauPhilomeneOne Regular", size=14),
                ),
              ]
            ),
            Divider(height=15, color="TRANSPARENT"),
            Text(
              text_align='JUSTIFY',
              spans=[
                TextSpan(
                  'Gracias por elegir ',
                  TextStyle(font_family="Poppins SemiBold"),
                ),
                TextSpan(
                  "CryDiagnoHealth",
                  TextStyle(font_family="ChauPhilomeneOne Regular", size=18),
                ),
                TextSpan("  y confiar en nosotros para cuidar las investigaciones sobre las patologías de los bebés.",TextStyle(font_family="Poppins SemiBold")),
              ]
            ),
          ]
        ),

        actions=[
            TextButton("Acepto", style=ButtonStyle(color=base_color), on_click=close_dlg, on_hover=on_hover_select),
            TextButton("No Acepto", style=ButtonStyle(color=base_color), on_click=close_dlg, on_hover=on_hover_select),
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("El dialogo fue cerrado!"),
    )

    def terms_open_dlg(e):
        self.page.dialog = dlg_modal
        dlg_modal.open = True
        self.page.update()

    # Set highlight and unhighlight of terms
    def terms_highlight_link(e):
      # For lighnight
      e.control.style.color = selected_item
      e.control.update()

    def terms_unhighlight_link(e):
      e.control.style.color = base_color
      e.control.update()

    # Set highlight and unhighlight of policy
    def policy_highlight_link(e):
        # For lighnight
        e.control.style.color = selected_item
        e.control.update()

    def policy_unhighlight_link(e):
        e.control.style.color = base_color
        e.control.update()

    return Column(
      scroll=ScrollMode.HIDDEN,
      height=980,
      controls=[
        SafeArea(
          bottom=False,
          maintain_bottom_view_padding = False,
          minimum = 5,
          #expand=True,
          content=Column(
            alignment="spaceBetween",
            controls=[ #este controlador expande al tamaño del padre
              Container(
                #border=border.all(6, colors.PINK_600),
                #padding = padding.only(left=35,right=35, bottom=40),
                content=Column(
                  # alignment=MainAxisAlignment.CENTER,
                  alignment="spaceBetween",
                  horizontal_alignment='center',
                  controls=[
                    Container(
                      #border=border.all(6, colors.RED_600),
                      padding = padding.only(top=-5,bottom=-30),
                      #border=border.all(5, colors.BLUE_600),
                      bgcolor="transparent",
                      width=450,
                      height=300,
                      #padding=padding.only(),
                      content=Image(
                          src='assets/images/recurso_6_forwh.png', #Picture one ob
                          scale=1.2,
                          width=100,
                          height=100,
                      )
                    ),
                    # Image(
                    #   src='assets/images/logo.png',
                    #   width=200,
                    # ),
                    # CircleAvatar(
                    #   foreground_image_url='https://images.unsplash.com/photo-1548449112-96a38a643324?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
                    #   # ,
                    #   radius=85//2,
                    # ),
                    # Container(
                    #   height=10
                    # ),
                    Text(
                      #overflow=TextOverflow.FADE, FADED
                      overflow=TextOverflow.VISIBLE,
                      value="Crea tu cuenta de CryDiagnoHealth.",
                      #no_wrap=False,
                      font_family='Poppins Bold',
                      #text_align=TextAlign.CENTER,
                      size=28,
                      #max_lines=2,
                      text_align="center",
                    ),
                    Divider(height=10, color="transparent"),
                    Text(
                      #expand=True,
                      width=600,
                      value="únete a nuestra comunidad para contribuir al cuidado de la salud infantil. Registrate y comienza a grabar llantos para un diagnóstico temprano y preciso.",
                      font_family='Poppins SemiBold',
                      #text_align=TextAlign.CENTER,
                      size=14,
                      #max_lines=4,
                      text_align="center",
                    ),
                    Container(
                      height=40
                    ),

                    Container(
                      on_click=lambda e: self.go_to_signup(),
                      height=44,
                      width=307,
                      border_radius=25,
                      bgcolor=base_color,
                      alignment=alignment.center,
                      content= Text('Sign Up',
                      font_family='Poppins SemiBold',
                      size=14,
                      color='white',
                      text_align='center'
                      ),
                    ),
                    Divider(height=10, color="transparent"),
                    Container(
                      on_click=lambda e: self.go_to_login(),
                      height=44,
                      width=307,
                      border_radius=25,
                      border=border.all(4, base_color),
                      bgcolor="transparent",
                      alignment=alignment.center,
                      content= Text('Log In',
                      font_family='Poppins SemiBold',
                      size=14,
                      color=base_color,
                      text_align='center'
                      ),
                    ),

                    Container(
                      height=50
                    ),
                    Container(
                      content=Text(
                        "Para continuar estas aceptando nuestros",
                        disabled=False,
                        max_lines=2,
                        text_align='center',
                        spans=[
                          TextSpan(" "),
                          TextSpan(
                            "Terminos del Servicio",
                            TextStyle(decoration=TextDecoration.UNDERLINE),
                            #on_click=lambda _: self.page.go('/terms'), #this work to going next page only

                            on_click=terms_open_dlg,
                            #url="https://google.com",
                            on_enter=terms_highlight_link,
                            on_exit=terms_unhighlight_link,
                        
                        #Events type examples for print in console
                            #on_click=lambda e: print(f"Clicked span: {e.control.uid}"),
                            #on_enter=lambda e: print(f"Estoy encima de terminos y condiciones: {e.control.uid}"),
                            #on_exit=lambda e: print(f"Estoy fuera de terminos y condiciones: {e.control.uid}"),
                          ),
                          TextSpan(" "),
                          TextSpan("y nuestras"),
                          TextSpan(" "),
                          TextSpan(
                            "Politicas de Privacidad",
                            TextStyle(decoration=TextDecoration.UNDERLINE),
                            on_click=lambda _: self.page.go('/policy'),
                            #url="https://google.com",
                            on_enter=policy_highlight_link,
                            on_exit=policy_unhighlight_link,
                          ),
                          TextSpan(".")
                        #   TextSpan(" "),
                        #   TextSpan(" "),
                        ],
                      ),
                    ),
                    Divider(height=50, color="transparent"),
                      # color='#3797EF',
                      # font_family='SF Pro SemiBold',
                      # size=14,
                      # text_align='center'
                      # ),),
                      # controls=[
                      #   Text("Don't have an account?",
                      #     color='black',
                      #     font_family='SF Pro SemiBold',
                      #     size=12,
                      #     text_align='center',
                      #     opacity=0.4
                      #     ),Container(
                      #         width=6
                      #       ),
                      #   Container(
                      #     on_click = lambda _: self.pg.go('/signup'),
                      #     content=Text("Sign up.",
                      #     color='#262626',
                      #     font_family='SF Pro SemiBold',
                      #     size=14,
                      #     text_align='center',
                      #     ),
                      #   )
                      # ]
                    ]
                  )
              )
            ]
          )
        )
      ]
    )
  # only for confirm or degree
  # async def close_dlg(e):
  #   e.dlg_modal.open = False
  #   e.control.page.update_async

  #ElevatedButton("Open dialog", on_click=open_dlg),