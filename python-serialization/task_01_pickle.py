import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        if isinstance(name, str):
            self.name = name
        if isinstance(age, int):
            self.age = age
        if isinstance(is_student, bool):
            self.is_student = is_student


    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception:
            return None
        
    @classmethod 
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj if isinstance(obj, cls) else None
        
        except (FileNotFoundError, EOFError, pickle.UnpicklingError, AttributeError, ImportError, IndexError):
            return None
        
        except Exception:
            return None
        