class BaseStoreException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class ItemNotFoundStoreException(BaseStoreException):
    def __init__(self, item_name):
        super().__init__('Item {} was not found.'.format(item_name))


class ItemAlreadyExistsStoreException(BaseStoreException):
    def __init__(self, item_name):
        super().__init__('Item {} already exists.'.format(item_name))


class MissingAttributeStoreException(BaseStoreException):
    def __init__(self, attribute_name):
        super().__init__('Attribute {} is required.'.format(attribute_name))


class WrappedStoreException(BaseStoreException):
    def __init__(self, msg, original_exception):
        super().__init__('{}: {}'.format(msg, original_exception))
        self._original_exception = original_exception

    @property
    def original_exception(self):
        return self._original_exception
