from django.core.exceptions import ValidationError

def _get_image_resolution(image:object) -> list:
        image_info = image.info()['image_info']

        img_width = image_info['width']
        img_height = image_info['height']

        return (img_width, img_height)


def image_max_resolution_validator(image:object, max_width:int, max_height:int) -> None:
    if not image.is_image():
        raise ValidationError('File must be image')


    errors = list
    
    img_width, img_height = _get_image_resolution(image)


    if img_width > max_width:
        errors.append(f'Width should be < {max_width} px.')


    if img_height > max_height:
        errors.append(f'Height should be < {max_height} px.')

    if errors:
        raise ValidationError(errors)

    return None

def image_size_validator(image:object, megabyte_limit:float) -> None:
    image_size = image.file.size

    size_limit = megabyte_limit * 1024 * 1024

    if image_size > size_limit:
        raise ValidationError(f'Max file size is {str(megabyte_limit)}')