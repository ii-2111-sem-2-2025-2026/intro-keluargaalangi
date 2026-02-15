"""quiz_tests.py — w05 (SKELETON)

Replace with real tests.
"""

import pytest
from weeks.w05.answers import q01, q02, q03, q04, q05, q06, q07, q08, q09, q10, q11, q12

def _call(fn, name: str):
    try:
        return fn()
    except NotImplementedError:
        pytest.fail(f"{name} not implemented")

@pytest.mark.task(taskno=1)
def test_q01():
    _call(q01, "q01")

@pytest.mark.task(taskno=2)
def test_q02():
    _call(q02, "q02")

@pytest.mark.task(taskno=3)
def test_q03():
    _call(q03, "q03")

@pytest.mark.task(taskno=4)
def test_q04():
    _call(q04, "q04")

@pytest.mark.task(taskno=5)
def test_q05():
    _call(q05, "q05")

@pytest.mark.task(taskno=6)
def test_q06():
    _call(q06, "q06")

@pytest.mark.task(taskno=7)
def test_q07():
    _call(q07, "q07")

@pytest.mark.task(taskno=8)
def test_q08():
    _call(q08, "q08")

@pytest.mark.task(taskno=9)
def test_q09():
    _call(q09, "q09")

@pytest.mark.task(taskno=10)
def test_q10():
    _call(q10, "q10")

@pytest.mark.task(taskno=11)
def test_q11():
    _call(q11, "q11")

@pytest.mark.task(taskno=12)
def test_q12():
    _call(q12, "q12")
