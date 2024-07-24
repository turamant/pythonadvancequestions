"""Полиморфизм - это одно из фундаментальных принципов объектно-ориентированного
программирования (ООП) и ключевая особенность в Python. Он позволяет объектам разных
классов обрабатываться как объекты общего суперкласса.

Полиморфизм обеспечивает повторное использование кода, гибкость и расширяемость в ООП.

Вот простой пример на Python, демонстрирующий полиморфизм через переопределение методов:

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
        

def animal_sound(animal):
    return animal.speak()

# Создаем экземпляры Dog и Cat
dog = Dog()
cat = Cat()

# Вызываем метод speak полиморфно
print(animal_sound(dog))  # "Woof!"
print(animal_sound(cat))  # "Meow!"
В этом примере Dog и Cat являются подклассами Animal. Они оба переопределяют метод speak,
позволяя объектам этих классов по-разному реагировать на один и тот же вызов метода,
демонстрируя полиморфизм."""


class Animal:
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return "Gav-gav"
        
class Cat(Animal):
    def speak(self):
        return "Meow-meow"
    
    
def animal_sound(animal):
    return animal.speak()

if __name__ == '__main__':
    dog = Dog()
    cat = Cat()
    
    print(animal_sound(dog))
    print(animal_sound(cat))
        