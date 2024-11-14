# Copyright 2025 Anjandev Momi
# SPDX-License-Identifier: GPL-3.0-or-later
from pmb.helpers.package import remove_operators


def test_remove_operators():
    """Test remove_operators function"""
    assert remove_operators("sxmo-utils") == "sxmo-utils"

    assert remove_operators("sxmo-utils>10.0.0") == "sxmo-utils"
    assert remove_operators("sxmo-utils>=10.0.0") == "sxmo-utils"
    assert remove_operators("sxmo-utils<=10.0.0") == "sxmo-utils"
    assert remove_operators("sxmo-utils=10.0.0") == "sxmo-utils"
    assert remove_operators("sxmo-utils<10.0.0") == "sxmo-utils"
    assert remove_operators("sxmo-utils~10.0.0") == "sxmo-utils"
