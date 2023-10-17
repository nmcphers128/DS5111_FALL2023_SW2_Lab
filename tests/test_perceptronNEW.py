import sys
import pytest
sys.path.append(".")

from bin.perceptron import Perceptron

@pytest.mark.parametrize(["trainingset", "labels"],
            [
                ([[1,1],[1,0],[0,1],[0,0]], [1,1,1,0]),
                ([[2,2],[2,1],[1,2],[1,1]], [1,1,1,0]),
                ([[3,3],[3,2],[2,3],[2,2]], [1,1,1,0])
            ])

        
def test_perceptron_batch(trainingset, labels):
    the_perceptron = Perceptron()

    trainSet = trainingset
    labels = labels
    
    the_perceptron.train(trainSet, labels)

    for idx, item in enumerate(trainSet):
#        print(f"training data is [{item}] and label is [{labels[idx]}]")
        assert the_perceptron.predict(item) ==  labels[idx], f"training data is [{item}] and label is [{labels[idx]}]"

