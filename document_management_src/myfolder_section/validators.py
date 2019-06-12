from django.core.exceptions import ValidationError


def clean_project_name(value):
    if value[0].isdigit():
        raise ValidationError('Project Name Can\'t Startswith Number')
    return value
