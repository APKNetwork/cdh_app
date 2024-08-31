from flet import *
#from pages.home import HomeScreen
from pages.login import LoginScreen
from pages.signup import SignupScreen
from pages.logged_out import LoggedOutScreen
from pages.onboarding import OnboardingScreen
from pages.secboarding import secondOnboardingScreen
from pages.thiboarding import thirdOnboardingScreen
from pages.home_screen import HomeScreen
#from pages.search import SearchScreen
#from pages.events import EventsScreen
#from pages.profile import ProfileScreen


def views_handler(page, myPyrebase):
  #print("estoy dentro de views_handler de views")
  return {
    '/onboarding':View(
        route='/onboarding',
        controls=[
          OnboardingScreen(page, myPyrebase)
        ]
      ),
    '/secondOnboarding': View(
        route='/secondOnboarding',
        controls=[
          secondOnboardingScreen(page, myPyrebase)
        ]
      ),
    '/thirdOnboarding': View(
      route='thirdOnboarding',
      controls=[
        thirdOnboardingScreen(page, myPyrebase)
      ]
    ),
    '/':View(
        route='/',
        controls=[
          LoggedOutScreen(page, myPyrebase)
        ]
      ),
    '/login':View(
        route='/login',
        controls=[
          LoginScreen(page, myPyrebase)
        ]
      ),
    '/signup':View(
        route='/signup',
        controls=[
          SignupScreen(page, myPyrebase)
        ]
      ),
    '/home':View(
        route='/home',
        controls=[
          HomeScreen(page, myPyrebase)
        ]
      ),
    # '/search':View(
    #     route='/search',
    #     controls=[
    #       SearchScreen(page)
    #     ]
    #   ),
    # '/events':View(
    #     route='/events',
    #     controls=[
    #       EventsScreen(page)
    #     ]
    #   ),
    # '/profile':View(
    #     route='/profile',
    #     controls=[
    #       ProfileScreen(page)
    #     ]
    #   ),
  }