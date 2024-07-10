class Result:
    def __init__(self):
        self.error = None
        self.value = None
        self.is_success = False
        
    @staticmethod
    def success(value = None):
        result = Result()
        result.value = value
        result.is_success = True
        return result
    
    @staticmethod
    def failure(error):
        result = Result()
        result.error = error
        result.is_success = False
        return result
    def is_failure(self):
        return not self.is_success