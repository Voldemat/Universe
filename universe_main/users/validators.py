from django.core.exceptions import ValidationError

def max_image_size(width:int, height:int) -> callable:

    def _get_image_resolution(image:object) -> list:
        image_info = image.info()['image_info']

        img_width = image_info['width']
        img_height = image_info['height']

        return (img_width, img_height)

    def validator(image:object) -> None:
        if not image.is_image():
            raise ValidationError('File must be image')

        errors = list
        
        img_width, img_height = _get_image_resolution(image)


        if img_width > width:
            errors.append(f'Width should be < {width} px.')


        if img_height > height:
            errors.append(f'Height should be < {height} px.')

        raise ValidationError(errors)

    return validator