from textual.app import App
from textual.widget import Widget
from rich.text import Text

from snake_game import SnakeGame, Direction


class SnakeWidget(Widget):
    """Renderable widget that draws the game grid as text."""

    def __init__(self, game: SnakeGame, **kwargs):
        super().__init__(**kwargs)
        self.game = game

    def render(self) -> Text:
        w = self.game.width
        h = self.game.height

        # helper to get cell char and style
        def cell_at(r: int, c: int):
            # snake first (so head/body render above food)
            for idx, (sr, sc) in enumerate(self.game.snake):
                if (r, c) == (sr, sc):
                    if idx == len(self.game.snake) - 1:
                        return "X", "bold white on red"
                    return "O", "white on green"

            # only show the current food (strict sequence): food at food_index
            if self.game.food_index < len(self.game.food):
                fr, fc = self.game.food[self.game.food_index]
                if (r, c) == (fr, fc):
                    return "*", "yellow"

            return " ", "dim"

        text = Text()

        # layout padding
        top_padding = 2  # number of blank lines above header
        left_padding = 4  # number of spaces left of the board/header

        # add top padding
        for _ in range(top_padding):
            text.append("\n")

        # Header: title and score with left padding
        header = " " * left_padding + " Snake Game "
        score = f"  Score: {self.game.score}"
        text.append(header, style="bold magenta")
        text.append(score, style="bold cyan")
        text.append("\n\n")

        # colored separator (top border) with left padding
        sep = "+" + ("---+" * w)
        text.append(" " * left_padding + sep + "\n", style="bright_blue")

        for r in range(h):
            # left padding and left border
            text.append(" " * left_padding)
            text.append("|", style="bright_blue")
            for c in range(w):
                ch, style = cell_at(r, c)
                text.append(f" {ch} ", style=style)
                # vertical border between cells
                text.append("|", style="bright_blue")
            text.append("\n")
            # row separator with left padding
            text.append(" " * left_padding + sep + "\n", style="bright_blue")

        return text


class SnakeApp(App):
    """Minimal Textual app for SnakeGame.

    Controls:
    - Arrow keys: move
    - q: quit
    """

    async def on_mount(self) -> None:
        # create game and widget
        self.game = SnakeGame(10, 10, [[1, 2], [0, 1], [2, 2]])
        self.snake_widget = SnakeWidget(self.game)
        # use mount for broader Textual compatibility
        await self.mount(self.snake_widget)
        try:
            # `set_focus` may be sync in some Textual versions; call without await
            self.set_focus(self.snake_widget)
        except Exception:
            # some textual versions handle focus differently; ignore if unsupported
            pass

    def on_key(self, event) -> None:
        key = getattr(event, "key", None)
        if key in ("q", "Q"):
            self.exit()
            return

        mapping = {
            "up": Direction.UP,
            "down": Direction.DOWN,
            "left": Direction.LEFT,
            "right": Direction.RIGHT,
        }

        if key in mapping:
            result = self.game.move(mapping[key])
            # refresh widget to show new state
            self.snake_widget.refresh()
            if result == -1:
                # game over
                self.exit(message="Game over")


if __name__ == "__main__":
    SnakeApp().run()
