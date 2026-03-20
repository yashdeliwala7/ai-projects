def greet(name):

    return f"Hello, {name}!"



def add_numbers(a,b):
    return a+b


def get_even_numbers(numbers):
    return[num for num in numbers if num % 2 ==0]

 

def reverse_string(text):
    return text[::-1]


 
def student_score(name,mark):
    avg=sum(mark) // len(mark)
    return f"Name: {name}, Average: {avg}"

 

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

