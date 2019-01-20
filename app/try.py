import os

root = '/home/caleb/batcave/one-stop-photoshop/app/static'
file_count = 0
for dirpath, dirnames, files in os.walk(root):
    for dirr in dirnames:
        print(dirr)
        for dirpath2, dirnames2, files2 in os.walk(os.path.join(dirpath, dirr)):
            print(int(len(files2) / 2))

for i in range(len(image_counts)):
    obj = Post()