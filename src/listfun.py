import numpy as np
import pandas as pd
import warnings as wa

def list_abs(pre, transformers, steps, features):
    ret = list(
    pre.named_transformers_[transformers]
    .named_steps[steps]
    .get_feature_names_out(features)
    )
    
    return ret