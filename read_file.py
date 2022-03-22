# 用Python实现，实现功能读取视频文件名，时长，大小，所在文件目录，代码如下：
import os
import xlwt
from moviepy.editor import VideoFileClip

# file_dir = input("请输入视频文件夹（如：e:\视频）：")#"D:\BaiduNetdiskDownload\work"
file_dir = "D:\直播视频"
class FileCheck():

    def __init__(self):

        self.file_dir = file_dir

    def get_filesize(self, filename):
        file_byte = os.path.getsize(filename)
        file_size_KB, file_size_B = divmod(file_byte, 1024)
        file_size_MB, file_size_KB = divmod(file_size_KB, 1024)
        file_size_MB_KB = str(file_size_MB) + "MB" + str(file_size_KB) + "KB"
        return file_size_MB_KB

    def get_file_times(self, filename):
        clip = VideoFileClip(filename)
        file_time = clip.duration
        clip.reader.close()
        clip.audio.reader.close_proc()
        return file_time

    def get_all_video_file(self):
        video_files = []
        all_files = []
        self.iter_files(file_dir, all_files)
        for f in all_files:
            if self.is_video_file(f):
                video_files.append(f)
        return video_files

    def iter_files(self, root_dir, all_files=[]):
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                file_name = os.path.join(root, file)
                all_files.append(file_name)

    def is_video_file(self, file):
        suffix = os.path.splitext(file)[1]
        if suffix == '.mp4' or suffix == '.mkv' or suffix == '.wmv' \
                or suffix == '.avi' or suffix == 'mpg':
            return True

        return False


def main():
    print("================执行中，请等待...............")
    fc = FileCheck()
    files = fc.get_all_video_file()
    datas = [['文件名', '大小', '时长', '文件目录']]
    for f in files:
        cell = []
        file_path = os.path.join(file_dir, f)
        file_size = fc.get_filesize(file_path)
        file_times = fc.get_file_times(file_path)

        f2 = os.path.basename(f)
        path = os.path.dirname(f)

        print(u"文件名:{filename},大小:{filesize},时长:{filetimes}"
              .format(filename=f2, filesize=file_size, filetimes=file_times))

        cell.append(f2)
        cell.append(file_size)
        cell.append(file_times)
        cell.append(path)
        datas.append(cell)

    wb = xlwt.Workbook()
    sheet = wb.add_sheet('视频清单')

    style = 'pattern: pattern solid, fore_colour yellow; '
    style += 'font: bold on; '
    style += 'align: horz center, vert center; '
    header_style = xlwt.easyxf(style)
    row_count = len(datas)
    col_count = len(datas[0])
    for row in range(0, row_count):
        col_count = len(datas[row])
        for col in range(0, col_count):
            if row == 0:
                sheet.write(row, col, datas[row][col], header_style)
            else:
                sheet.write(row, col, datas[row][col])

    wb.save(file_dir + '\视频清单.xls')
    print("================完成================")

    pass


if __name__ == '__main__':
    main()