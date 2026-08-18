"""
Functions for cleaning a raw list of scores before analysis.

This is one small module. In a real project a module usually groups
together functions that belong to the same job, cleaning data here,
summarizing data in stats.py.
"""


def fill_missing(scores, default=0):
    """Replace missing (None) scores with a default value instead of dropping them."""
    return [default if score is None else score for score in scores]


def remove_invalid(scores):
    """Keep only numeric, non-negative scores, drop everything else."""
    cleaned = []
    for score in scores:
        if isinstance(score, (int, float)) and score >= 0:
            cleaned.append(score)
    return cleaned
