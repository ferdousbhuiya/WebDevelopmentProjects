class User:
    def __init__(self,x):
        self.z_name = x
        self.is_logged_in = False

def is_authenticate_decorator(func):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in == True:
            func(args[0])
    return wrapper

@is_authenticate_decorator
def create_blog_spot(y):
    print(f"This is {y.z_name}'s blog spot")


n_new_user = User('Hedayet')
n_new_user.is_logged_in = True
create_blog_spot(n_new_user)