import com3,read_file,read_excel
import  os

output_path = ""
#读取文件中的所有视频并存入excel
read_file.main()

file_dir =read_file.file_dir

kv,video2 = read_excel.read_name(file_dir)

# 使用for循环遍历 一个个压缩
save_video = com3.Compress_Pic_or_Video()
for j in video2:

    path= kv[j]
    path1 = path[2:]
    output_path = file_dir + "\compress" + path1
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    video_name = j[:-4]
    save_video.set_video(path, j, output_path ,"{}_01.mp4".format( video_name))
    print(save_video.compress_video_anyc())





