from functools import partial


class ToggleManyToMany:
    def __init__(self, *args, **kwargs):
        self._toggleable_fields = getattr(self, 'TOGGLEABLE_FIELDS', None)

        if self._toggleable_fields:
            self._generate_toggle_methods()

    def _toggle(self, instance, field):
        field_to_toggle = getattr(self, field, None)

        if instance.id in field_to_toggle.values_list('id', flat=True):
            field_to_toggle.remove(instance)
        else:
            field_to_toggle.add(instance)

        return instance

    def _generate_toggle_methods(self):
        for toggleable_field in self._toggleable_fields:
            method_name = f'toggle_{toggleable_field}'
            toggle_method = partial(self._toggle, field=toggleable_field)

            setattr(self, method_name, toggle_method)
