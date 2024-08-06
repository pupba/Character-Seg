import torch
from PIL import Image
import numpy as np
from utils.models import INFERENCE

def detectSam2(check_point:str,image_input:Image):
    from imgutils.detect import detect_person
    result = detect_person(image_input)
    config:dict = {
        "ckpt":check_point,
        "image":image_input,
        "device":"cuda" if torch.cuda.is_available() else "cpu"
    }
    m_ = []
    c_ = []
    # detect 되는 만큼 전부 찾기
    for box,cls,score in result:
        config['box'] = np.array([box])
        masks,crops = INFERENCE(**config)
        m_+=masks
        c_+=crops
    return m_,c_