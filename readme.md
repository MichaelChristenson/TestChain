#### Test Chain Metaclass
The Test Chain Metaclass houses a function to asssist in unit testing
and a metaclass to apply that function automatically to all relevant
functions within any class that extends it. The @skip_if_already_done
function checks if a downstream function has failed and reports its
failing, rather than claiming that it itself has failed.