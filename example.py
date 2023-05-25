""" how can you store an array of arrays so you can reuse them later  """
# DEFINE ARRAYS, could come from a differnt source


ARRS = [
    [1,2,3,4,5], # index = 0
    [11,22,33,44,55], # index = 1
    [555,666,7777,1211] # index = 3
] 

# ----------------------- NAIVE APPROACH
OUTER_SCOPE = {}

def store_arrays(arrays):
    base_name = 'array'
    for index, array in enumerate(arrays):
    # loop arrays and get current index
        # create a string out of base_name and index to use as name
        name = f'{base_name}_{index}'
        # store in outer storage dictionary
        OUTER_SCOPE[name] = array


def naive_approach():
    # create storage
    store_arrays(ARRS)
    
    # print result stored in outer scope
    for k, v in OUTER_SCOPE.items():
        print(f'{k} ==> {v}')

# ----------------------- CLEANER APPROACH
""" this is cleaner because our method
    returns the result
    instead of writing to an outer variable
"""

def store_arrays_and_return(arrays):
    result = {} # initialise empty dictionary
    
    base_name = 'array' # define basename
    
    # loop arrays and get current index
    for index, array in enumerate(arrays):
        name = f'{base_name}_{index}'
        result[name] = array

    return result


def cleaner_approach():
    # create storage
    result = store_arrays_and_return(ARRS)
    for k, v in result.items():
        print(f'{k} ==> {v}')



# ----------------------- LIST COMP APPROACH

def store_arrays_and_return_listcomp(arrays, base_name=False):
    """ this is the same as the cleaner_approach but 
        even less lines of code
        this also allows us to use a different base_name if we want to
    """
    if not base_name:
        base_name = 'array' # define basename
    return {f'{base_name}_{index}' : array for index, array in enumerate(arrays)}  
    


def list_comp_approach(base_name=False):
    # create storage
    result = store_arrays_and_return_listcomp(ARRS, base_name)
    for k, v in result.items():
        print(f'{k} ==> {v}')



# ----------------------- CLASS BASED APPROACH
class Storage:
    # current_index =Count(0) <- python built in

    def __init__(self, base_name='array'):
        self.current_index = 0
        self.elements = {}
        self.base_name = base_name

    def add_arrays(self, arrays):
        for array in arrays:
            self._add_array(array)

    @property
    def current_name(self):
        return f'{self.base_name}_{self.current_index}' 

    def _add_array(self, array):
        # add array to stored arrays
        self.elements[self.current_name] = array
        # increase index
        self.current_index+= 1



def class_based_approach():
    storage = Storage()
    storage.add_arrays(ARRS)
    # we could even add more to our existing storage:
    storage.add_arrays(ARRS[::-1]) 
    for k, v in storage.elements.items():
        print(f'{k} ==> {v}')

def main():
    print('# NAIVE APPROACH #')
    naive_approach()
    
    print('# CLEANER APPROACH #')
    cleaner_approach()
    
    print('# LIST COMP APPROACH #')
    list_comp_approach()
    
    print('# LIST COMP APPROACH WITH BASENAME #')
    list_comp_approach('filename123')
    
    print('# CLASS APPROACH #')

    class_based_approach()

if __name__ == "__main__":
    main()
