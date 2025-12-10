
from collections import deque
from typing import List, Deque, Tuple
from enum import Enum


class Direction(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]) -> None:
        """Initialize the snake game.

        - `width`, `height`: board dimensions (columns, rows)
        - `food`: list of [row, col] positions for food in order

        The snake starts at (0, 0). We track the snake body in a deque
        (head at the right end) and a set of occupied positions for O(1)
        collision checks.
        """
        self.width = width
        self.height = height
        self.food: List[List[int]] = food or []
        self.score: int = 0
        self.snake: Deque[Tuple[int, int]] = deque([(0, 0)])
        self.occupied: set[Tuple[int, int]] = {(0, 0)}
        # food_index points to the next food to eat; only that food is active/visible
        self.food_index: int = 0

    def move(self, direction: Direction) -> int:
        """Move the snake in the given `Direction`.

        Returns the game's score after the move, or -1 for game over.
        The method body is left as a placeholder for now.
        """
        head = self.snake[-1]
        next_head = self._next_move(head, direction)

        # check wall collision
        nr, nc = next_head
        if not (0 <= nr < self.height and 0 <= nc < self.width):
            return -1

        tail = self.snake[0]

        # determine whether we'll grow (i.e., next food matches current food_index)
        will_grow = False
        if self.food_index < len(self.food):
            fr, fc = self.food[self.food_index]
            if next_head == (fr, fc):
                will_grow = True

        # collision with body: allowed to move into the current tail cell if the tail will move
        if next_head in self.occupied and not (not will_grow and next_head == tail):
            return -1

        # perform move
        self.snake.append(next_head)
        self.occupied.add(next_head)

        if will_grow:
            self.score += 1
            self.food_index += 1
            # tail remains (snake grows)
        else:
            # normal move: remove tail
            old_tail = self.snake.popleft()
            # use discard to avoid KeyError if occupied was modified elsewhere
            self.occupied.discard(old_tail)

        return self.score

    def get_current_location(self) -> Tuple[int, int]:
        return self.snake[-1]

    def _next_move(self, head: Tuple[int, int], direction: Direction) -> Tuple[int, int]:
        """Calculate the next head position based on the current head and direction."""
        row, col = head
        if direction == Direction.UP:
            return (row - 1, col)
        elif direction == Direction.DOWN:
            return (row + 1, col)
        elif direction == Direction.LEFT:
            return (row, col - 1)
        elif direction == Direction.RIGHT:
            return (row, col + 1)
        else:
            raise ValueError("Invalid direction")

    def _is_collision(self, position: Tuple[int, int]) -> bool:
        """Check if the given position results in a collision."""
        row, col = position
        if row < 0 or row >= self.height or col < 0 or col >= self.width:
            return True
        if position in self.occupied:
            return True
        return False





def _read_key_windows(msvcrt):
    ch = msvcrt.getch()
    if ch in (b"\x00", b"\xe0"):
        return msvcrt.getch()
    return ch


def _interactive_loop():
    try:
        import msvcrt
    except Exception:
        print("Interactive loop requires Windows (msvcrt).")
        return

    game = SnakeGame(10, 10, [[1, 2], [0, 1], [2, 2]])
    print("SnakeGame interactive demo. Use arrow keys to move; press 'q' to quit.")

    try:
        print("Waiting for key...")
        while True:
            key = _read_key_windows(msvcrt)

            if key in (b"q", b"Q"):
                print("Quit requested.")
                break

            direction = None
            if key == b"H":
                direction = Direction.UP
            elif key == b"P":
                direction = Direction.DOWN
            elif key == b"K":
                direction = Direction.LEFT
            elif key == b"M":
                direction = Direction.RIGHT
            else:
                print(f"Unrecognized key: {key!r}")
                continue

            result = game.move(direction)
            print(f"move {direction.name} to {game.get_current_location()} -> {result}")
            if result == -1:
                print("Game over!")
                break
    except KeyboardInterrupt:
        print("Interrupted, exiting.")


if __name__ == "__main__":
    _interactive_loop()
    