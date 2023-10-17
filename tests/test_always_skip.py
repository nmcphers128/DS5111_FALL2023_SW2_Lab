import pytest
import sys
sys.path.append(".")

import os

@pytest.mark.skip(reason="This test is not yet ready for prime time my brother!")
def test_condition_ALWAYSskip():

    trainSet = [[1,1],[1,0],[0,1],[0,0]]
    labels = [0,1,1,0]
    
    for idx, item in enumerate(trainSet):
        print(f"training data is [{item}] and label is [{labels[idx]}]")
#        assert the_perceptron.predict(item) ==  labels[idx], f"training data is [{item}] and label is [{labels[idx]}]"

