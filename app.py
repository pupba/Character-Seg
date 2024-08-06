from gui.gui_main import GUI

class SegmentMachine:
    def __gui(self):
        # GUI
        demo = GUI()

        return demo
    def __call__(self):
        demo = self.__gui()
        demo.launch(debug=False, show_error=True)

if __name__ == "__main__":
    SegmentMachine()()
