class fruit:
    seed="has many seeds"
    seeds="has a lot of seeds"
    def __init__(self, name, color):
          self.name = name
          self.color= color
    


orange = fruit('orange','orange')
print (orange.name)
print (orange.seeds)
apple = fruit('apple','red')
print(apple.name)
print(apple.seed)