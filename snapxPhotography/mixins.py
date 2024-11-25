class DisabledFieldsMixin:
    disabled_fields = []

    def disable_fields(self):
        for field_name in self.disabled_fields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['readonly'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()