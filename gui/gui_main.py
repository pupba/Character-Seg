import gradio as gr
from gui.gui_sam2 import guiSam2
from gui.gui_detected_sam2 import guiDetectSam2

def GUI():
    with gr.Blocks() as demo:
        gr.Markdown("# Segmentation with SAM2")
        guiSam2()
        guiDetectSam2()
        
    return demo