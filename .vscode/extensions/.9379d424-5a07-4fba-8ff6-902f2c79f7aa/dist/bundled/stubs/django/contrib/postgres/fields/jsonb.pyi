from django.db.models import JSONField as BuiltinJSONField
from django.db.models.fields.json import KeyTextTransform as BuiltinKeyTextTransform
from django.db.models.fields.json import KeyTransform as BuiltinKeyTransform

# All deprecated
class JSONField(BuiltinJSONField): ...
class KeyTransform(BuiltinKeyTransform): ...
class KeyTextTransform(BuiltinKeyTextTransform): ...