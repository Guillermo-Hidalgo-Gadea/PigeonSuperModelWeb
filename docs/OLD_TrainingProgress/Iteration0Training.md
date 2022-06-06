# Training: iteration-0
:::{note}
This jupyter book is a work in progress. This page will shortly be extended.
:::

## Initial video data
For the initial model (first training iteration/ iteration_0), we included a total amount of 18 videos, deriving from different experiments that are conducted at the Lab for Biopsychology of the Ruhr University Bochum. The videos show pigeons behaving in different experimental setups as they participate in each experiment.

The experimental setups, video acquisition and preprocessing of videos are described below.

## StopSignalParadigm (6 videos)
The first experimental setup consists of a conventional skinnerbox, equipped with diverse pecking keys and a feeder apparatus, that is used to train the pigeons in a stop signal paradigm and stop change paradigm, respectively.  
In this setup, the pigeon’s behavior is captured from two different camera angles simultaneously. Two representative frames for each camera are depicted below. It is to be noted that in this setup it can come to partly occlusions of the points of interest due to the pigeon moving out of the picture (see perspective camB).

<!---add TABLE--->

For the first training iteration, we included six videos from this experiment into the project – three videos per camera. The videos were filmed using GoPro HERO5 cameras.  
Two of the initially included videos later were excluded from the project due to insufficient meta data (date of acquisition, pigeon identity, etc.).

## ImagingSkinnerbox (6 videos)
In this setup, the pigeon behaves inside a skinnerbox, the walls of which are made of plexiglass. This allows for lots of cameras to be placed around the box that aim for detailed close-up shots (e.g., pigeons feet). By including this footage, we hope to increase the models ability to reliably recognize and differentiate the defined points of interest even when there are major occlusions in the regarded frames.  
A total of six cameras is used in this setup, each filming from a different angle.

<!---add TABLE--->

As can be seen in the snapshots depicted above, all videos from this setup are rotated by 180 degrees and therefore depict the pigeon “upside down”.
For the first training iteration, we included one video per camera angle, resulting in a total of six videos from the given experimental setup.

## HexagonalArena (6 videos)
In this experiment, the pigeon is moving freely inside a hexagonal arena. The filmed space is therefore much larger than in the other two setups, resulting in larger camera-to-pigeon-distance for all camera angles.  
There are six cameras mounted to the corners of the arena, each of which capturing the entire floor of the pigeon’s movement space.

<!---add TABLE--->

Due to the large camera-to-pigeon-distance, the video resolution for the pigeon itself is lower than in the other two setups, letting the pigeon appear much more “pixelated”. This might pose a special challenge for the initial training process and for the manual labeling process, but if the model training continues successful, the resulting model’s generalizability is likely to increase severely.
As for the other setups, six videos from this experiment were used for the first training iteration – one per camera.

## Video Preprocessing
All videos were renamed according to the following scheme:  
YYYY_MM_DD_ExperimentalSetup_P007_camX_partX.MP4

When filming for extended periods of time, GoPro cameras save the captured footage as multiple MP4 files, rather than as one file. Therefore, it is necessary to merge the original video files into a single MP4 file. For the regarding files, this was done using the concatenation function that is embedded in the VideoPyToolbox.  
Moreover, all video files were split using the VideoPyToolbox to exclude periods at the beginning and end of the recording when the pigeon is not in the picture.  
Afterwards, the resulting files were compressed by applying a common hevc compression (crf = 18), using the VideoPyToolbox.
Having been preprocessed accordingly, the videos were added to the DeepLabCut project and frames were extracted.

<!---Definitely need to specify!--->

## Training Dataset (iteration-0)
For the first training iteration (iteration 0), we extracted 5 frames per video (using kmeans algorithm). This resulted in a total of 90 extracted frames.  
Using the DeepLabCut labeling GUI, the extracted frames were labeled manually (see above for a list of the applied labels).

:::{note}
As we were having troubles launching the labeling GUI from the terminal / via jupyter notebook (there was an issue with saving the applied labels), we used the main DeepLabCut graphical user interface for this part.
:::

### Hints & Tricks for the Labeling Process <!---MOVE TO TUTORIAL SECTION--->
* Directional indications („left“ / “right”) always refer to the perspective of the bird. (e.g. “RigthWingTip” = tip of the birds right wing)
* Note that this type of directional information is easily confused during the manual labeling process (e.g. when the bird is seen from a frontal perspective). Take extra care and make sure that you do not confuse “right” and “left” in a single frame for this would have negative implications for your training model. (You should also run the check_labels function
* For some labels, the exact points on the pigeons body are rarely visible (e.g. “Chin”). However, in some cases the respective labels can still be applied approximately at the correct position (e.g. when the bird is seen in a side view). In such cases, DeepLabCut will still be able to learn the correct position of the labels by averaging all occursions.
* Due to the physique and plumage of pigeons, many of the points to be labeled are often difficult to differentiate. (This is especially true for the shoulders and for the “MiddleThroat”). Take extra care with these respective labels and try to label the same spot in every frame.

### Training Dataset Composition 
After having completed the manual labeling, we ran the deeplabcut.check_labels function and double-checked all frames for any errors.

Afterwards, the labeled frames’ h5-files were combined into a single training dataset using the deeplabcut.create_training_model_comparison function. We did not use the “normal” create_training_dataset function since we wanted to train three independent models based on different types of residual neural networks to compare their analysis performances.  
We left the TrainingFraction parameter in the config.yaml file at the default value (0.95), which resulted in the creation of a training dataset consisting of 5 test frames and 85 training frames.

Subsequently, we trained different types of residual neural networks using the same training dataset (=same training- and test-frames) for each network.  
The developers of the DeepLabCut toolbox [recommend](https://github.com/DeepLabCut/DeepLabCut/wiki/What-neural-network-should-I-use%3F-(Trade-offs,-speed-performance,-and-considerations)) using ResNet-50 when using DeepLabCut for lab applications. However, we still wanted to compare the different network’s results for our own data and hence trained a ResNet_50, ResNet_101 and a Resnet_152, respectively.

The final composition of the training dataset consisting of 90 labeled frames for the first training iteration is summarized below:
|                                       |                         |     StopSignalParadigm    |     HexagonalArena    |     ImagingSkinnerbox    |
|---------------------------------------|-------------------------|---------------------------|-----------------------|--------------------------|
|     Iiteration 0                      |     # sessions          |     3                     |     1                 |     1                    |
|                                       |     # pigeons           |     3                     |     1                 |     1                    |
|                                       |     # videos            |     6                     |     6                 |     6                    |
|                                       |     # camera angles     |     2                     |     6                 |     6                    |
|                                       |     # labeled frames    |     30                    |     30                |     30                   |
|     # frames total   (iteration 0)    |                         |     90                    |                       |                          |
