import os


def setup(app):
    if hasattr(app, "add_html_theme"):
        app.add_html_theme(
            "library",
            os.path.abspath(os.path.dirname(__file__))
        )
