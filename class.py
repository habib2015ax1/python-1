class vehicle:

    def __init__(self, name, max_speed, mialage):
        self.max_speed= max_speed
        self.mialage = mialage
        self.name = name

tesla = vehicle('tesla','200','400')
audi = vehicle('audi','210','330')
xaiomi=vehicle('xaiomi','133','400')

print (tesla.max_speed)
print (tesla.mialage)
print (audi.max_speed)
print (audi.mialage)
print (xaiomi.max_speed)
print (xaiomi.mialage)

     