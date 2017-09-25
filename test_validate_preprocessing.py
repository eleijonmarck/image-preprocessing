import os
import errno
import itertools
import scipy.misc
import numpy as np

curr_dir = os.getcwd()
proj_dir = os.path.normpath(os.path.join(curr_dir))
image_dir = 'data/train'
input_filepath = os.path.normpath(os.path.join(proj_dir, image_dir))

validation_dir = 'data/processed/validation'
train_dir = 'data/processed/train'

class_dict = {'dog': 0, 'cat': 1}

def put_classes_into_separate_folders(parent_dir, images):
    make_sure_path_exists(parent_dir)

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


train_shuffled_images = []
test_shuffled_images = []
def create_train_validation_shuffle_images():
    test_percentage = 0.2
    for key, _ in class_dict.items():
        class_images = [x for x in os.listdir(input_filepath) if x.startswith(key + ".")]
        k = int(len(class_images) * test_percentage)
        test_shuffled_images = class_images[0:k]
        train_shuffled_images = class_images[k:]
    return train_shuffled_images, test_shuffled_images

train_images = []
validation_images = []
def resize_of_images():
    train_images = [scipy.misc.imresize(scipy.misc.imread(input_filepath + '/' + image), (100,50)) for image in train_shuffled_images]
    validation_images = [scipy.misc.imresize(scipy.misc.imread(input_filepath +
        '/' + image), (100,50)) for image in test_shuffled_images]
    return train_images, validation_images

def put_class_images_in_folders(save_dir, image_files, class_feature):
    counter = 0
    class_counter = 0
    first = True

    make_sure_path_exists(save_dir)

    for image in image_files:
        counter += 1

        if (counter % int(len(image_files) / len(class_feature)) == 0) and (first == False) != (counter == int(len(image_files))):
            class_counter += 1
        first = False

        class_dir = os.path.join(save_dir,class_feature[class_counter])
        make_sure_path_exists(class_dir)

        save_image = os.path.join(class_dir,'{}_{}.jpeg'.format(class_feature[class_counter],"".join((map(str,np.random.randint(0,9,8))))))

        scipy.misc.imsave(save_image, image)


if __name__ == '__main__':
    train_shuffled_images, test_shuffled_images = create_train_validation_shuffle_images()
    train_images, test_images = resize_of_images()
    keys = []
    for k, _ in class_dict.items():
        keys.append(k)
    print(input_filepath)
    put_class_images_in_folders(input_filepath + '/train/', train_images,
            keys)
    put_class_images_in_folders(input_filepath + '/validation/', test_images,
            keys)
