import sys
sys.path.append(".")

from bin.perceptron import Perceptron

def test_perceptron():
    the_perceptron = Perceptron()

    trainSet = [[1,1],[1,0],[0,1],[0,0]]
    labels = [1,1,1,0]
    
    the_perceptron.train(trainSet, labels)

    for idx, item in enumerate(trainSet):
#        print(f"training data is [{item}] and label is [{labels[idx]}]")
        assert the_perceptron.predict(item) ==  labels[idx], f"training data is [{item}] and label is [{labels[idx]}]"

