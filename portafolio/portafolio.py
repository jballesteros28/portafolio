

import reflex as rx
from portafolio.views.header import header
from portafolio.views.body import body
from .views.footer import footer
from portafolio.componentes.about import about
import portafolio.data as data
from portafolio.styles.styles import Size,EmSize,MAX_WIDTH,STYLESHEETS,BASE_STYLE   
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            header(),
            about(
                "Sobre mi",
                data.DESCRIPTION
            ),
            rx.divider(),
            body(),
            rx.divider(),
            footer(),
            spacing=Size.MEDIUM.value,
            padding_x=EmSize.BIG.value,
            padding_y=EmSize.SUPER_BIG.value,
            max_width=MAX_WIDTH,
            width="100%"
        )
    )




app = rx.App(
    theme=rx.theme(
        appearance="inherit",
        radius="full",
        accent_color="mint",
        panelBackground="solid",
    ),
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
)
app.add_page(index)
