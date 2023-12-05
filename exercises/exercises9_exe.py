from exercises.exercises9 import *

user1 = User('anton', 'ivanov', 'ash.rest@gmail.com', '1234562566')
user1.increment_attempts()
user1.increment_attempts()
user1.increment_attempts()
user1.reset_attempts()

# login_page = LoginPage()
# main_page = MainPage()
# login_page.enter_username('johndoe')
# login_page.enter_password('123456')
# login_page.signin()
# main_page.verify_welcome_message('johndoe')

admin1 = Admin('jane', 'doe', 'janedoe@gmail.com', '12345')
admin1.increment_attempts()
admin1.show_privileges()
admin1.add_privileges('can update user info')

admin1.privileges.show_privileges()
print(admin1.privileges.privileges)
admin1.privileges.add_privileges('can create user')