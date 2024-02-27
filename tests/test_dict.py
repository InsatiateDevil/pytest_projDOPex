from utils import dict
import pytest


def test_get_val():
    assert dict.get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
    assert dict.get_val({"vcs": "mercurial"}, "vcs", "git") == "mercurial"
    assert dict.get_val({}, "vcs", "git") == "git"
    assert dict.get_val({}, "vcs", "bazaar") == "bazaar"
