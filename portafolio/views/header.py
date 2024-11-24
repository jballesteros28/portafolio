import reflex as rx
import portafolio.data as data
from portafolio.styles.styles import Size
from portafolio.componentes.icon_buttom import icon_buttom
from portafolio.views.title import title



class State(rx.State):
    """The app state."""

    ...


def header() -> rx.Component:
    # Welcome Page (Index)
    return rx.hstack(
            rx.avatar(
                src= data.AVATAR,
                size= Size.BIG.value,
                radius="full"
            ),
            rx.vstack(
                rx.vstack(
                    title("Juan David Ballesteros Bayona",True),
                    title("programador frontend y backend"),
                    spacing="0",
                    width="100%"
                ),
                rx.text(
                    rx.icon("map-pin"),
                    "Buenos Aires, Argentina",
                    display="inherit"
                ),
                rx.flex(
                    rx.hstack(
                        icon_buttom(
                            "mail",
                            f"mailto:{data.MAIL}",
                            "juandavidballesteros bayona@gmail.com",
                            True
                        ),
                        icon_buttom(
                            "file-text",
                            data.URL_CV,
                        ),
                        icon_buttom(
                            "github",
                            data.URL_GITHUB
                        ),
                        icon_buttom(
                            "linkedin",
                            data.URL_LINKEDIN
                        ),
                        flex_wrap="wrap",
                    )
                ),
                width="100%"
            ),
            width="100%"
        ),