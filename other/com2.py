import sys
import os
import zlib
import threading
import platform
from PIL import Image



def SaveVideo(self):
    # fpsize = os.path.getsize(self.fileInputPath) / 1024
    fpsize = os.path.getsize(r'D:\BaiduNetdiskDownload\test.mp4') / 1024
    if fpsize >= 150.0:  # 大于150KB的视频需要压缩
        if self.outName:
            compress = "ffmpeg -i {} -r 10 -pix_fmt yuv420p -vcodec libx264 -preset veryslow -profile:v baseline  -crf 23 -acodec aac -b:a 32k -strict -5 {}".format(
                self.fileInputPath, self.fileOutPath)
            isRun = os.system(compress)
        else:
            compress = "ffmpeg -i {} -r 10 -pix_fmt yuv420p -vcodec libx264 -preset veryslow -profile:v baseline  -crf 23 -acodec aac -b:a 32k -strict -5 {}".format(
                self.fileInputPath, self.fileInputPath)
            isRun = os.system(compress)
        if isRun != 0:
            return (isRun, "没有安装ffmpeg")
        return True
    else:
        return True


if __name__ == "__main__":
    #判断文件有多少兆，getsize返回文件大小kb除以1024为K大小，再除以1024等于兆M
    fpsize1 = os.path.getsize(r'D:\BaiduNetdiskDownload\test2.mp4')/1024/1024
    print(fpsize1)
    #命令行执行成功
    compress = r'ffmpeg -i D:\BaiduNetdiskDownload\test2.mp4 -s 1920x1080 -c:v libx265 -c:a aac -b:v 200k -r 25 D:\BaiduNetdiskDownload\test22.mp4'
    isRun = os.system(compress)
    print(isRun)