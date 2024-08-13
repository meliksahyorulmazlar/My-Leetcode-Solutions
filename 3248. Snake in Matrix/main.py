class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        total = (n**2)-1
        current = 0
        for command in commands:
            if command == "UP":
                current -= n
            elif command == "DOWN":
                current += n
            elif command ==  "LEFT":
                current -= 1
            else:
                current += 1
        return current
