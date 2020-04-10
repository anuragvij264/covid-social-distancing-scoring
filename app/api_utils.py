from torchvision import transforms
from PIL import Image
import numpy as np
import torch
from model import CSRNet

transform = transforms.Compose([
    transforms.ToTensor(), transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                std=[0.229, 0.224, 0.225]),
])


def gen_img_counts(img_path, model):
    """
    given an image return the head count in the image
    """

    img = transform(Image.open(img_path).convert('RGB'))
    print(type(img))
    output = model(img.unsqueeze(0))
    pred_count = int(output.detach().cpu().sum().numpy())
    return pred_count


def score(output):
    if output < 400:
        return np.tanh(152 * output + 0.1578)
    else:
        return 1.


def load_model(model_path, device):
    """
    model_path: saved model (.pth or .pth.tar)
    #TODO: map_location
    """
    model = CSRNet()
    checkpoint = torch.load(model_path, map_location=device)
    model.load_state_dict(checkpoint['state_dict'])

    return model


def debug_pred(img_path, model, orig_img_path):
    """
    debug
    """
    pass
