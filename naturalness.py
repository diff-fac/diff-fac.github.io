from dominate.tags import *


systems = [
    ("Source", "source"),
    ("TTS (aligned)", "tts_aligned"),
    ("Baseline", "baseline"),
    ("Proposed", "diff_phnLoss_predPE"),
    ("Ablation-1", "diff_frmLoss_predPE"),
    ("Ablation-2", "diff_phnLoss_origPE"),
]

samples = [
    (
        "NCC",
        "arctic_a0042",
        "how could he explain his possession of the sketch.",
    ),
    (
        "BWC",
        "arctic_a0541",
        "the warden with a quart of champagne.",
    ),
    (
        "LXC",
        "arctic_b0152",
        "ow, a wild dog, he growled.",
    ),
    (
        "TXHC",
        "arctic_a0239",
        "he cried in such genuine dismay that she broke into hearty laughter.",
    ),
    (
        "NCC",
        "arctic_b0020",
        "he made no reply as he waited for whittemore to continue.",
    ),
    (
        "BWC",
        "arctic_b0462",
        "one guess will do, ernest retorted.",
    ),
    (
        "LXC",
        "arctic_b0156",
        "for that reason le beau had chosen him to fight the big fight.",
    ),
    (
        "TXHC",
        "arctic_b0078",
        "there was pride and strength, the ring of triumph in his voice.",
    ),
]


def get_table(
    root: str = "./samples/naturalness",
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
