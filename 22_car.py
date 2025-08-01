class Cars:
    def __init__(self, model):
        self.model = model

    def colors(self):
        return "4 color variants available"
    
class BMW(Cars):
    def colors(self):
        return "2 color variants available"
    
class TATA(Cars):
    def colors(self):
        return "3 color variants available"
    
b1 = BMW("M8")
t1 = TATA("Hariar")
print(f"{b1.model} has {b1.colors()}")
print(f"{t1.model} has {t1.colors()}")
#colors is model so use () but model is attribute so use nothing