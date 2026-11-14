"""Tests for the vmpipe demo example."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from examples.vmpipe_demo import soma


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (-5, -7, -12),
        (2.5, 0.5, 3.0),
    ],
)
def test_soma_returns_sum(a, b, expected) -> None:
    assert soma(a, b) == expected
