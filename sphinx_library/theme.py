from pygments.style import Style
from pygments.token import Comment
from pygments.token import Error
from pygments.token import Generic
from pygments.token import Keyword
from pygments.token import Name
from pygments.token import Number
from pygments.token import Operator
from pygments.token import String


class LibraryLight(Style):
    background_color = None
    default_style = None

    styles = {
        Comment: "italic #777",
        Keyword: "bold",
        Keyword.Type: "#458",
        Name.Builtin: "#458",
        Name.Constant: "#458",
        Name.Class: "bold #458",
        Name.Function: "bold #844",
        Name.Exception: "bold #844",
        Name.Variable: "#458",
        Number: "#099",
        Operator: "bold",
        String: "#a84",
        String.Doc: "italic #777",
        Generic.Error: "#a00",
        Generic.Emph: "italic",
        Generic.Strong: "bold",
        Generic.Prompt: "#555",
        Generic.Output: "#777",
        Generic.Traceback: "#a00",
        Error: "bg:#e3d2d2 #a61717",
    }


class LibraryDark(LibraryLight):
    background_color = None
    default_style = None

    styles = LibraryLight.styles
    styles.update(
        {
            Comment: "italic #aaa",
            Keyword.Type: "#9ad",
            Name.Builtin: "#9ad",
            Name.Constant: "#9ad",
            Name.Class: "bold #9ad",
            Name.Function: "bold #c88",
            Name.Exception: "bold #c88",
            Name.Variable: "#9ad",
            Number: "#8cc",
            String: "#ca8",
            String.Doc: "italic #aaa",
            Generic.Prompt: "#888",
            Generic.Output: "#aaa",
        }
    )
