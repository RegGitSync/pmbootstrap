# Copyright 2025 Anjandev Momi
# SPDX-License-Identifier: GPL-3.0-or-later
import pytest
from pmb.helpers.package import remove_operators, check_arch
from pmb.core.arch import Arch


def test_remove_operators():
    """Test remove_operators function"""
    assert remove_operators("sxmo-utils") == "sxmo-utils"

    assert remove_operators("sxmo-utils>10.0.0") == "sxmo-utils"
    assert remove_operators("sxmo-utils>=10.0.0") == "sxmo-utils"
    assert remove_operators("sxmo-utils<=10.0.0") == "sxmo-utils"
    assert remove_operators("sxmo-utils=10.0.0") == "sxmo-utils"
    assert remove_operators("sxmo-utils<10.0.0") == "sxmo-utils"
    assert remove_operators("sxmo-utils~10.0.0") == "sxmo-utils"


def test_check_arch(pmaports):
    with pytest.raises(RuntimeError):
        check_arch("this-package-does-not-exist", Arch.aarch64)

    assert check_arch("hello-world", Arch.aarch64)

    assert not check_arch("linux-postmarketos-qcom-sdm845", Arch.x86_64)
