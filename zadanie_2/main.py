from uczelnia.student import Student

if __name__ == "__main__":
    student_1 = Student("Jan Kowalski", [60, 70, 80, 55])
    student_2 = Student("Anna Nowak", [40, 50, 30, 45])

    print(student_1)
    print(f"Czy {student_1.imie_i_nazwisko} zdał? {student_1.czy_zdal()}")

    print(student_2)
    print(f"Czy {student_2.imie_i_nazwisko} zdała? {student_2.czy_zdal()}")