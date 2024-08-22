class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        position = 0
        move_dict = {"UP": -n, "DOWN": +n, "RIGHT":1, "LEFT":-1}
        for command in commands:
            position += move_dict[command]
        return position