class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        total=0
        cur=0
        for req in requests:
            total+=abs(req-cur)
            cur=req
        return total
        