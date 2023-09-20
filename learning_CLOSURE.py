# inspired the_dice_game problems I found different approach, it is called "CLOSURE"

def fib():
    x1 = 0
    x2 = 1
    def get_next_number():
        nonlocal x1, x2  #we can tell the inner function of a closure that the variable should not be considered as a “local variable”,
        #by using the nonlocal keyword
        x3 = x1 + x2
        x1, x2 = x2, x3
        return x3
    return get_next_number


fibonacci = fib()
for i in range(2,21):
    num = fibonacci()
    print(f'The {i}th Fibonacci number is {num}')

#=========================---anotrher_example---===============================


students = {
    'Alice': 98,
    'Bob': 67,
    'Chris': 85,
    'David': 75,
    'Ella': 54,
    'Fiona': 35,
    'Grace': 69
}

def make_student_classifier(lower_bound, upper_bound):
    def classify_student(exam_dict):
        return {k:v for (k,v) in exam_dict.items() if lower_bound <= v < upper_bound}
    return classify_student

grade_A = make_student_classifier(80, 100)
grade_B = make_student_classifier(70, 80)
grade_C = make_student_classifier(50, 70)
grade_D = make_student_classifier(0, 50)

print(grade_A(students))
print(grade_B(students))
print(grade_C(students))
print(grade_D(students))