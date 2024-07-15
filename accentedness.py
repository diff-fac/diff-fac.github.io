from dominate.tags import *


systems = [
    ("Source", "Reference"),
    ("Baseline", "baseline"),
    ("Proposed", "diff_phnLoss_predPE"),
    ("Ablation-1", "diff_frmLoss_predPE"),
    ("Ablation-2", "diff_phnLoss_origPE"),
]

samples = [
    (
        "NCC",
        "arctic_a0397",
        "call me that again, he murmured ecstatically",
    ),
    (
        "BWC",
        "arctic_b0152",
        "ow, a wild dog, he growled.",
    ),
    (
        "LXC",
        "arctic_a0397",
        "call me that again, he murmured ecstatically",
    ),
    (
        "TXHC",
        "arctic_a0459",
        "there's too much of the schoolboy in me.",
    ),
    (
        "NCC",
        "arctic_b0138",
        "and then, steadily, he began to chew.",
    ),
    (
        "BWC",
        "arctic_b0224",
        "but to culture the revolution thus far had exhausted the junta.",
    ),
    (
        "LXC",
        "arctic_b0337",
        "here he got a fresh thrill.",
    ),
    (
        "TXHC",
        "arctic_b0517",
        "eggshell is not good to eat.",
    ),
]


def get_table(
    root: str = "./samples/accentedness",
    control_width_px=240,
) -> html_tag:
    _div = div(cls="table-responsive", style="overflow-x: scroll").add(
        table(cls="table table-sm")
    )
    with _div:
        with thead():
            with tr():
                th("Speaker", scope="col")
                for spk, _, _ in samples:
                    th(spk, scope="col")
        with tbody():
            with tr():
                th(
                    "Text",
                    scope="row",
                    style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                )
                for _, _, text in samples:
                    td(p(text))

            for sys_name, sys_id in systems:
                with tr():
                    th(
                        sys_name,
                        scope="row",
                        style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                    )
                    for spk, key, _ in samples:
                        td(
                            audio(
                                source(
                                    src=f"{root}/{spk}-{key}-{sys_id}.wav",
                                    type="audio/wav",
                                ),
                                controls="",
                                style=f"width: {control_width_px:d}px",
                                preload="none",
                            )
                        )
    return _div
