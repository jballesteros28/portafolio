from enum import Enum
import reflex as rx
from .colors import color

MAX_WIDTH = "900px"
IMAGE_HEIGHT = "175px"


class EmSize(Enum):
    ZERO="0em"
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em"
    VERY_BIG="2.5em"
    SUPER_BIG="4em"


class Size(Enum):
    ZERO = "0"
    SMALL = "2"  # 8px
    DEFAULT = "4"  # 16px/1em
    MEDIUM = "6"  # 32px
    BIG = "8"  # 48px


STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"
]

BASE_STYLE = {
    "white_space": "normal",
    rx.badge: {
        "--cursor-button": "pointer",
        "white_space": "normal",
        "hover":{
            "text_decoration":"none",
        }
    },
    rx.link:{
        "text_decoration":"none",
        "_hover":{}
    },
}