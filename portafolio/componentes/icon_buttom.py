import reflex as rx
from portafolio.styles.styles import EmSize



class State(rx.State):
    """The app state."""

    ...


def icon_buttom(image: str, url: str, text="", solid= False,) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.badge(
                rx.icon(
                    tag= image,
                    height=EmSize.BIG.value,
                    margin_left="0.5em",
                ),
                rx.text(
                    text,
                    size="2",
                ),
                size="2",
                radius="full",
                variant="solid" if solid else "surface",
                width="100%"
            ),
            width="100%"
        ),
        href= url,
        is_external=True
    )