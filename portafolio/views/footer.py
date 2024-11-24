import reflex as rx
from portafolio.componentes.icon_buttom import icon_buttom
import portafolio.data as data




def footer() -> rx.Component:
    return rx.vstack(
        rx.text("Juan David Ballesteros Bayona"),
        rx.hstack(
            rx.flex(
                rx.hstack(
                    icon_buttom(
                        "mail",
                        f"mailto:{data.MAIL}",
                        "juandavidballesterosbayona@gmail.com",
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
        ),
        width="100%"
    )