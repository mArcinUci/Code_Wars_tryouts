'''
Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. 
Lowercase characters can be numbers. If the method gets a number as input, it should return a string.
'''
'''
"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"
'''



def to_underscore(string):
    string = str(string)
    upper_case_index = []
    for i in range(len(string)):
        if string[i].isupper() and i !=0:
            upper_case_index.append(i)
    string = string.lower()
    upper_case_index.reverse()
    new_string = [x for x in string]      
    for i in upper_case_index:
        new_string.insert(i, '_')
    string = ''.join(new_string)
    return string

print(to_underscore(1))
print(to_underscore('App7Test'))