from flet import *
from utils.selectable_container import SelectableContainer
from utils import back
from utils.extras import *

# Const firebase auth
# const firebaseConfig = {
#     apiKey: "AIzaSyC_vNk-ij4QogsXt2FGAqaf3gga0nBcYFk",
#     authDomain: "cdhapp-appdevof.firebaseapp.com",
#     projectId: "cdhapp-appdevof",
#     storageBucket: "cdhapp-appdevof.appspot.com",
#     messagingSenderId: "656390134432",
#     appId: "1:656390134432:web:1a02b9c0bdbe121ad407c5"
#   };


class LoggedOutScreen(Container):
  def __init__(self, page: Page):
    super().__init__()
    self.page = page

    page.title = "Welcome to CryDiagnoHealth" #Title Page
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.scroll = ScrollMode.ADAPTIVE
    page.update()

    #page.window_width = base_width
    #page.window_height = base_height
    page.fonts = { #fonts
        "Poppins Bold":"fonts/poppins/Poppins-Bold.ttf",
        "Poppins SemiBold":"fonts/poppins/Poppins-SemiBold.ttf",
        "ChauPhilomeneOne Regular":"fonts/ChauPhilomeneOne/ChauPhilomeneOne-Regular.ttf",
        "ChauPhilomeneOne Italic":"fonts/ChauPhilomeneOne/ChauPhilomeneOne-Italic.ttf"
    }

    #Funcions for terms and privacy
    def close_dlg(e):
        dlg_modal_terms.open = False
        dlg_modal_policy.open = False
        self.page.update()

    
    def on_hover_select(e):
      e.control.style.bgcolor = base_color  if e.data == "true" else "transparent"
      e.control.style.color = input_fill_color  if e.data == "true" else font_color 
      e.control.update()

    def on_long_press_select(e):
      e.control.style.bgcolor = base_color  if e.data == "true" else "transparent"
      e.control.style.color = input_fill_color  if e.data == "true" else font_color 
      e.control.style.overlay_color = base_color # if e.data == "true" else "transparent"
      e.control.update()

    # Popup message for terms of services
    dlg_modal_terms = AlertDialog(
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
            TextButton("Acepto", style=ButtonStyle(color=base_color, bgcolor="transparent"), on_click=close_dlg, on_hover=on_hover_select, on_long_press=on_long_press_select),
            TextButton("No Acepto", style=ButtonStyle(color=base_color, bgcolor="transparent"), on_click=close_dlg, on_hover=on_hover_select, on_long_press=on_long_press_select),
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("El dialogo de los terminos y condiciones fue cerrado!"),
    )

    # Popup message for terms of services
    dlg_modal_policy = AlertDialog(
        modal=True,
        #adaptative=True, revisar para ios cuppertino
        title=Text("POR FAVOR LEA DETENIDAMENTE NUESTRAS POLITICAS DE PRIVACIDAD.",
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
            " Fecha de la Última Actualización: [13 - 02 - 2024] .",
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
                    "Gracias por confiar en",
                    TextStyle(font_family="Poppins SemiBold"),                  
                    spans=[
                      TextSpan(
                      " CryDiagnoHealth ",
                      TextStyle(font_family="ChauPhilomeneOne Regular", size=18),
                      ),
                      TextSpan(
                        ", para el cuidado de la salud de los bebés. La privacidad de tus datos personales es una prioridad para nosotros. Esta política de privacidad explica cómo recopilamos, utilizamos y protegemos tu información personal, especialmente en relación con el preprocesamiento de patologías en bebés. Al utilizar nuestra aplicación, aceptas las prácticas descritas en esta política de privacidad.",
                        TextStyle(font_family="Poppins SemiBold"),
                      ),
                    ],
                  )
                ],
            ),

            Divider(height=25,color=base_color),
            Text(
              "1. Información Recopilada:",
                font_family="Poppins Bold",
                size=16,
              ),
            Text(
                '• Recopilamos información personal que nos proporcionas voluntariamente al registrarte en la aplicación, incluidos tu nombre, dirección de correo electrónico, edad, etc. Esta información es necesaria para crear una cuenta personalizada y brindarte acceso a los servicios de la aplicación.',
                font_family="Poppins SemiBold",
                text_align="JUSTIFY",
            ),
            Text(
                '• Además, recopilamos información sobre la salud de los bebés, incluidas las grabaciones de llanto, la edad, el color de piel, el idioma principal hablado en el hogar, etc. Esta información es esencial para el análisis y preprocesamiento de patologías en bebés.',
                font_family="Poppins SemiBold",
                text_align="JUSTIFY",
            ),
            Text(
                '• La grabación de llantos de bebés es una parte esencial de nuestra aplicación y se utiliza únicamente con el propósito de preprocesar patologías en bebés para facilitar diagnósticos y tratamientos médicos. Nos comprometemos a utilizar esta información de manera ética y responsable.',
                font_family="Poppins SemiBold",
                text_align="JUSTIFY",
            ),
            Divider(height=15,color="TRANSPARENT"),
            Text(
              "2. Uso de la Información:",
                font_family="Poppins Bold",
                size=16,
              ),
            Text(
              "• Utilizamos la información recopilada para proporcionar y mejorar nuestros servicios, incluido el preprocesamiento de patologías en bebés. Esta información es fundamental para ayudar a los profesionales de la salud en la detección temprana y el tratamiento adecuado de enfermedades en bebés.",
              font_family="Poppins SemiBold",
              text_align="JUSTIFY",
            ),
            Text(
              '• La grabación de llantos de bebés se procesa de forma segura y solo se utiliza con fines médicos y de investigación para mejorar la detección temprana y el tratamiento de enfermedades en bebés.',
              font_family="Poppins SemiBold",
              text_align="JUSTIFY",
            ),
            Divider(height=15,color="TRANSPARENT"),
            Text(
              "3. Protección de la Información:",
                font_family="Poppins Bold",
                size=16,
              ),
            Text(
              "• Implementamos medidas de seguridad técnicas y organizativas para proteger tu información personal y la grabación de llantos de bebés contra accesos no autorizados, divulgación o destrucción.",
              font_family="Poppins SemiBold",
              text_align="JUSTIFY",
            ),
            Text(
              '• Nos comprometemos a proteger la confidencialidad de la grabación de llantos de bebés y a utilizarla únicamente con fines médicos y de investigación.',
              font_family="Poppins SemiBold",
              text_align="JUSTIFY",
            ),
            Divider(height=15,color="TRANSPARENT"),
            Text(
              "4. Acceso y Control de la Información:",
                font_family="Poppins Bold",
                size=16,
              ),
            Text(
              "• Tienes el derecho de acceder, corregir y eliminar tus datos personales en cualquier momento. Puedes actualizar tu información personal y la de los bebés en la configuración de tu cuenta en la aplicación.",
              font_family="Poppins SemiBold",
              text_align="JUSTIFY",
            ),
            Text(
              text_align='JUSTIFY',
              spans=[
                TextSpan("Si deseas ejercer tus derechos de privacidad o tienes alguna pregunta sobre esta política de privacidad, por favor contáctanos a través de ",TextStyle(font_family="Poppins SemiBold")),
                TextSpan(
                  "support@service.crydiagnohealt.com",
                  TextStyle(font_family="ChauPhilomeneOne Regular", size=14),
                ),
              ]
            ),
            Divider(height=15,color="TRANSPARENT"),
            Text(
              "5. Consentimiento:",
                font_family="Poppins Bold",
                size=16,
              ),
              Text(
              "• Al utilizar nuestra aplicación, aceptas la recopilación y el uso de tu información personal, así como de la grabación de llantos de bebés, de acuerdo con esta política de privacidad. Entendemos la sensibilidad de los datos recopilados y nos comprometemos a utilizarlos únicamente con el propósito de preprocesar patologías en bebés y mejorar los servicios de salud. Tu consentimiento es fundamental para proporcionar la atención médica necesaria y continuar avanzando en la investigación en este campo. Si no estás de acuerdo con alguno de los términos de esta política de privacidad, te recomendamos que dejes de utilizar la aplicación de inmediato.",
              font_family="Poppins SemiBold",
              text_align="JUSTIFY",
            ),
            Divider(height=15,color="TRANSPARENT"),
            Text(
              "6. Cambios en la Política de Privacidad:",
                font_family="Poppins Bold",
                size=16,
              ),
              Text(
              "• Nos reservamos el derecho de actualizar o modificar esta política de privacidad en cualquier momento para reflejar cambios en nuestras prácticas de recopilación y uso de datos, así como para cumplir con las leyes y regulaciones aplicables. Es importante que revises periódicamente esta política para estar informado sobre cómo se está utilizando y protegiendo tu información personal. Se te notificará sobre cualquier cambio significativo en esta política a través de la aplicación o por otros medios adecuados. El uso continuado de la aplicación después de la publicación de los cambios en esta política se considerará como tu aceptación de dichos cambios.",
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
                TextSpan(" aceptas cumplir con esta política de privacidad. Si tienes alguna pregunta o inquietud sobre esta política, no dudes en ponerte en contacto con nosotros al correo ",TextStyle(font_family="Poppins SemiBold")),
                TextSpan(
                  "support@service.crydiagnohealt.com",
                  TextStyle(font_family="ChauPhilomeneOne Regular", size=14),
                ),
              ]
            ),
          ]
        ),

        actions=[
            TextButton("Acepto", style=ButtonStyle(color=base_color, bgcolor="transparent"), on_click=close_dlg, on_hover=on_hover_select, on_long_press=on_long_press_select),
            TextButton("No Acepto", style=ButtonStyle(color=base_color, bgcolor="transparent"), on_click=close_dlg, on_hover=on_hover_select, on_long_press=on_long_press_select),
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("El dialogo de las politicas de provacidad fue cerrado!"),
    )

    # Set route for open and close dialogs for terms and policy

    # D E P R E C A T E D  - - -  on ver. 0.21.0 flet
    # def terms_open_dlg(e):
    #     self.page.dialog = dlg_modal_terms
    #     dlg_modal_terms.open = True
    #     self.page.update()
    
    # def policy_open_dlg(e):
    #     self.page.dialog = dlg_modal_policy
    #     dlg_modal_policy.open = True
    #     self.page.update()

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


    self.content = Column(
       controls=[
        SafeArea(
          #expand=True,
          content=Column(
            alignment="spaceBetween",
            spacing=0,
            controls=[ #este controlador expande al tamaño del padre
              Column(
              horizontal_alignment=CrossAxisAlignment.CENTER, # Text on top boarding      
              alignment=MainAxisAlignment.CENTER,
                controls=[
                  #Divider(height=0, color="transparent"),
                  Container(
                    #border=border.all(6, colors.RED_600),
                    padding = padding.only(top=-25,bottom=-30),
                    #border=border.all(5, colors.BLUE_600),
                    bgcolor="transparent",
                    width='auto', 
                    height='auto',
                    #right=30, left=30,
                    #padding=padding.only(),
                    content=Image(
                        src='/images/recurso_6_forwh.png', #Picture one ob
                        scale=1,
                        width='auto',
                        height='auto',
                    )
                  ),
                  #Divider(height=0,color="transparent"), 
                  Container(
                    padding=padding.only(left=25, right=25, top=-40),
                    content=Text(
                      "Crea tu cuenta de ",
                      disabled=False,
                      font_family='Poppins Bold',
                      overflow=TextOverflow.VISIBLE,
                      #max_lines=2,
                      size=30,
                      text_align="center",
                      spans=[
                        TextSpan(" "),
                        TextSpan(
                          "CryDiagnoHealth",
                          TextStyle(decoration=TextDecoration.NONE, font_family='ChauPhilomeneOne Regular', size=37),
                          #on_click=lambda _: self.page.go('/terms'), #this work to going next page only
                          #on_click=terms_op en_dlg,
                          on_enter=lambda e: terms_highlight_link(e),
                          on_exit=lambda e: terms_unhighlight_link(e),
                        ),
                        TextSpan(".")
                      ],
                    ),
                  ),
                  #Divider(height=0, color="transparent"),
                  Container(
                    Text(
                      #expand=True,
                      width=550,
                      value="Únete a nuestra comunidad para contribuir al cuidado de la salud infantil. Registrate y comienza a grabar llantos para un diagnóstico temprano y preciso.",
                      font_family='Poppins SemiBold',
                      size=15,
                      text_align=TextAlign.CENTER,
                    ), margin=margin.only(left=20, right=20),
                  ),
                  Container(
                    height=35
                  ),

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
                  #Divider(height=2, color="transparent"),
                  Container(
                    margin=margin.only(left=20, right=20), 
                    on_click=lambda e: self.go_to_login(),
                    height=55,
                    width=450,
                    border_radius=25,
                    border=border.all(3.5, base_color),
                    bgcolor="transparent",
                    alignment=alignment.center,
                    content= Text('Iniciar Sesión',
                    font_family='Poppins SemiBold',
                    size=14,
                    color=base_color,
                    text_align='center'
                    ),
                  ),

                  Container(
                    height=40
                  ),
                  Container(
                    padding=padding.only(left=25, right=25),
                    content=Text(
                      "Para continuar estas aceptando nuestros",
                      disabled=False,
                      #max_lines=2,
                      text_align='center',
                      spans=[
                        TextSpan(" "),
                        TextSpan(
                          "Terminos del Servicio",
                          TextStyle(decoration=TextDecoration.UNDERLINE),
                          #on_click=lambda _: self.page.go('/terms'), #this work to going next page only

                          on_click=lambda e: page.open(dlg_modal_terms),
                          #url="https://google.com",
                          on_enter=lambda e: terms_highlight_link(e),
                          on_exit=lambda e: terms_unhighlight_link(e),
                      
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
                          on_click=lambda e: page.open(dlg_modal_policy),
                          on_enter=lambda e: policy_highlight_link(e),
                          on_exit=lambda e: policy_unhighlight_link(e),
                        ),
                        TextSpan(".")
                      ],
                    ),
                  ),
                  #Divider(height=20, color="transparent"),
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

    #page.window_min_height = 600
    #page.scroll = "adaptative"

  def go_to_login(self):
    self.page.go('/login')
    back.back_ = '/'
  print("estoy en logged_out mandado por onboardings")

  def go_to_signup(self):
    self.page.go('/signup')
    back.back_ = '/'