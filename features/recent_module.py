from logic.middleware import processing_helper
from shared.utils import init

def run_new_feature():
    # 1. TRIGGER: INDIRECT DEPENDENCY
    # This calls middleware, which calls legacy. System must find the path features -> logic -> database.
    
    # 2. TRIGGER: MIDDLE-AGE GAP
    # middleware.py is 60 days old (ignored by old buckets, caught by Relative Age logic).
    
    init() # 3. TRIGGER: SYMBOL AMBIGUITY
           # System must verify this is shared.utils.init, NOT database.legacy_provider.init.
           
    result = processing_helper("test_input")
    return result