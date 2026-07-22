class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        cars=sorted(zip(position,speed),reverse=True)
        for pos, spd in cars:
            time = (target - pos) / spd

            if not fleets or time > fleets[-1]:
                fleets.append(time)
        return len(fleets)