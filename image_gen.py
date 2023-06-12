import openai
import json
from base64 import b64decode
from config import GPT as token


def generic_image(generic_data, image_size):
    openai.api_key = token
    generic_data = generic_data
    image_size = image_size
    try:
        response = openai.Image.create(
                                        prompt=generic_data,
                                        n=1,
                                        size=image_size,
                                        response_format='b64_json',
                                    )

        image_data = b64decode(response['data'][0]['b64_json'])

        with open('data.png', 'wb') as file:
            file.write(image_data)
    except Exception as p:
        print(p)
        return False
    return True


if __name__ == '__main__':
    generic_image('girl of beach', '1024x1024')
