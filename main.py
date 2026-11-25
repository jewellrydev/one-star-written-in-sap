"""One Star, Written in Sap — a make.fun entry.

Prints exactly one line, under 280 characters, in the voice of a
houseplant leaving a 1-star review of its human owner.
"""

LINE = (
    "One star. He waters me on his schedule, talks to the dog more "
    "than to me, and my cousin in the jungle grew into a tree. Would not "
    "be owned again."
)


def build_line() -> str:
    line = LINE
    assert len(line) < 280, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
