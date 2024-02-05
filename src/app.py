import random
from owlready2 import *
from queries import *

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
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(script_dir)
    onto = get_ontology(os.path.join(script_dir, "../ontology/ks_ontology.owx")).load()
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

