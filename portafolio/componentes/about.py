import reflex as rx
from ..views.title import title



class State(rx.State):
    """The app state."""

    ...


def about(text: str, description: str) -> rx.Component:
    return rx.flex(
        rx.vstack(
            title(text),
            rx.text(
                description
            )
        )
    )