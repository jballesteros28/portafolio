import reflex as rx
import portafolio.data as data
from portafolio.styles.styles import Size,EmSize
from ..views.title import title
from .icon_badge import icon_badge
from .icon_buttom import icon_buttom


def info_detail(heading="", text1="", text2="",text3="") -> rx.Component:
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
                    ),
                    rx.hstack(
                        rx.badge(
                            rx.image(
                                src= data.LOGO_PYTHON,
                                height=EmSize.LARGE.value
                            ),
                            "Python",
                            radius="full",
                            color_scheme="gray"
                        ),
                        rx.badge(
                            rx.image(
                                src= data.LOGO_REFLEX,
                                height=EmSize.LARGE.value,
                                border_radius="50px"
                            ),
                            "Reflex",
                            radius="full",
                            color_scheme="gray"
                        ),
                    ),
                    rx.hstack(
                        icon_buttom(
                            "link",
                            data.URL_JUANDEV,
                        ),
                        icon_buttom(
                            "github",
                            data.URL_JUANDEV_GITHUB,
                        )
                    )
                )
            ),
            width="100%"
        )
    )