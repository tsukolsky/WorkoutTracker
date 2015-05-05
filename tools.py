def prop(func):
    ops = func(None) or {}
    name=ops.get('prefix','_') + func.__name__
    
    fget=ops.get('fget', lambda self:getattr(self, name))
    fset=ops.get('fset', lambda self, value:setattr(self, name,value))
    fdel=ops.get('fdel', lambda self:delattr(self, name))
    return property (fget, fset, fdel, ops.get('doc',''))