# Handwritten_text_recording
recording of
Project: identification of English handwriting with artificial intelligence
Libraries Used:
* Python 3.x
* OpenCV 4.x
* Editdistance
 TensorFlow 2.0
Dataset Used: Bentham: http://transcriptorium.eu/datasets/bentham-collection/
Arguments from the command line:
* - dataset: dataset name (bentham))
* -- arch: network to use (puigcerver, bluche, fluorine)
* -- transform: convert dataset to HDF5 file
* -- cv2: sample visualization from converted dataset
* -- train: train model using dataset argument
* -- test: evaluating and estimating the model using the dataset argument
* -- epochs: number of periods
* -- batch_size: number of dimensions of each partition
Project summary: 
The handwriting text recognition (HTR) system was implemented using TensorFlow 2.0 and trained from Bentham handwriting datasets.  This neural network model recognizes text contained in images of segmented lines of text.
Data partitioning (train, validation, test) was performed following the methodology of each dataset. The project implemented the htrmodel abstraction model (adapted from Ctcmodel ) to facilitate the development of handwriting identification systems.


Sources used:
* https://towardsdatascience.com/build-a-handwritten-text-recognition-system-using-tensorflow-2326a3487cd5
* https://github.com/mburaksayici/turkce-derin-ogrenme-kaynaklari
* https://core.ac.uk/download/pdf/11743110.pdf
* https://www.youtube.com/watch?v=mfw8ruywyeı
* https://github.com/ardamavi/HandwritingRecognition/
* https://www.youtube.com/watch?v=y-Jb0fXcFVU
*https://www.youtube.com/watch?v=GhV0CLwhd3k&list=PLDhGq4xb3blT41_BE98Mbs7ZRvFduhu69&index=1
