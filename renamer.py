import os

file_path = 'E:\\02_촬영 이미지_원본\\20210628_연화지\\012_연꽃'
file_names = os.listdir(file_path)
print(file_names)

i = 1

for name in file_names:
    src = os.path.join(file_path, name)
    dst = "OR012_FL_{}.jpg".format(str(i).zfill(5))
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1
