import types
from alpGenerator import *


"""
코드의 정상적인 동작유무를 확인하기 위한 파이썬 테스트 파일이다.
테스트는 pytest 모듈을 활용한다.
"""


def test_alpGenerator():
    alps = alpGenerator()
    assert type(alps) == types.GeneratorType
    assert len(list(alps)) == 26 * 26 * 26


test_alpGenerator()