

import nd2



my_array = nd2.imread('/home/tom/Bureau/phd/Batrin/Images pour FISH/Expérience 2/Delta_adk1_pCenTy_001.nd2')



import napari


viwer = napari.Viewer()
viwer.add_image(my_array[:,1])



