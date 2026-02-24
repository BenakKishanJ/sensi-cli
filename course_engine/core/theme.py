"""
theme.py

Centralized ANSI color and styling configuration
for Sensei CLI.

No other file should hardcode ANSI escape codes.
All styling must pass through this module.
"""

class Theme:
    # === Base Colors (Kanagawa-inspired) ===
    BG = "\033[48;5;235m"        # Dark charcoal background
    FG = "\033[38;5;223m"        # Soft cream foreground

    ACCENT_BLUE = "\033[38;5;110m"
    ACCENT_GOLD = "\033[38;5;180m"
    ACCENT_RED = "\033[38;5;167m"
    ACCENT_GREEN = "\033[38;5;150m"
    ACCENT_PURPLE = "\033[38;5;176m"

    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

    # === Utility Methods ===

    @staticmethod
    def apply(text: str, *styles: str) -> str:
        """
        Apply one or more ANSI styles to text.
        Example:
            Theme.apply("Hello", Theme.ACCENT_BLUE, Theme.BOLD)
        """
        return f"{''.join(styles)}{text}{Theme.RESET}"

    @staticmethod
    def divider(width: int = 60, char: str = "─") -> str:
        return Theme.apply(char * width, Theme.DIM)

    @staticmethod
    def title(text: str) -> str:
        return Theme.apply(text, Theme.BOLD, Theme.ACCENT_GOLD)

    @staticmethod
    def success(text: str) -> str:
        return Theme.apply(text, Theme.ACCENT_GREEN, Theme.BOLD)

    @staticmethod
    def error(text: str) -> str:
        return Theme.apply(text, Theme.ACCENT_RED, Theme.BOLD)

    @staticmethod
    def info(text: str) -> str:
        return Theme.apply(text, Theme.ACCENT_BLUE)

    @staticmethod
    def highlight(text: str) -> str:
        return Theme.apply(text, Theme.ACCENT_PURPLE)
