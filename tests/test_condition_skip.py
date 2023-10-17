import pytest
import sys
sys.path.append(".")

import os
# Getting all memory using os.popen()
total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
print(total_memory)
print(used_memory)
print(free_memory)

@pytest.mark.skipif(free_memory < 1280, reason = "Not enough Free Memory man!  Bailing with code 128!")

def test_condition_skipif():

    trainSet = [[1,1],[1,0],[0,1],[0,0]]
    labels = [0,1,1,0]
    
    for idx, item in enumerate(trainSet):
        print(f"training data is [{item}] and label is [{labels[idx]}]")
#        assert the_perceptron.predict(item) ==  labels[idx], f"training data is [{item}] and label is [{labels[idx]}]"

