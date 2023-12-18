import bisect
import typing

class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        tupled_items = []
        for item in items:
            tupled_items.append((item[0],item[1]))
        tupled_items = sorted(tupled_items, key=lambda x: x[0])
        max_till_here_list = []
        max_so_far = -1
        for item in tupled_items:
            if item[1] > max_so_far:
                max_so_far = item[1]
            max_till_here_list.append(max_so_far)
        answer = []

        for query in queries:
            index = bisect.bisect_right(tupled_items, query, key=lambda x: x[0])
            if index == 0:
                answer.append(0)
            else:
                answer.append(max_till_here_list[index-1])


class TestCase:
    def __init__(self,items, queries):
        self.items = items
        self.queries = queries 
        


def main():
    test_cases = [TestCase([[1,2],[3,2],[2,4],[5,6],[3,5]],[1,2,3,4,5,6])] 
    s = Solution()
    s.maximumBeauty(test_cases[0].items, test_cases[0].queries)



if __name__=="__main__":
    main()