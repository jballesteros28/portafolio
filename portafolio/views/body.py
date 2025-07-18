import reflex as rx
import portafolio.data as data
from portafolio.styles.styles import IMAGE_HEIGHT, Size
from portafolio.componentes.info_detail import info_detail
from portafolio.views.tech_stack import tech_stack
from .info_experience import info_experience




def body() -> rx.Component:
    return rx.vstack(
        tech_stack(),
        rx.hstack(
            rx.vstack(
                info_detail(
                    "Proyectos",
                    "Gestor de tareas personales (To-Do List):",
                    "Desarrollo de una aplicación web moderna y segura para la gestión de tareas personales.",
                    data.DESCRIPCION_LIST_TO_DO,
                    data.URL_LIST_TO_DO,
                    data.URL_LIST_TO_DO_GITHUB
                ),
                width="30em"
            ),
            rx.spacer(),
            rx.card(
                rx.inset(
                    rx.image(
                        src= "list_to_do.png",
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
                    "Página de Links",
                    "",
                    "Página de enlaces personal (my-links-page)",
                    data.DESCRIPCION_PAGINA_LINKS,
                    data.URL_LINKS_PAGE,
                    data.URL_LINKS_PAGE_GITHUB
                ),
                width="30em"
            ),
            rx.spacer(),
            rx.card(
                rx.inset(
                    rx.image(
                        src= "links_page.png",
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
                    "portafolio",
                    "",
                    "Portafolio web profesional (portafolio):",
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
                        src= "portafolio.png",
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