class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        self.solve(0, target, [], candidates, result)
        return result

    def solve(self, index, total, subset, candidates, result):
        if total == 0:
            result.append(subset.copy())
            return

        for i in range(index, len(candidates)):

            if i > index and candidates[i] == candidates[i-1]:
                continue

            if candidates[i] > total:
                break

            subset.append(candidates[i])
            self.solve(i+1, total-candidates[i], subset, candidates, result)
            subset.pop()
        