# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            while True:
                if not stack or asteroid > 0 or stack[-1] < 0 or (stack[-1] > 0 and asteroid > 0):
                    stack.append(asteroid)
                    break
                elif stack[-1] > 0 and asteroid < 0:
                    if stack[-1] < abs(asteroid):
                        stack.pop()
                        if not stack:
                            stack.append(asteroid)
                            break
                        continue
                    elif stack[-1] == abs(asteroid):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    break
        
        return stack