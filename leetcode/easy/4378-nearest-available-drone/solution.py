class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        tx,ty=target
        reachable=[
            (abs(x-tx)+abs(y-ty),i)
            for i,(x,y,r) in enumerate(drones)
            if abs(x-tx)+abs(y-ty)<=r
        ]
        return min(reachable)[1] if reachable else -1        