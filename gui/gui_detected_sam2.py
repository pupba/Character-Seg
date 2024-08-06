import gradio as gr
from modules.detect_sam2 import detectSam2
from utils.models import CHECKPOINT_NAMES

def guiDetectSam2():
    with gr.Tab("Character Detect with SAM2") as tab:
        with gr.Row():
            check_point = gr.Dropdown(
                choices=CHECKPOINT_NAMES,
                value = CHECKPOINT_NAMES[0],
                label="SAM2_Checkpoint",info="Select a SAM2 Checkpoint!",
                interactive=True
            )
        with gr.Row():
            with gr.Column():
                image_input = gr.Image(
                    type="pil",label="Image"
                )
                infer_btn = gr.Button(
                    value="Inference",variant="primary"
                )
            with gr.Column():
                # 크롭 이미지들
                mask_outputs = gr.Gallery(None,format="png",label="Mask Outputs",height="auto")
                crop_outputs = gr.Gallery(None,format="png",label="Crop Outputs",height="auto")
                # 마스크 이미지들
        infer_btn.click(
            fn=detectSam2,
            inputs=[check_point,image_input],
            outputs=[mask_outputs,crop_outputs]
        )

    return tab