class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            alive = True
            while alive and asteroid<0 and stack and stack[-1]>0:
                s=asteroid+stack[-1]
                if stack[-1]<-asteroid:
                    stack.pop()
                    continue
                elif stack[-1]==-asteroid:
                    stack.pop()
                alive=False
            if alive:
                stack.append(asteroid)
        return stack
