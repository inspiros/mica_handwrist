import os


for root_dir in ['train', 'test']:
    out_file = os.path.join(root_dir, 'annotation.txt')

    with open(out_file, 'w') as of:
        labels_dir = os.path.join(root_dir, 'labels')
        for label_file in sorted(os.listdir(labels_dir)):
            img_file = os.path.splitext(label_file)[0] + '.jpg'
            label_file_path = os.path.join(labels_dir, label_file)
            with open(label_file_path) as lf:
                label = int(lf.readlines()[0].strip().split()[0])
            of.write(img_file + ' ' + str(label))
            of.write('\n')
