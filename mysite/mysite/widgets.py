from croppie.fields import CroppieField
import copy


CROP_OPTIONS = {
    'viewport': {
        'width': 140,
        'height': 140,
    },
    'boundary': {
        'width': 220,
        'height': 220,
    },
    'showZoomer': False,
}


class MyCroppieField(CroppieField):
    def __init__(self, *args, **kwargs):
        self.is_image = True
        opt = copy.copy(CROP_OPTIONS)
        if "options" in kwargs:
            opt.update(kwargs["options"])
        kwargs["options"] = opt
        return CroppieField.__init__(self, *args, **kwargs)

    def crop_image(self, *args, **kwargs):
        try:
            return CroppieField.crop_image(self, *args, **kwargs)
        except AttributeError:
            return None
