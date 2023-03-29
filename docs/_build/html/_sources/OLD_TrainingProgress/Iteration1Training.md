# Training: iteration-1
:::{note}
This jupyter book is a work in progress. This page will shortly be extended.
:::

## Additional Video Data, Video Analysis & Outlier Refinement
For the subsequent refinement of the model, we included 10 new video files that were acquired during further experimental sessions in the StopSignalParadigm setup and in the HexagonalArena setup.  
The position of the two GoPro HERO5 cameras had been changed in the StopSignalParadigm setup to allow for improved later triangulation (see table below). In the new setup, both cameras are fixed to the front side of the skinnerbox.

<!---add TABLE--->

In total, we used four additional StopSignalParadigm videos deriving from the new camera setup for the second training iteration (iteration 1).  
Moreover, two video files from the StopSignalParadigm setup that had initially been included in the labeling/training process were excluded from the project due to missing information on their origin (date of acquisition, pigeon, etc.)

There had also been a change in the HexagonalArena setup as the arena had been equipped with a different colored carpet and additional chessboard markers to allow for subsequent triangulation (see table below).

<!---add TABLE--->

The video footage for the ImagingSkinnerbox setup remained unchanged.  
We analyzed all videos (new + old ones) except the excluded ones with the pretrained model and then extracted outlier frames for all the videos. We extracted 5 outlier frames per analyzed video and therefore ended up with a total of 10 frames for each of the old videos and a total of five frames for the new ones.  
We refined the extracted outlier frames using the labeling GUI and a p-cutoff of 0.3. Subsequently, we merged the resulting h5 files to the training dataset.

Eventually, the extended training dataset for training iteration 1 consisted of 210 manually labeled frames that were taken from a compound of videos summarized in the table below:

|                                       |                         |     StopSignalParadigm    |     HexagonalArena    |     ImagingSkinnerbox    |
|---------------------------------------|-------------------------|---------------------------|-----------------------|--------------------------|
|     Iiteration 0                      |     # sessions          |     3                     |     1                 |     1                    |
|                                       |     # pigeons           |     3                     |     1                 |     1                    |
|                                       |     # videos            |     6                     |     6                 |     6                    |
|                                       |     # camera angles     |     2                     |     6                 |     6                    |
|                                       |     # labeled frames    |     30                    |     30                |     30                   |
|     Iteration 1                       |     # sessions          |     4                     |     2                 |     1                    |
|                                       |     # pigeons           |     3                     |     2                 |     1                    |
|                                       |     # videos            |     8                     |     12                |     6                    |
|                                       |     # camera angles     |     4                     |     6                 |     6                    |
|                                       |     # labeled frames    |     60                    |     90                |     60                   |
|     # frames total   (iteration 1)    |                         |     210                   |                       |                          |

We started the second training iteration on January, 17.01.2022.

## 