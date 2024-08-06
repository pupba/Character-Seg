from typing import Dict, Tuple
from PIL import Image
import torch
import numpy as np
import cv2
from sam2.build_sam import build_sam2
from sam2.utils.misc import variant_to_config_mapping
from sam2.sam2_image_predictor import SAM2ImagePredictor

CHECKPOINT_NAMES = ["tiny","small","base_plus", "large"]
CHECKPOINTS = {
    "tiny": "models/sam2_hiera_tiny.pt",
    "small": "models/sam2_hiera_small.pt",
    "base_plus": "models/sam2_hiera_base_plus.pt",
    "large":"models/sam2_hiera_large.pt",
}

# 마스크 선택 알고리즘

# # Reference: https://colab.research.google.com/github/MrSyee/SAM-remove-background/blob/main/jupyternotebook/sam_click.ipynb
# def select_masks(
#     masks: np.ndarray, iou_preds: np.ndarray, num_points: int
# ) -> Tuple [np.ndarray, np.ndarray]:
#     # Determine if we should return the multiclick mask or not from the number of points.
#     # The reweighting is used to avoid control flow.
#     # Reference: https://github.com/facebookresearch/segment-anything/blob/6fdee8f2727f4506cfbbe553e23b895e27956588/segment_anything/utils/onnx.py#L92-L105
#     score_reweight = np.array([1000] + [0] * 2)
#     score = iou_preds + (num_points - 2.5) * score_reweight
#     best_idx = np.argmax(score)
#     masks = np.expand_dims(masks[best_idx, :, :], axis=-1)
#     iou_preds = np.expand_dims(iou_preds[best_idx], axis=0)
#     return masks, iou_preds

def getMask(img:Image,mask:np.ndarray)->None:
    img = np.array(img)

    mask_image = np.where(mask, 255, 0).astype(np.uint8)

    mask = mask_image

    crop = cv2.bitwise_and(img,img, mask=mask_image)
    return mask,crop


def INFERENCE(
    ckpt:str,
    image:Image,
    box:np.ndarray | None = None,
    point:np.ndarray | None = None,
    label:np.ndarray | None = None,
    device:torch.device = "cpu"
)->list:
    model = build_sam2(
        variant_to_config_mapping[ckpt],
        CHECKPOINTS[ckpt],
        device=device
    )
    image_predictor = SAM2ImagePredictor(model)
    image_predictor.set_image(image)

    masks, scores, logits = image_predictor.predict(
        point_coords=point,
        point_labels=label,
        box=box,
        multimask_output=True,
    )

    masks_ = []
    crops_ = []
    for idx,mask in enumerate(masks):
        mask,crop = getMask(img=image,mask=mask)
        masks_.append((Image.fromarray(mask),f"{idx}_m.png"))
        crops_.append((Image.fromarray(crop),f"{idx}_c.png"))
    return masks_,crops_