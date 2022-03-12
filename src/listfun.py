# This is the abstract function for list, used in Results part of the notebook
# @param pre is the preprocessor we're working w ith
# @param transformers is the name of the transformers for pre
# @param steps is the steps name for pre
# @param features is the category of features we're focusing on

def list_abs(pre, transformers, steps, features):
    
    #See if transformersna and steps are Strings
    if (not isinstance(transformers, str)) or (not isinstance(steps, str)):
        raise TypeError("Transformers and Steps need to be strings")
        
    #See if features is a list of Strings
    if (not isinstance(features, list)):
        raise TypeError("features need to be a list")
        
    #If both tests are passed: we generate the outcome and return
    else:
        ret = list(
        pre.named_transformers_[transformers]
        .named_steps[steps]
        .get_feature_names_out(features)
        )
    
    return ret