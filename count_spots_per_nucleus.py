

import numpy as np
import tifffile
from pathlib import Path
import pandas as pd


from bigfish import detection

from bigfish import stack









if __name__ == '__main__':



   path_main_folder  = "/home/tom/Bureau/phd/Batrin/Images_pour_Pasteur/"
   path_ch0 = path_main_folder + "round_folder/ch0_mip/"
   path_mask_folder  = path_main_folder + "ch1_mask_mip/20_cyto/"
   path_csv_folder = path_main_folder + "round_folder/detection_csv/"
   dico_mean_spots = {}
   dico_snr = {}
   dico_mean_intensity = {}
   dico_mean_intensity_normalize = {}
   for path_mask in Path(path_mask_folder).glob("*tif*"):
        print(path_mask.name)
        mask = tifffile.imread(path_mask)
        img_fish = tifffile.imread(path_ch0 + path_mask.name[:-4])
        img_fish_mean = stack.mean_filter(img_fish, kernel_shape = "square", kernel_size = 4)


        df_spots = pd.read_csv(path_csv_folder + path_mask.name[:-4] + ".csv")
        df_spots['in_mask'] = 0
        df_spots['mean_intensity'] = 0
        df_spots['normalized_mean_intensity'] = 0

        list_spots = np.array([[x,y] for x, y in zip(df_spots['x'], df_spots['y'])])
        snr  = detection.compute_snr_spots(img_fish, list_spots, voxel_size = 108, spot_radius= 300)
        dico_snr[path_mask.name[:-4]] = snr
        list_mean_intensity = []
        mean_norm = np.mean(img_fish_mean[mask == 0])
        for i in range(len(df_spots)):
            if mask[int(df_spots['x'][i]), int(df_spots['y'][i])]  !=0:
                df_spots['in_mask'][i] =  mask[int(df_spots['x'][i]), int(df_spots['y'][i])]
                list_mean_intensity.append(img_fish_mean[int(df_spots['x'][i]), int(df_spots['y'][i])])


            df_spots['mean_intensity'][i] = img_fish_mean[int(df_spots['x'][i]), int(df_spots['y'][i])]
            df_spots['normalized_mean_intensity'][i] = img_fish_mean[int(df_spots['x'][i]), int(df_spots['y'][i])] / mean_norm
        df_spots.to_csv(path_csv_folder + path_mask.name[:-4] + ".csv", index=False)

        dico_mean_spots[path_mask.name[:-4]] = np.sum(df_spots['in_mask'] != 0) / len(np.unique(mask)[1:])

        dico_mean_intensity[path_mask.name[:-4]] = np.mean(list_mean_intensity)

        dico_mean_intensity_normalize[path_mask.name[:-4]] = np.mean(list_mean_intensity) / np.mean(img_fish_mean[mask == 0])









   path_main_folder  = "/home/tom/Bureau/phd/Batrin/Images_pour_FISH/Expérience2/"
   path_ch0 = path_main_folder + "round_folder/ch0_mip/"
   path_mask_folder  = path_main_folder + "ch1_mask_mip/20_cyto/"
   path_csv_folder = path_main_folder + "round_folder/detection_csv/"
   dico_mean_spots = {}

   dico_snr = {}
   dico_mean_intensity = {}
   dico_mean_intensity_normalize = {}


   for path_mask in Path(path_mask_folder).glob("*tif*"):
        print(path_mask.name)
        mask = tifffile.imread(path_mask)
        img_fish = tifffile.imread(path_ch0 + path_mask.name[:-4])
        img_fish_mean = stack.mean_filter(img_fish, kernel_shape = "square", kernel_size = 4)


        df_spots = pd.read_csv(path_csv_folder + path_mask.name[:-4] + ".csv")
        df_spots['in_mask'] = 0
        df_spots['mean_intensity'] = 0
        df_spots['normalized_mean_intensity'] = 0

        list_spots = np.array([[x,y] for x, y in zip(df_spots['x'], df_spots['y'])])
        snr  = detection.compute_snr_spots(img_fish, list_spots, voxel_size = 108, spot_radius= 300)
        dico_snr[path_mask.name[:-4]] = snr
        list_mean_intensity = []
        mean_norm = np.mean(img_fish_mean[mask == 0])
        for i in range(len(df_spots)):
            if mask[int(df_spots['x'][i]), int(df_spots['y'][i])]  !=0:
                df_spots['in_mask'][i] =  mask[int(df_spots['x'][i]), int(df_spots['y'][i])]
                list_mean_intensity.append(img_fish_mean[int(df_spots['x'][i]), int(df_spots['y'][i])])


            df_spots['mean_intensity'][i] = img_fish_mean[int(df_spots['x'][i]), int(df_spots['y'][i])]
            df_spots['normalized_mean_intensity'][i] = img_fish_mean[int(df_spots['x'][i]), int(df_spots['y'][i])] / mean_norm
        df_spots.to_csv(path_csv_folder + path_mask.name[:-4] + ".csv", index=False)

        dico_mean_spots[path_mask.name[:-4]] = np.sum(df_spots['in_mask'] != 0) / len(np.unique(mask)[1:])

        dico_mean_intensity[path_mask.name[:-4]] = np.mean(list_mean_intensity)

        dico_mean_intensity_normalize[path_mask.name[:-4]] = np.mean(list_mean_intensity) / np.mean(img_fish_mean[mask == 0])








   path_main_folder  = "/home/tom/Bureau/phd/Batrin/Images_pour_FISH/Expérience3/"
   path_ch0 = path_main_folder + "round_folder/ch0_mip/"
   path_mask_folder  = path_main_folder + "ch1_mask_mip/20_cyto/"
   path_csv_folder = path_main_folder + "round_folder/detection_csv/"
   dico_mean_spots = {}

   dico_snr = {}
   dico_mean_intensity = {}
   dico_mean_intensity_normalize = {}


   for path_mask in Path(path_mask_folder).glob("*tif*"):
        print(path_mask.name)
        mask = tifffile.imread(path_mask)
        img_fish = tifffile.imread(path_ch0 + path_mask.name[:-4])
        img_fish_mean = stack.mean_filter(img_fish, kernel_shape = "square", kernel_size = 4)


        df_spots = pd.read_csv(path_csv_folder + path_mask.name[:-4] + ".csv")
        df_spots['in_mask'] = 0
        df_spots['mean_intensity'] = 0
        df_spots['normalized_mean_intensity'] = 0
        list_spots = np.array([[x,y] for x, y in zip(df_spots['x'], df_spots['y'])])
        snr  = detection.compute_snr_spots(img_fish, list_spots, voxel_size = 108, spot_radius= 300)
        dico_snr[path_mask.name[:-4]] = snr
        list_mean_intensity = []
        mean_norm = np.mean(img_fish_mean[mask == 0])
        for i in range(len(df_spots)):
            if mask[int(df_spots['x'][i]), int(df_spots['y'][i])]  !=0:
                df_spots['in_mask'][i] =  mask[int(df_spots['x'][i]), int(df_spots['y'][i])]
                list_mean_intensity.append(img_fish_mean[int(df_spots['x'][i]), int(df_spots['y'][i])])


            df_spots['mean_intensity'][i] = img_fish_mean[int(df_spots['x'][i]), int(df_spots['y'][i])]
            df_spots['normalized_mean_intensity'][i] = img_fish_mean[int(df_spots['x'][i]), int(df_spots['y'][i])] / mean_norm
        df_spots.to_csv(path_csv_folder + path_mask.name[:-4] + ".csv", index=False)

        dico_mean_spots[path_mask.name[:-4]] = np.sum(df_spots['in_mask'] != 0) / len(np.unique(mask)[1:])

        dico_mean_intensity[path_mask.name[:-4]] = np.mean(list_mean_intensity)

        dico_mean_intensity_normalize[path_mask.name[:-4]] = np.mean(list_mean_intensity) / np.mean(img_fish_mean[mask == 0])













