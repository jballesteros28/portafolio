import reflex as rx
import portafolio.data as data
from ..componentes.link_buttom import link_buttom
from ..views.title import title



class State(rx.State):
    """The app state."""

    ...


def tech_stack() -> rx.Component:
    return rx.vstack(
        title("Tecnologias"),
        rx.flex(
            rx.hstack(
                link_buttom(
                    data.LOGO_PYTHON,
                    data.URL_PYTHON,
                    "python"
                ),
                link_buttom(
                    data.LOGO_REFLEX,
                    data.URL_REFLEX,
                    "Reflex"
                ),
                link_buttom(
                    data.LOGO_FASTAPI,
                    data.URL_FASTAPI,
                    "Fast-API"
                )
            ),
            flex_wrap="wrap",
        )
    )