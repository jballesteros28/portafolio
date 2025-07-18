import reflex as rx
import portafolio.data as data
from ..componentes.link_buttom import link_buttom
from ..views.title import title



class State(rx.State):
    """The app state."""

    ...


def tech_stack() -> rx.Component:
    return rx.vstack(
        title("Tecnologías"),
        rx.flex(
            rx.hstack(
                link_buttom(
                    data.LOGO_PYTHON,
                    data.URL_PYTHON,
                    "Python"
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
                ),
                link_buttom(
                    data.LOGO_REACT,
                    data.URL_PYTHON,
                    "ReactJS"
                ),
                link_buttom(
                    data.LOGO_CSS,
                    data.URL_PYTHON,
                    "Css"
                ),
                link_buttom(
                    data.LOGO_JAVASCRIPT,
                    data.URL_PYTHON,
                    "Javascript"
                ),
                display= "flex",
                flex_wrap= "wrap"
            ),
            flex_wrap="wrap",
        )
    )