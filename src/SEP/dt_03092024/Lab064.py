class Car:

    def __init__(self,name,version,model):
        self.name=name
        self.version=version
        self.model=model

    def start_engine(self):
        print("starting a car with name", self.name)
        print("starting a car with version", self.version)
        print("starting a car with model", self.model)

lambo=Car("lamborghini","v2",2024)
lambo.start_engine()
tata=Car("nexon","v6",2023)
tata.start_engine()


