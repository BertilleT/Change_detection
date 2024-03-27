Project on Change Detection from AI and Environment course, MVA 2024. 

<<<<<<< Updated upstream
The script for the OSCD datset were taken from : https://github.com/rcdaudt/fully_convolutional_change_detection.   

Data:
  - OSCD: https://ieee-dataport.org/open-access/oscd-onera-satellite-change-detection.   
  - HRSCD: https://ieee-dataport.org/open-access/hrscd-high-resolution-semantic-change-detection-dataset
=======
Data: https://ieee-dataport.org/open-access/oscd-onera-satellite-change-detection. 


## Src folder description

- `binary_CD_HRSCD.ipynb`: Jupyter notebook for performing binary change detection on the High Resolution Semantic Change Detection (HRSCD) dataset. 

- `binary_CD_OSCD.ipynb`: Jupyter notebook for binary change detection on the OSCD (Other Satellite Change Detection) dataset. Code from https://github.com/rcdaudt/fully_convolutional_change_detection. 

- `siamunet_conc.py`: Implementation of the Siamese U-Net with a concatenation approach, for binary change detection.

- `siamunet_diff.py`: Implementation of the Siamese U-Net with a difference approach, for binary change detection. 

- `split_HRSCD_train_valid_test.py`: Script for splitting the HRSCD dataset into training, validation, and test sets, ensuring a balanced distribution.

- `unet.py`: The U-Net architecture, a foundational model for semantic segmentation tasks in satellite image analysis.
>>>>>>> Stashed changes
