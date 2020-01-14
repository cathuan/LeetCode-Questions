from typing import List


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # trivial case
        if candidates == []:
            return []

        d = {}
		
        for candidate in candidates:
            for i in range(1, target+1):
                if i == candidate:
                    if i not in d:
                        d[i] = [[candidate]]
                    else:
                        d[i] += [[candidate]]
						
				# see if i - candidate exists in dicationary already
                elif i - candidate > 0 and i - candidate in d:
                    for num_set in d[i - candidate]:
						# add candidate to the saved sets in d[i - candidate]
                        x = num_set + [candidate]
                        if i not in d:
                            d[i] = [x]
                        else:
                            d[i].append(x)

        if target not in d:
            return []
        else:
            return d[target]


class SolutionFaster:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size <= 0:
            return []
        path = []
        res = []
        candidates.sort()
        self.find_path(candidates, res, target, path, 0, size)
        
        return res
    
    def find_path(self, candidates, res, target, path, begin, end):
        if target == 0:
            res.append(path.copy())
        
        for i in range(begin,end):
            left_num = target - candidates[i]
            if left_num < 0:
                break
            path.append(candidates[i])
            self.find_path(candidates,res,left_num,path,i,end)
            path.pop()


if __name__ == "__main__":

    candidates = {2,3,6,7}
    target = 7
    print(Solution().combinationSum(candidates, target))