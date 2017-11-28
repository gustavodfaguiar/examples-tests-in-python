class Calculator:
    def sum(self, value_one, value_two):
        if not all( type(value) is int for value in (value_one, value_two) ):
            raise Exception("Two integer values are expected")
        
        return value_one + value_two
