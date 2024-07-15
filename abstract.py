from dominate.tags import *
from dominate.util import raw


def section_abstract():
    h3("Abstract")
    p(
        raw("""
        Accent conversion (AC) aims to alter the accent of spoken language while preserving the original content and speaker characteristics. While any accent can be selected as a target, foreign accent conversion (FAC) that focuses on L2 speakers is particularly noteworthy due to its wide-ranging applications. Compared to general voice conversion tasks, which focus on speaker conversion, research related to accent conversion is relatively scarce, and the audio quality is often limited. In this article, we introduce a diffusion decoder into the conventional TTS-guided accent conversion framework and propose a phoneme-level acoustic-linguistic alignment strategy. Subjective evaluations on the Chinese-accent source speech confirm that the proposed method outperforms the baseline in terms of speech naturalness, accentedness, and speaker similarity.
        """),
        _class="lead"
    )