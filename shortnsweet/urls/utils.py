# from shortnsweet.shortnsweet import settings
import uuid

from string import  ascii_letters, digits

SIZE =  7

AVAILABLE_CHARS = ascii_letters + digits

def create_random_code(chars=AVAILABLE_CHARS):

    return str(uuid.uuid4())[:SIZE]


def create_shortened_url(model_instance):
    random_code = create_random_code(model_instance)

    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=random_code).exists():

        return create_shortened_url(model_instance)

    return random_code