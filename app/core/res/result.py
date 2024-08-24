## NOTE 📋:
### this is the result design pattern
####🔗 The Advantages🥳 of this design:
    ##-💪🏻 no more exceptions to handle.
    ##-💪🏻 better performance.

####🔗 The Disadvantages😓 of this design:
    ##-👎🏽 it is much harder to catch the errors

class Result:
    def __init__(self):
        self.error = None
        self.value = None
        self.is_success = False

    # when Ok ✅
    @staticmethod
    def success(value = None):
        result = Result()
        result.value = value
        result.is_success = True
        return result
    
    # when Error ❌
    @staticmethod
    def failure(error):
        result = Result()
        result.error = error
        result.is_success = False
        return result
    def is_failure(self):
        return not self.is_success