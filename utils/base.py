from flet import *

#
# D E P R E C A T E D only for onboarding pages 06/01/24
#

class BasePage(UserControl):
  def __init__(self, content=None):
    super().__init__()
    self.content = content
  def build(self):
    return Column(
      #expand=True,
      scroll=ScrollMode.HIDDEN,
      #auto_scroll=True,
      alignment="spaceEvenly",
      controls=[
        Container(
          #expand=True,
          #border=border.all(5, colors.PINK_600),
          padding=35,
          #bottom=False,
          #bgcolor="#40374E",
          #bgcolor='#F2F2F2',
          bgcolor= colors.TRANSPARENT,
          content=self.content
        )
      ]
    )