import reflex as rx
import portafolio.data as data
from portafolio.styles.styles import IMAGE_HEIGHT, Size
from portafolio.componentes.info_detail import info_detail
from portafolio.views.tech_stack import tech_stack
from .info_experience import info_experience




def body() -> rx.Component:
    return rx.vstack(
        tech_stack(),
        info_experience(
            "Experiencia",
            "Supermercados Dia",
            "Encargado Tienda",
            "Mi experiencia"
        ),
        rx.hstack(
            rx.vstack(
                info_detail(
                    "Proyectos",
                    "Pagina de links",
                    "una pagina de links responsive y configurable",
                    "Herramienta personal de acceso"
                )
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
                    "Un portafolio de programador responsive y personalizable",
                    "Herramienta personal de acceso"
                )
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
            "Formacion",
            "Instituto Tecnico Jose Eugenio Martinez(secundaria)",
            "Bachiller Tecnico en Sistemas",
            "Aprendi cosas"
        ),
        spacing="7",
        width="100%"
    )