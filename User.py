
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

        self.rewards_member = False
        self.golden_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.rewards_member)
        print(self.golden_points)

    def signed_up(self):
        self.rewards_member = True
        self.golden_points = 200
    def spend_points(self, amount):
        self.amount = self.golden_points - amount
        print(self.amount)

joe = User("Joe","Coats","Joe@coding",26)

joe.signed_up()
joe.display_info()

hannah = User('Hannah','Gayle', 'hgay23@coding', 25)
tay = User("Tay", "Wilson", "taytay@gmail", 32)


joe.spend_points(50)

hannah.signed_up()
hannah.spend_points(80)

joe.display_info()
hannah.display_info()
tay.display_info()

