from .base import PacketBase
from libopenttd.utils import six
from .exceptions import InvalidFieldName

class Packet(six.with_metaclass(PacketBase)):
    pid = -1

    def __init__(self, **kwargs):
        all_names = set([field.name for field in self._meta.fields])
        for field, value in kwargs.items():
            if field not in all_names:
                raise InvalidFieldName("Field name '%s' not found, did you mean: %s" % (field, ', '.join(all_names)))
        for field in self._meta.fields:
            value = kwargs.get(field.name, field.default_value)
            setattr(self, field.name, value)

    def write(self):
        return self.manager.to_data(self)

    def __repr__(self):
        try:
            utf = six.text_type(self)
        except (UnicodeEncodeError, UnicodeDecodeError):
            utf = '[Bad Unicode data]'
        return '<%s (%d): %s>'  % (self.__class__.__name__, self.pid, utf)

    def __str__(self):
        if six.PY2 and hasattr(self, '__unicode__'):
            return six.text_type(self).encode('utf-8')
        return '%s packet' % self.__class__.__name__

    class Meta:
        abstract = True
