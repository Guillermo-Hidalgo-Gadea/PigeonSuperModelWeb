# DeepLabCut

There are several ways to use the PigeonSuperModel in DeepLabCut.

## Using the DeepLabCut Model Zoo

The easiest way to use our models is to download them directly from the DeepLabCut Model Zoo.

:::{note}
This option is not yet available, but we have come up with a solution that will allow you to use our models as if they already were included into the Model Zoo.

To do so, use [this link](https://gitlab.ruhr-uni-bochum.de/ikn/pigeonsupermodel/-/tree/main/models/DeepLabCut) to download the pre-trained model of your choice (`resnet-50`, `resnet-101` or `resnet-152`).

Then download this Jupyter Notebook to start analyzing your data.
:::

## Using the provided dataset to train your own model

You can of course also use our dataset, to train novel DeepLabCut models.

## Adapting the model to your experimental setup

<!---Add labels / Train reference model?--->

If you've wondered how you could adapt the Pigeon Super Model to your own experimental setup and include novel labels for specific key features, here is the answer you have been looking for:

First of all, we would not recommend adding new labels to the original Pigeon Super Model.

As a solution for this issue, we recommend training a novel DeepLabCut model to recognize only the surrounding of your experiment, excluding the pigeon.  
If you filmed your video data from a stable perspective so that the background hardly ever changes throughout your videos, the manual labeling task for this separate model will not take long (as you can copy-and-paste the labels for almost all your frames).

After training this reference model sufficiently, the analysis results of both models can be merged, generating output labels for both, the pigeon and your experimental setup's key features.
