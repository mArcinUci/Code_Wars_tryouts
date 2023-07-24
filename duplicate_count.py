'''def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(duplicate_count(""), 0)
        test.assert_equals(duplicate_count("abcde"), 0)
        test.assert_equals(duplicate_count("abcdeaa"), 1)
        test.assert_equals(duplicate_count("abcdeaB"), 2)
        test.assert_equals(duplicate_count("Indivisibilities"), 2)'''



def duplicate_count(text):
    test1 = sorted([str(x).upper() for x in text])
    repeating_letters = []
    for i in range(len(test1)-1):
        if test1[i] == test1[i+1]:
            repeating_letters.append(test1[i])
    ans = len(list(set(repeating_letters)))    
    return ans



duplicate_count('abcde')