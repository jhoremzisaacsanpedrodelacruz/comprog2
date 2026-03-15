
students = {}

def add_student(name, scores):
    students[name] = scores

def compute_average(scores):
    return sum(scores) / len(scores)

def leaderboard():
    ranking = []

    for name, scores in students.items():
        avg = compute_average(scores)
        ranking.append((name, avg))

    ranking.sort(key=lambda x: x[1], reverse=True)

    return ranking