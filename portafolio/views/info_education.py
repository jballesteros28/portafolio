import reflex as rx
from portafolio.styles.styles import EmSize,Size
from ..componentes.icon_badge import icon_badge
from .title import title

def info_education(heading="", text1="", text2="",text3="") -> rx.Component:
    return rx.flex(
        rx.vstack(
            title(heading),
            rx.hstack(
                icon_badge("user"),
                rx.vstack(
                    rx.text.strong(text1),
                    rx.text.strong(text2),
                    rx.text.strong(text3),
                    
                )
            ),
            width="100%"
        ),
        width="100%"
    )