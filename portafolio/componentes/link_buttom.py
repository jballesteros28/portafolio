import reflex as rx
from portafolio.styles.styles import EmSize



class State(rx.State):
    """The app state."""

    ...


def link_buttom(image: str, url: str, text="", solid= False) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.badge(
                rx.image(
                    src= image,
                    height=EmSize.BIG.value,
                    border_radius="50px",
                ),
                rx.text(
                    text,
                    size="2"
                ),
                size="2",
                radius="full",
                variant="solid" if solid else "surface"
            )
        ),
        href= url,
        is_external=True
    )