class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def create_blog_spot(user):
    print(f"This is {user.name}'s blog spot.")

new_user = User('Babul')
create_blog_spot(user=new_user)