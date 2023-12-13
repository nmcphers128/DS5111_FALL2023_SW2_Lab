"""
This is a docstring for the MODULE and elimiates C0114
"""
class Perceptron:
    ''' This is the class docstring '''
    def __init__(self):
        ''' this is a docstring '''
        self._weights = 0.0

    def train(self, inputs, labels):
        '''This is the docstring for the train func'''
        dummied_inputs = [x + [-1] for x in inputs]
        self._weights = [0.2] * len(dummied_inputs[0])
        for _ in range(5000):
            for myinput, label in zip(dummied_inputs, labels):
                label_delta = (label - self.predict(myinput))
                for index, mycount in enumerate(myinput):
                    self._weights[index] += .1 * mycount * label_delta

    def predict(self, myinput):
        '''This is the docstring for the predict func'''
        if len(myinput) == 0:
            return None
        myinput = myinput + [-1]
        return int(0 < sum([x[0]*x[1] for x in zip(self._weights, myinput)]))
