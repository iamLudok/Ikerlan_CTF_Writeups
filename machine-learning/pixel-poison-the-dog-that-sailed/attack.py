#!/usr/bin/env python3
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
import sys

# ============================================================================
# MODELO
# ============================================================================

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(128 * 4 * 4, 256)
        self.fc2 = nn.Linear(256, 10)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.5)
        
    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = self.pool(self.relu(self.conv3(x)))
        x = x.view(-1, 128 * 4 * 4)
        x = self.dropout(self.relu(self.fc1(x)))
        x = self.fc2(x)
        return x

CLASSES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 
           'dog', 'frog', 'horse', 'ship', 'truck']

# ============================================================================
# TU CÓDIGO AQUÍ
# ============================================================================

def generate_adversarial_example(model, image, target_class, epsilon):
    """
    Genera un ejemplo adversarial.
    
    Args:
        model: Modelo pre-entrenado
        image: Tensor [1, 3, 32, 32]
        target_class: Clase objetivo (8 = 'ship')
        epsilon: Perturbación máxima
    
    Returns:
        adversarial_image: Tensor [1, 3, 32, 32]
    """
    
    device = next(model.parameters()).device
    model.eval()
    
    # TODO: Tu implementación aquí
    
    raise NotImplementedError("Implementa esta función")

# ============================================================================
# TEST
# ============================================================================

def test_attack(image_path='dog_sample.png', model_path='model.pth'):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    model = SimpleCNN().to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    
    img = Image.open(image_path).convert('RGB').resize((32, 32))
    transform = transforms.ToTensor()
    img_tensor = transform(img).unsqueeze(0).to(device)
    
    with torch.no_grad():
        output = model(img_tensor)
        probs = torch.softmax(output, dim=1)
        pred = torch.argmax(probs).item()
        conf = probs[0][pred].item()
    
    print(f"Original: {CLASSES[pred]} ({conf:.2%})")
    
    try:
        adversarial_tensor = generate_adversarial_example("a completar")
    except NotImplementedError:
        print("Implementa generate_adversarial_example()")
        return False
    
    with torch.no_grad():
        output_adv = model(adversarial_tensor)
        probs_adv = torch.softmax(output_adv, dim=1)
        pred_adv = torch.argmax(probs_adv).item()
        conf_adv = probs_adv[0][pred_adv].item()
        ship_conf = probs_adv[0][8].item()
    
    diff = torch.max(torch.abs(adversarial_tensor - img_tensor)).item()
    
    print(f"Adversarial: {CLASSES[pred_adv]} ({conf_adv:.2%})")
    print(f"Ship confidence: {ship_conf:.2%}")
    print(f"Epsilon: {diff:.4f}")
    
    success = (pred_adv == 8 and ship_conf > 0.70 and diff <= 0.05)
    
    if success:
        print("ÉXITO")
        transforms.ToPILImage()(img_tensor.squeeze(0).cpu()).save('dog_original.png')
        transforms.ToPILImage()(adversarial_tensor.squeeze(0).cpu()).save('dog_adversarial.png')
    else:
        print("FALLO")
    
    return success

if __name__ == '__main__':
    import torchvision
    testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True)
    
    from pathlib import Path
    if not Path('dog_sample.png').exists():
        for i, (img, label) in enumerate(testset):
            if label == 5:
                img.save('dog_sample.png')
                break
    
    test_attack()