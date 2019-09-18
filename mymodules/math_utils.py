def average_grade(roster):
    total = 0
    for i in roster:
        total += i.get_grade()
        average = total/len(roster)
    return average
