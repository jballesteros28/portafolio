import reflex as rx
from portafolio.styles.styles import Size



class State(rx.State):
    """The app state."""

    ...


def title(text: str, h1=False) -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        rx.heading(
            text,
            as_="h1" if h1 else "h2",
            size=Size.BIG.value if h1 else Size.MEDIUM.value
        ),
        width="100%"
    )