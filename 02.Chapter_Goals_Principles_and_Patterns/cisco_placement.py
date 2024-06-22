'''
FY25 Cisco Pre Placement Talk

Don't miss the chance to learn from Cisco experts 
and discover what it takes to become a part of the
Cisco family.
'''


class Cisco:
    def __init__(self, techie, passion):
        self.techie = techie
        self.passion = passion

    def __str__(self):
        return f"\nTechie: {self.techie} \
                Passion: {self.passion}"

    def show_bright_future(self):
        print('\n\tSwipe right, choose Cisco')
        print("\n\t'The bridge to possible'\n")


c1 = Cisco('Pranav', 'Software Engineer-SDE')
print(c1)
c1.show_bright_future()
