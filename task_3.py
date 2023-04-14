class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def __str__(self):
        return f"Сотрудник: {self.get_full_name()}, должность: {self.position}, доход: {self.get_total_income()}"


worker = Position("Иван", "Иванов", "менеджер", 50000, 10000)


print(worker)
print(f"Полное имя сотрудника: {worker.get_full_name()}")
print(f"Доход с учетом премии: {worker.get_total_income()}")