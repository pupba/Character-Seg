from gradio_image_prompter import ImagePrompter
import numpy as np
import gradio as gr
import torch
from utils.models import INFERENCE

def onlySAM2(check_point:str,image_prompter_input:ImagePrompter):
    img_input = image_prompter_input["image"]
    prompts = image_prompter_input['points']
    if len(prompts) == 0:
        gr.Warning("No Prompt....")
        return None,None
    boxes = []
    points = []
    labels = []
    for prompt in prompts:
        x1,y1,_,x2,y2,_ = prompt
        # point is negtive
        if x2 == 0 and y2 == 0:
            points.append([x2,y2])
            labels.append(0)
            continue
        # box
        boxes.append([x1,y1,x2,y2])

    boxes = np.array(boxes)
    points = np.array(points)
    labels = np.array(labels)
    config:dict = {
        "ckpt":check_point,
        "image":img_input,
        "box":boxes if len(boxes) > 0 else None,
        "point":points if len(points) > 0 else None,
        "label":labels if len(labels) > 0 else None,
        "device": "cuda" if torch.cuda.is_available() else "cpu"
    }
    masks,crops = INFERENCE(**config)
    return masks,crops