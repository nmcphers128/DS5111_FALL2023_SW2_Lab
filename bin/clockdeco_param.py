import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):  
    def decorate(func):      
        def clocked(*_args): 
            t0 = time.time()
            _result = func(*_args)  
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)  
            result = repr(_result)  
            print(fmt.format(**locals()))  
            return _result  
        return clocked  
    return decorate  

@clock()
def snooze5111(seconds):
    time.sleep(seconds)
    return str(seconds)


#print("Hello this is the line BEFORE __main__")


if __name__ == '__main__':


#    print("Hello this is the line AFTER __main__")
    
    @clock()  
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)
        
