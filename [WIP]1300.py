class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        arr = sorted(arr)
        prefix_sum = []
        current_sum = 0
        for x in arr:
            current_sum += x
            prefix_sum.append(current_sum)

        
        min_val = 0
        max_val = arr[-1]

        answer_so_far = 0
        while (medium != answer_so_far):
            medium = min_val + (max_val-min_val)/2


            val = calculate_answer_with_x(medium)
            new_answer = target-val
            if abs(new_answer) = abs(answer_so_far):
                break

            if abs(new_answer) < abs(answer_so_far):
                answer_so_far = abs(new_answer)
                
                if new_answer < 0:
                    min_val = medium
                if new_answer > 0:
                    max_val = medium
                if new_answer == 0:
                    break



            
    def calculate_answer_with_x(self,x):
        right_bisect =  bisect.bisect_right(arr)
        val = prefix_sum[right_bisect-1] + x*max(0,l-right_bisect)
        return val
        


        
class TestCase:
    def __init__(self, arr, target, answer):
        self.arr = arr
        self.target = target
        self.answer = answer

def main():
    tc = [TestCase([4,9,3], 10, 3), TestCase([2,3,5], 10, 5)]
    
    s = Solution()
    for x in tc:
        got = s.findBestValue(x.arr,x.target)
        if got == x.answer:
            print("tc ", x , "pass")
        else:
            print("answer expected {0}, but got {1}".format(x.answer, got))
            break
    

if __name__ == "__main__":
    main()

