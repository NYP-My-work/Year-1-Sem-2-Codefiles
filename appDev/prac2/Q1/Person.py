class Person():
    def __init__(self,name,nric):
        self.__name=name
        self.__nric=nric
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.__name=name
    def get_nric(self):
        return self.nric
    def set_nric(self,nric):
        self.__nric=nric