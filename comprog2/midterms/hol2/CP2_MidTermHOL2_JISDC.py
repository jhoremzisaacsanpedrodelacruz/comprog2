#MARCH 3, 2026
#CP2_MidTermHOL2_JISDC.py

import gradesJISDC as grades


def ask_name():
    return input("Enter student name (or 'done' to finish): ")


def ask_scores(name):
    return input(f"Enter scores for {name}, separated by spaces: ")


print("C: Student Grades System\n")
while True:
        
    while True:

        name = ask_name()

        if name.lower() == "done":
            break

        scores = list(map(int, ask_scores(name).split()))

        grades.add_student(name, scores)

        print()


    print("\n--- Student Results ---")

    for name, scores in grades.students.items():

        avg = grades.compute_average(scores)

        print(f"Student: {name}")
        print(f"Scores: {scores}")
        print(f"Average: {avg:.2f}")
        print(f"Highest: {max(scores)}")
        print(f"Lowest: {min(scores)}")
        print("----------------------")


    print("\n--- Leaderboard ---")

    ranking = grades.leaderboard()

    rank = 1
    for name, avg in ranking:
        print(f"{rank}. {name} - Avg: {avg:.2f}")
        rank += 1