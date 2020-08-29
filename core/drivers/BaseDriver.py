
class BaseDriver():
    con = None

    def __init__(self):
        pass
    
    def connect(self, instructions):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def query(self, parameter_list):
        raise NotImplementedError

    def create_all(self):
        raise NotImplementedError
    