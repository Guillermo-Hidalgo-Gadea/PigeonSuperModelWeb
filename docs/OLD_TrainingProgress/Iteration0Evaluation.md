# Evaluation: iteration-0
:::{note}
This jupyter book is a work in progress. This page will shortly be extended.
:::

After training was completed, we executed deeplabcut.evaluate_network and compared the models’ labeling accuracies. Setting the plotting-parameter to TRUE printed the test- and training-frames together with the manually applied labels and the computed machine labels.

Here, the evaluation results for each of the trained models are compared by exemplarily depicting three of the test and training frames from each of the three included experimental settings.

:::{note}
Labeling results are depicted acording to this scheme:  
“+”: Original markers set by the human scorer,  
“x” : Markers computed by the model, label accuracy < …% ,  
“dot”: Markers computed by the model, label accuracy > …
:::

The frames were trimmed, focusing on the pigeon, and excluding the experimental surrounding.

## StopSignalParadigm
<!---TABLE--->

## ImagingSkinnerbox
<!---TABLE--->

## HexagonalArena
<!---TABLE--->

## Statistics
The model that was trained using a 50-layer residual neural network, showed surprisingly good results after the first training iteration. However, it should be noted, that there are seemingly less “dots” depicted in the training and test frames compared to those computed by the other models, indicating, that the labeling accuracy of the resnet_50 model is somewhat lower than that of both other models.

When comparing the labeled video files from resnet101 to those that were rendered using resnet50 (see above), those from resnet 101 seem to be a little bit more accurate. The same is true for ResNet_152 when its analysis results are compared to those of ResNet_50 and ResNet_101.

The formal evaluation results are summarized in the table below:

|                    |                              |     ResNet_50    |     ResNet_101    |     ResNet_152    |
|--------------------|------------------------------|------------------|-------------------|-------------------|
|     Iteration 0    |     training   iterations    |                  |     1030000       |     1030000       |
|                    |     training   dataset       |                  |     95            |     95            |
|                    |     train   error            |                  |     1.12          |     1.04          |
|                    |     test   error             |                  |     38.11         |     18.74         |
|                    |     p-cutoff   used          |                  |     0.3           |     0.3           |
