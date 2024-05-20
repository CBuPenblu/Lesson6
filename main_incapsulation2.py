class Test():
    def public_func(self):
        print("public method")

    def _protected_func(self):
        print("protected method")

    def __private_func(self):
        print("private method")

    def test_private(self):
        self.__private_func()

test = Test()

test.public_func()

test._protected_fund()

test.test_private()