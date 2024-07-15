import inspect
import os
from pathlib import Path
import dominate
from dominate.tags import *
from dominate.util import raw

from templates import header, authors_row


# Where to save the generated file.
root_path = Path(inspect.getfile(inspect.currentframe())).parent
doc = dominate.document(title=None)

with doc.head:
    meta(charset="utf-8")
    meta(http_equiv="X-UA-Compatible", content="IE=edge")
    meta(name="viewport", content="width=device-width, initial-scale=1")
    title("AC Demo")
    link(href="/statics/bootstrap-5.2.3-dist/css/bootstrap.min.css", rel="stylesheet")
    link(href="/statics/my.css", rel="stylesheet")

with doc:
    # Title and Metadata:
    with div(cls="container").add(div(cls="row")):
        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            header(
                title="Diffusion-Based Method with TTS Guidance for Foreign Accent Conversion",
                sub="",
            )
            br()
            from abstract import section_abstract

            section_abstract()
            p(
                "You can download all audio files on this page by cloning this annoymous ",
                a(
                    "github repository",
                    href="https://github.com/diff-fac/diff-fac.github.io",
                ),
                ".",
                cls="lead",
            )

        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            from naturalness import get_table

            h3("Naturalness")
            p(
                """
                In this task, we evaluate the naturalness of samples derived from the following systems.
                """,
                cls="lead",
            )
            get_table()
            p(
                "* please scroll horizontally to explore additional columns in the table.",
                cls="lead",
            )

        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            from accentedness import get_table

            h3("Accentedness Reduction")
            p(
                """
                In this task, we evaluate the accentedness reduction achieved by the four systems.
                """,
                cls="lead",
            )
            get_table()
            p(
                "* please scroll horizontally to explore additional columns in the table.",
                cls="lead",
            )

        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            from spksim import get_table

            h3("Speaker Similarity")
            p(
                """
                In this task, we evaluate the speaker characteristics preserved by the four systems.
                """,
                cls="lead",
            )
            get_table()
            p(
                "* please scroll horizontally to explore additional columns in the table.",
                cls="lead",
            )

with doc.footer:
    script(src="/statics/jquery/jquery-3.7.1.slim.min.js")
    script(src="/statics/bootstrap-5.2.3-dist/bootstrap.min.js")

# Script for allowing only one audio to play at the same time:
doc.children.append(
    script(
        raw(
            """ $(function(){
        $("audio").on("play", function() {
            $("audio").not(this).each(function(index, audio) {
                audio.pause();
                audio.currentTime = 0;
            });
        });
    }); """
        )
    )
)

with open(root_path / "index.html", "w") as index:
    index.write(doc.render())
