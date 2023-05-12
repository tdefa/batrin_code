

import napari
import numpy as np
import tifffile
from pathlib import Path
import pandas as pd


def plot_spots_detection(
      df_spots_path = "/home/tom/Bureau/phd/Batrin/Images_pour_Pasteur/round_folder/detection_csv/Delta_adk1_pCenTy_001.tiff.csv" ,
      path_to_img = "/home/tom/Bureau/phd/Batrin/Images_pour_Pasteur/round_folder/ch0_mip/Delta_adk1_pCenTy_001.tiff",
       spots_size = 4):


    df_spots = pd.read_csv(df_spots_path)
    img = tifffile.imread(path_to_img)
    viewer = napari.Viewer()
    viewer.add_image(img)
    viewer.add_points(df_spots[['x', 'y']], size=spots_size, face_color='red')