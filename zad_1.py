class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if not self.marks:
            return False
        return (sum(self.marks) / len(self.marks)) > 50

    def __str__(self):
        return f"Student: {self.name} (Średnia: {sum(self.marks)/len(self.marks):.2f})"

if __name__ == "__main__":
    student1 = Student("Jan Kowalski", [60, 70, 80, 55])
    student2 = Student("Anna Nowak", [40, 50, 30, 45])
    print(f"Czy {student1.name} zdał? {student1.is_passed()}")
    print(f"Czy {student2.name} zdała? {student2.is_passed()}")