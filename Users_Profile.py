import time
class Profile:
  def __init__(self, user_name, email, learn_language):
    self.user_name = user_name
    self.email = email
    self.learn_language = learn_language

first_user = Profile("Jane", "qpmzj@example.com", "python")
second_user = Profile("Jack", "qpmzj@example.com", "java")
third_user = Profile("Jill", "qpmzj@example.com", "c++")

print(f"The first user's name is ({first_user.user_name}) and their email is ({first_user.email}) and they are learning ({first_user.learn_language}).")

print(f"The second user's name is ({second_user.user_name}) and their email is ({second_user.email}) and they are learning ({second_user.learn_language}).")

print(f"The first user's name is ({third_user.user_name}) and their email is ({third_user.email}) and they are learning ({third_user.learn_language}).")

time.sleep(2)
