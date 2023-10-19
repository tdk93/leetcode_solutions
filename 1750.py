class Solution:
    def minimumLength(self, s: str) -> int:
        can_remove_count = 0
        start_index = 0
        last_index = len(s)-1
        new_string = ""

        for i in range(len(s)):
            if i == 0:
                new_string += s[i]
                continue
            
            if s[i] == new_string[-1]:
                continue

            new_string += s[i]
        
        return new_string


   
class Test_Cases:
    def __init__(self):
        self.tc = ["caccc", "cc", "caabaac"]
        self.tc_answers = [2,0,1]


def main():
    s = Solution()
    test_cases = Test_Cases()
    for i in range(len(test_cases.tc)):
        print(s.minimumLength(test_cases.tc[i]))
        '''
        if s.minimumLength(test_cases.tc[i]) == test_cases.tc_answers[i]:
            print("pass")
        else:
            print("fail")
        '''

    
if __name__ == "__main__":
    main()