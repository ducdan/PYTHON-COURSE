#thua ke
# class Chu(Ong):
#     def print_ho(self):
#         print(self.ho)
class Ong:
    def __init__(self):
        self.ho='Tran'
        self.__ten='Hung'
    def __tai_san(self):
        print("100 cay vang")
class Me:
    def __init__(self):
        self.tai_san='200 cay vang'
class Cha(Ong):
    def __init__(self):
        self.ho='Nguyen'
    def print_name(self):
        pass
    # def tai_san(self):
    #     print("10 cay vang")
class Con(Cha,Me):
    def print_ho(self):
        print(self.ho)
        print(self.tai_san)
nam=Con()
# nam.print_ho()
nam.tai_san()
# chu=Chu()
# chu.print_ho()

