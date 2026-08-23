# Question 2: Class Average Using `*args`

def class_average(*scores):
    if len(scores) == 0:
        return 0
    
    average = sum(scores) / len(scores)
    
    return round(average, 2)
    
print(class_average(80, 90, 70))
print(class_average(55, 60, 65, 70, 75))
print(class_average())
