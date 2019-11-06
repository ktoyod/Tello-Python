import subprocess as sp


class TelloDecoder:
    def __init__(self):
        pass

    def decode(self, input_data):
        # ffmpegCmd = ['ffmpeg', '-', '-f', 'null', '-']
        ffmpegCmd = ['ffmpeg', '-i', '-', '-f', 'rawvideo', '-vcodec', 'bmp', '-vf', 'fps=5', '-']
        ffmpeg = sp.Popen(ffmpegCmd, stdin=input_data, stdout=sp.PIPE)
        return ffmpeg