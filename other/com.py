# coding=utf-8
import os
import subprocess
import re


class FFmpeg:

    def __init__(self, video_file:str):
        self.video_file = video_file
        self.vdo_time, self.vdo_width, self.vdo_height, self.attr_dict = self.get_attr()
        self.video_path = os.path.dirname(video_file)
        self.video_name = os.path.basename(video_file)

    def get_attr(self) -> set:
        """
        :return:
        """
        strcmd = r'ffprobe -print_format json -show_streams -i "{}"'.format(self.video_file)
        status, output = subprocess.getstatusoutput(strcmd)
        agrs = eval(re.search('{.*}', output, re.S).group().replace("\n", "").replace(" ", ''))
        streams = agrs.get('streams', [])
        agrs_dict = dict()
        [agrs_dict.update(x) for x in streams]
        vdo_time = agrs_dict.get('duration')
        vdo_width = agrs_dict.get('width')
        vdo_height = agrs_dict.get('height')
        attr = (vdo_time, vdo_width, vdo_height, agrs_dict)
        return attr


    def edit_resolution(self, resolution:str='1024x720', rate:int=30, save_path=None) -> bool:
        """
        :param resolution: change resolution
        :param save_path: save path
        :return:
        """
        if None == save_path:
            if not os.path.exists(self.video_path+'/'+'edit_resolution'):
                os.mkdir(self.video_path+'/'+'edit_resolution')
            save_path = self.video_path+'/'+'edit_resolution'+self.video_name
        strcmd = r'ffmpeg -i "{}" -s {} -r {} "{}"'.format(self.video_file, resolution, rate, save_path)
        result = subprocess.run(args=strcmd, stdout=subprocess.PIPE, shell=True)
        if os.path.isfile(save_path):
            return True
        else:
            return False

if __name__ == "__main__":
    x = FFmpeg(r"D:\BaiduNetdiskDownload\test2.mp4")
    x.edit_resolution(save_path=r'../test22.mp4')
