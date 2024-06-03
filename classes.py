class User:
    def __init__(self, id, password, email):
        self.id = id
        self.password = password
        self.email = email



    def email2(self):
        print(self.email)
        return self.email

u = User(1, '12345', 'dave@gmail.com')
print(u.email)

u.email2()

def get_email():
    e = User()
