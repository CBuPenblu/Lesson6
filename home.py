class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name

    def set_access_level(self, access_level):
        if access_level in ['user', 'admin']:
            self.__access_level = access_level
        else:
            raise ValueError("Access level must be 'user' or 'admin'")

    def __repr__(self):
        return f"User(id={self.__user_id}, name={self.__name}, access_level={self.__access_level})"

class Admin(User):
    def __init__(self, user_id, name, admin_level):
        super().__init__(user_id, name, access_level='admin')
        self.__admin_level = admin_level
        self.__user_list = []

    def get_admin_level(self):
        return self.__admin_level

    def set_admin_level(self, admin_level):
        self.__admin_level = admin_level

    def add_user(self, user):
        if isinstance(user, User):
            self.__user_list.append(user)
        else:
            raise TypeError("Only instances of User can be added")

    def remove_user(self, user_id):
        self.__user_list = [user for user in self.__user_list if user.get_user_id() != user_id]

    def get_all_users(self):
        return self.__user_list

    def __repr__(self):
        return f"Admin(id={self.get_user_id()}, name={self.get_name()}, admin_level={self.__admin_level})"

user1 = User(1, "Alice")
user2 = User(2, "Bob")
admin = Admin(3, "Charlie", "Super Admin")

admin.add_user(user1)
admin.add_user(user2)

print(admin.get_all_users())

admin.remove_user(1)

print(admin.get_all_users())