class details:
# Gets the details
    def getdetails(self):
        import random
        self.name=input('Enter your name: ')
        self.id=random.randint(100,1000)
        while True:
            self.num=input('Enter Phone number:')
            if len(self.num)==10:
                break
            else:
                print('Invalid phone number try again.')
        self.email=input('Enter Email:')
# Prints the details
    def printdetails(self):
        print(f'Welcome {self.name}.')
