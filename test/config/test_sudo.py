# Copyright 2025 Anjandev Momi
# SPDX-License-Identifier: GPL-3.0-or-later
import os
import pytest
import shutil
from pmb.config.sudo import which_sudo, PMB_SUDO_ENV_KEY
from _pytest.monkeypatch import MonkeyPatch


def test_sudo_override(monkeypatch: MonkeyPatch) -> None:
    """check sudo is used when PMB_SUDO_ENV_KEY is set to sudo"""
    monkeypatch.setenv(PMB_SUDO_ENV_KEY, "sudo")
    which_sudo.cache_disable()
    assert which_sudo() == "sudo"


def test_using_doas_default(monkeypatch: MonkeyPatch) -> None:
    """check doas is used when PMB_SUDO_ENV_KEY not defined"""

    def doas_path(program: str) -> str:
        return "/usr/bin/doas"

    monkeypatch.delenv(PMB_SUDO_ENV_KEY, raising=False)
    monkeypatch.setattr(shutil, "which", doas_path)
    which_sudo.cache_disable()
    assert which_sudo() == "doas"


def test_bad_env(monkeypatch: MonkeyPatch) -> None:
    """check error is raised when PMB_SUDO_ENV_KEY is misspelled"""
    monkeypatch.setenv(PMB_SUDO_ENV_KEY, "doass")
    which_sudo.cache_disable()
    with pytest.raises(RuntimeError):
        which_sudo()


def test_already_root(monkeypatch: MonkeyPatch) -> None:
    """which_sudo should be None if pmbootstrap ran as root"""

    def root_getuid() -> int:
        return 0

    which_sudo.cache_disable()
    monkeypatch.setattr(os, "getuid", root_getuid)
    assert which_sudo() is None
