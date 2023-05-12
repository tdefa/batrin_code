

import nd2
from pathlib import Path
import numpy as np
import tifffile






if __name__ == '__main__':



    path_exp_folder  = "/home/tom/Bureau/phd/Batrin/Images_pour_FISH/Expérience2/"
    path_save_ch0 = "/home/tom/Bureau/phd/Batrin/Images_pour_FISH/Expérience2/ch0/"
    path_save_ch1 = "/home/tom/Bureau/phd/Batrin/Images_pour_FISH/Expérience2/ch1/"
    path_save_ch0_mip = "/home/tom/Bureau/phd/Batrin/Images_pour_FISH/Expérience2/ch0_mip/"
    path_save_ch1_mip = "/home/tom/Bureau/phd/Batrin/Images_pour_FISH/Expérience2/ch1_mip/"

    Path(path_save_ch0).mkdir(parents=True, exist_ok=True)
    Path(path_save_ch1).mkdir(parents=True, exist_ok=True)
    Path(path_save_ch0_mip).mkdir(parents=True, exist_ok=True)
    Path(path_save_ch1_mip).mkdir(parents=True, exist_ok=True)
    for im_path in Path(path_exp_folder).glob(f'*.nd2'):
        my_array = nd2.imread(im_path)
        tifffile.imsave(path_save_ch0 + im_path.name[:-4] + '.tiff', my_array[:,0])
        tifffile.imsave(path_save_ch1 + im_path.name[:-4] + '.tiff', my_array[:,1])
        tifffile.imsave(path_save_ch0_mip + im_path.name[:-4] + '.tiff', np.amax(my_array[:,0], 0))
        tifffile.imsave(path_save_ch1_mip + im_path.name[:-4] + '.tiff', np.amax(my_array[:,1], 0))