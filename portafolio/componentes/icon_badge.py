import reflex as rx
from portafolio.styles.styles import EmSize


def icon_badge(icon) -> rx.Component:
    return rx.badge(
            rx.icon(
                tag=icon,
                size=32
            ),
            aspect_ratio="1"
        ),