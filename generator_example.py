class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percentage):
        self.salary += (percentage / 100) * self.salary

    def __str__(self):
        return f"{self.name}, {self.age} years old, Salary: ${self.salary:.2f}"


def person_generator(person_list):
    for person in person_list:
        person.increase_salary(10)
        yield person


# Example usage:
people = [
    Person("Alice", 28, 50000),
    Person("Bob", 32, 60000),
    Person("Charlie", 22, 70000),
    Person("Diana", 30, 80000)
]

gen = person_generator(people)

for person in gen:
    print(person)
