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
        "arctic_a0070",
        "he would first hunt up gregson and begin his work there.",
    ),
    (
        "BWC",
        "arctic_b0200",
        "we leave the eventuality to time and law.",
    ),
    (
        "LXC",
        "arctic_a0217",
        "oppressive as the heat had been, it was now even more oppressive.",
    ),
    (
        "TXHC",
        "arctic_a0199",
        "thus had the raw wilderness prepared him for this day.",
    ),
    (
        "NCC",
        "arctic_b0465",
        "but such divergence of opinion would constitute no menace to society.",
    ),
    (
        "BWC",
        "arctic_a0232",
        "i cannot follow you, she said.",
    ),
    (
        "LXC",
        "arctic_a0064",
        "the fourth and fifth days passed without any developments.",
    ),
    (
        "TXHC",
        "arctic_b0462",
        "one guess will do, ernest retorted.",
    ),
]


def get_table(
    root: str = "./samples/spksim",
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
