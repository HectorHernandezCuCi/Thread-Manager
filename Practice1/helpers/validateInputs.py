from utils.formats.numbers import get_int

def validate_inputs(threads_input, limit_input):
    n = get_int(threads_input)
    limit = get_int(limit_input)
    
    if n < 1 or n > 128:
        return "Thread count must be between 1 and 128"
    if limit < 2:
        return "Range limit must be at least 2"
    if limit > 100_000_000:
        return "Range limit  (Max: 100M)"
    return None