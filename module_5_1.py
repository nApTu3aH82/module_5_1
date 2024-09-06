class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, floor):
        self.floor = floor
        if floor > self.number_of_floors:
            print('Такого этажа не существует!')
        else:
            for count in range(floor):
                print(count + 1)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

print("на какой этаж вы хотите подняться в 'ЖК Горский?':")
num_float = int(input())
h1.go_to(num_float)
