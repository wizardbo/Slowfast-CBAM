import os

dataset_path = '/home/tione/notebook/slowfast/data/charades/frames'    # 切分图片目录
label_path = '/home/tione/notebook/slowfast/data_file/train.txt'  #train.txt, val.txt
tag_id_file = '/home/tione/notebook/VideoStructuring/dataset/label_id.txt'

if __name__ == '__main__':
    #获取类别字典
    dict_categories = {}
    with open(tag_id_file, 'r',encoding='utf-8') as lnf:
        for line in lnf:
            tag, idx = line.strip().split('\t')
            dict_categories[tag] = int(idx)

    print(dict_categories)


    count_cat = {k: 0 for k in dict_categories.keys()}
    with open(label_path) as f:
        lines = f.readlines()
    folders = []
    idx_categories = []
    categories_list = []
    for line in lines:
        line = line.rstrip()    #  删除 string 字符串末尾的指定字符（默认为空格）
        items = line.split('\t')
        folders.append(items[0])  #视频文件名
        categories_list = []
        items_list = items[1].split(',')
        for i in range(len(items_list)):
            items_catergory = items_list[i]
            categories_list.append(dict_categories[items_catergory])
        idx_categories.append(categories_list)

    assert len(idx_categories) == len(folders)

    csv_path = '/home/tione/notebook/SlowFast/data/charades/frame_lists/train.csv'
    csv_file = open(csv_path,'w')
    csv_file.write("original_vido_id,video_id,frame_id,path,labels\n")
    j = 0
    for i in range(len(folders)):
        curFolder = folders[i]
        curIDX = idx_categories[i]
        # counting the number of frames in each video folders
        img_dir = os.path.join(dataset_path, curFolder)
        #print(img_dir)
        k = 0
        filen = os.listdir(img_dir)
        filen.sort(key=lambda x:int(x[-10:-4]))
        for h in filen:
            csv_file.write(curFolder + ' ' + str(j) + ' ' + str(k) + ' ' + os.path.join(curFolder, h) + ' ' + str(curIDX).replace('[', '"').replace(']', '"').replace(' ', '') + '\n')

            k += 1
        j += 1

    csv_file.close()
