class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        new_floor = int(new_floor)
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)
                i += 1

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, House):
            return self.number_of_floors > other

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return House(self.name, self.number_of_floors + other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return self.__add__(other)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
