import ffmpeg


class TelloFFmpeg:
    def __init__(self):
        pass

    def decode(self, input_data):
        out, _ = (
            ffmpeg
            .input(input_data)
            .output('pipe:', f='null')
            .run(capture_stdout=True)
        )