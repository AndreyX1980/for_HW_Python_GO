#Доработаем задачи 5-6. Создайте класс-фабрику.
#Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
#Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

import lesson10_5_6

class AnimalFabric:
    def __init__(self, animal_type, *args, **kwargs):
        self.animal_type = animal_type

    def get(animal_type):
        if animal_type == "Fish":
            return lesson10_5_6.Fish
        if animal_type == "Birds":
            return lesson10_5_6.Birds
        if animal_type == "Mammals":
            return lesson10_5_6.Mammals


if __name__ == '__main__':
    goldfish = AnimalFabric.get("Fish")(True, 3, "Goldfish", True)
    print(goldfish.fresh_water)
    print(f"Рыбка называется {goldfish.name},Она плавает на глубине {goldfish.deep} метра,"
          f"Она живет в пресной воде? {goldfish.yes_no(goldfish.fresh_water)} "
          f"Есть ли у неё хвост? {goldfish.yes_no(goldfish.tail)}")
