import reflex as rx
from portafolio.styles.styles import EmSize,Size
from ..componentes.icon_badge import icon_badge
from .title import title

def info_experience(heading="", text1="", text2="",text3="") -> rx.Component:
    return rx.flex(
        rx.vstack(
            title(heading),
            rx.hstack(
                icon_badge("user"),
                rx.vstack(
                    rx.text.strong(text1),
                    rx.text(text2),
                    rx.text(
                        text3,
                        size=Size.SMALL.value,
                        color_scheme="gray"
                    )
                )
            )
        )
    )