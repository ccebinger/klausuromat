# Externals
import copy

# Internals
from operations import BasicOperation


# A pseudo operation that exists to retrieve a snapshot of the current identifiers
class Result(BasicOperation):
    # Constructor
    def __init__(self, *args):
        # Do all the initializing stuff
        super().__init__(*args)

        # Make snapshot and disable self
        self.snapshot = copy.deepcopy(self._ids)
        self._done = True
