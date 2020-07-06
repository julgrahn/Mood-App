from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def signUp(self):
        self.manager.current = "signUpScreen"

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def addUser(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        users[uname] = {'username': uname, 'password': pword, 
                    'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

        with open("users.json", 'w') as file:
            json.dump(users, file)
        self.manager.current = "signUpScreenSuccess"
        
class SignUpScreenSuccess(Screen):
    def goToLogin(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "loginScreen"

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()

