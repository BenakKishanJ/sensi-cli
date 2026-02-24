"""
mascot.py

Sensei Cat system.
Handles expressions, blinking simulation, and reactions.
No rendering responsibilities — UI will call render().
"""

import itertools


class Mascot:
    """
    Stateful ASCII mascot with expression management.
    """

    def __init__(self):
        self.mode = "normal"
        self.expression = "teaching"

        # Blink cycle (simple toggle, no threading)
        self._blink_cycle = itertools.cycle(["open", "closed"])
        self._blink_state = "open"

        # Event → expression mapping
        self._expression_map = {
            "teaching": "o.o",
            "thinking": "~.~",
            "correct": "^-^",
            "incorrect": "-.-",
            "advanced": "*.*",
            "trick": "@.@",
            "judging": "=.=",
            "hardcore": "-.^",
            "zen": "._.",
        }

    # --------------------------------------------------
    # State Control
    # --------------------------------------------------

    def set_mode(self, mode: str):
        """
        Modes affect personality tone.
        Available: normal, hardcore, zen
        """
        self.mode = mode

        if mode == "hardcore":
            self.expression = "hardcore"
        elif mode == "zen":
            self.expression = "zen"
        else:
            self.expression = "teaching"

    def react(self, event: str):
        """
        Update expression based on event.
        """
        if event in self._expression_map:
            self.expression = event

    # --------------------------------------------------
    # Blink Logic
    # --------------------------------------------------

    def blink(self):
        """
        Toggle blink state.
        Call this periodically (UI/engine controlled).
        """
        self._blink_state = next(self._blink_cycle)

    # --------------------------------------------------
    # Rendering
    # --------------------------------------------------

    def render(self) -> str:
        """
        Return full ASCII mascot string.
        """
        eyes = self._get_eyes()

        return (
            "    /\\_/\\\n"
            f"   ( {eyes} )\n"
            "    > ^ <"
        )

    def _get_eyes(self) -> str:
        """
        Determine eye state based on expression + blink.
        """
        if self._blink_state == "closed":
            return "-.-"

        return self._expression_map.get(self.expression, "o.o")
