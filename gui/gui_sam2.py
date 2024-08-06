import gradio as gr
from gradio_image_prompter import ImagePrompter
from modules.only_sam2 import onlySAM2
from utils.models import CHECKPOINT_NAMES

def guiSam2():
    with gr.Tab("Mouse with SAM2") as tab:
        with gr.Row():
            check_point = gr.Dropdown(
                choices=CHECKPOINT_NAMES,
                value = CHECKPOINT_NAMES[0],
                label="SAM2_Checkpoint",info="Select a SAM2 Checkpoint!",
                interactive=True
            )
        with gr.Row():
            with gr.Column():
                image_prompter_input = ImagePrompter(
                    type="pil",label="Image prompt",visible=True
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
            fn=onlySAM2,
            inputs=[
                check_point,
                image_prompter_input,
            ],
            outputs=[mask_outputs,crop_outputs]
        )

    return tab