import os
import threading
import platform
import const

# 本地ffmpeg位置
const.FFMPEG_BIN = "ffmpeg" or "/Users/napoleon/Downloads/ffmpeg"


class Compress_Pic_or_Video(object):
    def __init__(self, file_path="", input_name="", output_name=""):
        # self.set_video(file_path, input_name, output_name)
        pass

    @property
    def is_video(self):
        videoSuffixSet = {"WMV", "ASF", "ASX", "RM", "RMVB", "MP4", "3GP", "MOV", "M4V", "AVI", "DAT", "MKV", "FIV",
                          "VOB"}
        suffix = self.file_input_path.rsplit(".", 1)[-1].upper()
        if suffix in videoSuffixSet:
            return True
        else:
            return False

    def save_video(self):
        fpsize = os.path.getsize(self.file_input_path) / 1024
        if fpsize >= 150.0:  # 大于150KB的视频需要压缩
            if self.out_name:
                compress = const.FFMPEG_BIN + " -i {} -r 10 -pix_fmt yuv420p -vcodec libx264 -preset 1 -profile:v baseline  -crf 33 -acodec aac -b:a 64k -ac 1  -strict -5 {}".format(
                    self.file_input_path, self.file_out_path)
                isRun = os.system(compress)
            else:
                compress = const.FFMPEG_BIN + " -i {} -r 10 -pix_fmt yuv420p -vcodec libx264 -preset 1 -profile:v baseline  -crf 33 -acodec aac -b:a 64k -ac 1 -strict -5 {}".format(
                    self.file_input_path, self.file_input_path)
                isRun = os.system(compress)
            if isRun != 0:
                return (isRun, "没有安装ffmpeg")
            return True
        else:
            return True

    # 异步代码
    def compress_video(self):
        thr = threading.Thread(target=self.save_video)
        thr.start()

    # 同步代码
    def compress_video_anyc(self):
        fpsize = os.path.getsize(self.file_input_path) / 1024
        if fpsize >= 150.0:  # 大于150KB的视频需要压缩
            compress = const.FFMPEG_BIN + " -i {} -r 10 -pix_fmt yuv420p -vcodec libx264 -preset 1 -profile:v baseline  -crf 33 -acodec aac -b:a 64k -ac 1 -strict -5 {}".format(
                self.file_input_path, self.file_out_path)
            isRun = os.system(compress)
            if isRun != 0:
                return (isRun, "没有安装ffmpeg")
            return True
        else:
            return True

    def set_video(self, file_path, input_name, output_path,output_name=""):
        self.file_path = file_path  #文件地址
        self.output_path = output_path # 文件输出路径
        self.input_name = input_name  # 输入的文件名字
        self.out_name = output_name  # 输出的文件名字
        self.system_ = platform.platform().split("-", 1)[0]
        # if  self.system_ ==  "Windows":
        #     self.file_path = (self.file_path + "\\") if self.file_path.rsplit("\\",1)[-1] else self.file_path
        # elif self.system_ == "Linux":
        #     self.file_path = (self.file_path + "/") if self.file_path.rsplit("/",1)[-1] else self.file_path
        self.file_input_path = os.path.join(self.file_path, input_name)
        self.file_out_path = os.path.join(self.output_path, output_name)


# if __name__ == "__main__":
#     # 测试压缩
#     save_video = Compress_Pic_or_Video()
#     save_video.set_video("D:/BaiduNetdiskDownload/", "test1.mp4", "o1.mp4")
#     print(save_video.compress_video_anyc())