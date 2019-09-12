from django.conf import settings
from .helpers import Choices


STATES = Choices(
    ('DRAFT', 100, 'Draft'),
    ('SUBMITTED', 200, 'Submitted'),
    ('ACCEPTED', 300, 'Accepted'),
    ('REFUSED', -1, 'Refused'),
    ('CANCELLED', -100, 'Cancelled'),
    ('MISSING', 0, 'Missing'),
)
STATES.add_subset('MANUAL', (
    'DRAFT',
    'SUBMITTED',
    'ACCEPTED',
    'REFUSED',
    'CANCELLED',
))

STATES = getattr(settings, 'STATES', STATES)
