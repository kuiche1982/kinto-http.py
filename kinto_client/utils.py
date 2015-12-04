import re
import unicodedata
from unidecode import unidecode
import six


def slugify(value):
    """Normalizes string, converts to lowercase, removes non-alpha characters
    and converts spaces to hyphens.
    """
    value = unidecode(six.text_type(value))
    if isinstance(value, six.binary_type):
        value = value.decode('ascii')  # pragma: nocover
    value = unicodedata.normalize('NFKD', value).lower()
    value = re.sub('[^\w\s-]', '', value.lower()).strip()
    value = re.sub('[-\s]+', '-', value)
    return value


def urljoin(server_url, path):
    """Return the url concatenation of server_url and path."""
    return server_url.rstrip('/') + '/' + path.lstrip('/')


def quote(text):
    return '"{0}"'.format(text)


def chunks(l, n):
    """Yield successive n-sized chunks from l.
    Source: http://stackoverflow.com/a/312464
    """
    if n > 0:
        for i in xrange(0, len(l), n):
            yield l[i:i+n]
    else:
        yield l
