import requests
import base64
from PIL import Image
import io

def encode_image(image_path):
    """Codifica una imagen en base64"""
    with open(image_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def submit_solution(server_url, original_path, adversarial_path):
    """Envía la solución al servidor"""
    original_b64 = encode_image(original_path)
    adversarial_b64 = encode_image(adversarial_path)
    
    data = {
        'original_image': original_b64,
        'adversarial_image': adversarial_b64
    }
    
    response = requests.post(f'{server_url}/submit', json=data)
    return response.json()

if __name__ == '__main__':
    SERVER_URL = 'URL_RETO'
    
    # Ejemplo de uso
    result = submit_solution(
        SERVER_URL,
        'dog_original.png',
        'barco_ad.png'
    )
    
    print(result)