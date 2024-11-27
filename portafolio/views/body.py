import reflex as rx
import portafolio.data as data
from portafolio.styles.styles import IMAGE_HEIGHT, Size
from portafolio.componentes.info_detail import info_detail
from portafolio.views.tech_stack import tech_stack
from .info_experience import info_experience




def body() -> rx.Component:
    return rx.vstack(
        tech_stack(),
        rx.vstack(
            info_experience(
                "Experiencia",
                "Supermercados Día",
                "Encargado general de Tienda",
                data.DESCRIPCION_EXPERIENCIA_DIA
            ),
            width="100%"
        ),
        rx.hstack(
            rx.vstack(
                info_detail(
                    "Proyectos",
                    "Página de Links",
                    "página de links responsive y configurable",
                    data.DESCRIPCION_PAGINA_LINKS,
                    data.URL_JUANDEV,
                    data.URL_JUANDEV_GITHUB
                ),
                width="30em"
            ),
            rx.spacer(),
            rx.card(
                rx.inset(
                    rx.image(
                        src= "preview.png",
                        height= IMAGE_HEIGHT,
                        width="100%",
                        object_fit="cover"
                    ),
                    pb=Size.DEFAULT.value
                )
            ),
            width="100%",
            wrap="wrap-reverse"
        ),
        rx.hstack(
            rx.vstack(
                info_detail(
                    "Proyectos",
                    "portafolio",
                    "Portafolio de programador responsive y personalizable",
                    data.DESCRIPCION_PORTAFOLIO,
                    data.URL_PORTAFOLIO,
                    data.URL_PORTAFOLIO_GITHUB
                ),
                width="30em"
            ),
            rx.spacer(),
            rx.card(
                rx.inset(
                    rx.image(
                        src= "preview-2.png",
                        height= IMAGE_HEIGHT,
                        width="100%",
                        object_fit="cover"
                    ),
                    pb=Size.DEFAULT.value
                )
            ),
            width="100%",
            wrap="wrap-reverse",
            align="center"
        ),
        info_experience(
            "Formación",
            "Instituto Técnico José Eugenio Martinez",
            "Bachiller Técnico en Sistemas",
            "Egresado noviembre 2018"
        ),
        spacing="7",
        width="100%"
    )