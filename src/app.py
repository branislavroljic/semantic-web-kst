import random
from owlready2 import *
from src.queries import *

import sys
from os import system


def display_menu():
    print("\nMenu:")
    print("1. List students")
    print("2. Find knowledge space for student")
    print("3. Find students for problem")
    print("4. Find next problems for student")
    print("5. Find students for knowledge space")
    print("6. Find optimal learning path")
    print("0. Exit")


def list_students():
    find_students()
    input("\nPress Enter to Continue\n")
    system('cls')   


def student_knowledge_space():
    student = input("Enter student's name: ")
    find_knowledge_state_for_student(student_name=student)
    input("\nPress Enter to Continue\n")
    system('cls')   


def problem_students():
    print("Select problems from list: ")
    problems = find_problems()
    while(True):
        problem = input("Enter problem: ")
        if(problems.__contains__(problem)):
            break
        else: print("Invalid problem name")
    print(problem)
    find_students_for_problem(problem)
    input("\nPress Enter to Continue\n")
    system('cls')    

def student_next_problems():
    student = input("Enter student's name: ")
    find_next_problems_for_student(student_name=student)
    input("\nPress Enter to Continue\n")
    system('cls')

def knowledge_space_students():
    problems = []
    while True:
        problem = input("Enter a problem (or 'done' to finish): ")
        if problem.lower() == 'done':
            break
        problems.append(problem)
    find_knowledge_state_for_student(problems)
    input("Press Enter to Continue\n")
    system('cls')   

def optimum_learning_path():
    first_problem = onto.search_one(hasTitle = 'A')
    optimum_path = find_optimum_learning_path(first_problem, [first_problem], set())

    print("Optimum Learning Path:", [problem.hasTitle[0] for problem in optimum_path])
    input("\nPress Enter to Continue\n")
    system('cls')   


def done():
    system('cls')   
    print("Goodbye")
    sys.exit()

if __name__ == '__main__':
    onto = get_ontology("../ontology/ks_ontology.owx").load()
    count_correct_answers("A")
   

    assessmentTest = onto.AssessmentTest("Full_Test")
    assessmentTest.hasTitle.append('Full_KS_test')
    assessmentTest.hasPart.append(onto.search_one(hasTitle = 'Question A1'))
    assessmentTest.hasPart.append(onto.search_one(hasTitle = 'Question B1'))
    assessmentTest.hasPart.append(onto.search_one(hasTitle = 'Question AB1'))
    assessmentTest.hasPart.append(onto.search_one(hasTitle = 'Question AD1'))
    assessmentTest.hasPart.append(onto.search_one(hasTitle = 'Question BC1'))
    assessmentTest.hasPart.append(onto.search_one(hasTitle = 'Question ABD1'))
    assessmentTest.hasPart.append(onto.search_one(hasTitle = 'Question ABC1'))
    assessmentTest.hasPart.append(onto.search_one(hasTitle = 'Question BCD1'))
    assessmentTest.hasPart.append(onto.search_one(hasTitle = 'Question ABCD1'))

    # student1 = onto.Student("Student1")
    # student1.hasFullName.append('Name1 Surname1')
    # student1.hasIndexNumber.append('1111/1')

    # student1_Full_Test = onto.StudentAssessmentTest("Student1_Full_Test")
    # student1_Full_Test.belongsToTest.append(assessmentTest)
    # student1_Full_Test.hasPart.append(onto.search_one(hasTitle = 'A1.1'))
    # student1_Full_Test.hasPart.append(onto.search_one(hasTitle = 'B1.1'))
    # student1_Full_Test.hasPart.append(onto.search_one(hasTitle = 'AB1.1'))
    # student1_Full_Test.hasPart.append(onto.search_one(hasTitle = 'AD1.1'))
    # student1_Full_Test.hasPart.append(onto.search_one(hasTitle = 'BC1.1'))
    # student1_Full_Test.hasPart.append(onto.search_one(hasTitle = 'ABD1.1'))
    # student1_Full_Test.hasPart.append(onto.search_one(hasTitle = 'ABC1.1'))
    # student1_Full_Test.hasPart.append(onto.search_one(hasTitle = 'BCD1.1'))
    # student1_Full_Test.hasPart.append(onto.search_one(hasTitle = 'ABCD1.1'))

    
    # student2_Full_Test = onto.StudentAssessmentTest("Student2_Full_Test")
    # student2_Full_Test.belongsToTest.append(assessmentTest)
    # student2_Full_Test.hasPart.append(onto.search_one(hasTitle = 'A1.2'))
    # student2_Full_Test.hasPart.append(onto.search_one(hasTitle = 'B1.2'))
    # student2_Full_Test.hasPart.append(onto.search_one(hasTitle = 'AB1.2'))
    # student2_Full_Test.hasPart.append(onto.search_one(hasTitle = 'AD1.2'))
    # student2_Full_Test.hasPart.append(onto.search_one(hasTitle = 'BC1.2'))
    # student2_Full_Test.hasPart.append(onto.search_one(hasTitle = 'ABD1.2'))
    # student2_Full_Test.hasPart.append(onto.search_one(hasTitle = 'ABC1.2'))
    # student2_Full_Test.hasPart.append(onto.search_one(hasTitle = 'BCD1.2'))
    # student2_Full_Test.hasPart.append(onto.search_one(hasTitle = 'ABCD1.2'))


    # student3_Full_Test = onto.StudentAssessmentTest("Student3_Full_Test")
    # student3_Full_Test.belongsToTest.append(assessmentTest)
    # student3_Full_Test.hasPart.append(onto.search_one(hasTitle = 'A1.3'))
    # student3_Full_Test.hasPart.append(onto.search_one(hasTitle = 'B1.3'))
    # student3_Full_Test.hasPart.append(onto.search_one(hasTitle = 'AB1.3'))
    # student3_Full_Test.hasPart.append(onto.search_one(hasTitle = 'AD1.3'))
    # student3_Full_Test.hasPart.append(onto.search_one(hasTitle = 'BC1.3'))
    # student3_Full_Test.hasPart.append(onto.search_one(hasTitle = 'ABD1.3'))
    # student3_Full_Test.hasPart.append(onto.search_one(hasTitle = 'ABC1.3'))
    # student3_Full_Test.hasPart.append(onto.search_one(hasTitle = 'BCD1.3'))
    # student3_Full_Test.hasPart.append(onto.search_one(hasTitle = 'ABCD1.3'))


    # for i in range(1, 11):
    #     student_name = f"Student{i}"
    #     student = onto.Student(student_name)
    #     student.hasFullName.append(f'Name{i} Surname{i}')
    #     student.hasIndexNumber.append(f'{1110+i}/{i}')

    #     student_full_test = onto.StudentAssessmentTest(f"{student_name}_Full_Test")
    #     student_full_test.belongsToTest.append(assessmentTest)
    #     random_number = random.randint(1, 3)

    #     student_full_test.hasPart.append(onto.search_one(hasTitle = f'A1.{random_number}'))
    #     student_full_test.hasPart.append(onto.search_one(hasTitle = f'B1.{random_number}'))
    #     student_full_test.hasPart.append(onto.search_one(hasTitle = f'AB1.{random_number}'))
    #     student_full_test.hasPart.append(onto.search_one(hasTitle = f'AD1.{random_number}'))
    #     student_full_test.hasPart.append(onto.search_one(hasTitle = f'BC1.{random_number}'))
    #     student_full_test.hasPart.append(onto.search_one(hasTitle = f'ABD1.{random_number}'))
    #     student_full_test.hasPart.append(onto.search_one(hasTitle = f'ABC1.{random_number}'))
    #     student_full_test.hasPart.append(onto.search_one(hasTitle = f'BCD1.{random_number}'))
    #     student_full_test.hasPart.append(onto.search_one(hasTitle = f'ABCD1.{random_number}'))

    # onto.save(file = "ks_ontology.owx", format = "rdfxml")
    # system('cls')
    while True:
            display_menu()
            choice = input("\nSelect option: ")

            if choice == "1":
                list_students()
            elif choice == "2":
                student_knowledge_space()
            elif choice == "3":
                problem_students()
            elif choice == "4":
                student_next_problems()
            elif choice == "5":
                knowledge_space_students()
            elif choice == "6":
                optimum_learning_path()
            elif choice == "0":
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please enter a number between 0 and 5.")



    # list_students()
    # print("\nKnowledge state for student: ")
    # find_knowledge_state_for_student("Milan")
    # print("\nStudents for problem: ")
    # find_students_for_problem("AB")
    # print("\nNext problems for student")
    # find_next_problems_for_student("Milan")
    # print("\nStudents for knowledge state: ")
    # find_students_for_knowladge_state(["ProblemA", "ProblemB"])

