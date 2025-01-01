class Readonly(object):
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, item):
        return getattr(self._obj, item)

    def __setattr__(self, key, value):
        if key == '_obj':
            super().__setattr__(key, value)
        else:
            raise AttributeError('Read Only')