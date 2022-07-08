# DeepLabCut

## How to use the PigeonSuperModel

The easiest way to use our pre-trained models is to download them with DeepLabCut ModelZoo. This notebook will show you how to do that:

* [How to use the PigeonSuperModel](HowToPigeonSuperModel.ipynb)

## How to use the PigeonSuperModel Dataset

You want more? After creating your own PigeonSuperModel project and labeling some frames of your own, you can download and merge our entire labeled dataset for free to increse the size of your own training dataset. Check out the the step by step guide in the notebook below:

* [How to use the PigeonSuperModel Dataset](HowToPigeonSuperModelDataset.ipynb)

## DeepLabCut Guides and HowTos

Need some further help? Check our step by step guide:

* [DeepLabCut - A Student’s Quick Start Guide](DLC_StudentGuide.ipynb)

You can also brows some of our seminar websites on [Tracking Animal Behavior](https://guillermo-hidalgo-gadea.github.io/Seminar-TrackingAnimalBehavior/intro.html) and [Computational Ethology](https://guillermo-hidalgo-gadea.github.io/Seminar-ComputationalEthology/intro.html) at the Ruhr University Bochum.

## Using Anipose for 3D Pose Reconstruction

Why stop at 2D tracking when your tracked animals move in 3D space? Pigeons in particular have a naturally upright pose, which makes 2D poses often hard to interpret. For some help on multi-camera recording see [syncFLIR](https://gitlab.ruhr-uni-bochum.de/ikn/syncflir) and [JARVIS](https://jarvis-mocap.github.io/jarvis-docs//2021-10-29-manual.html#designing-a-3d-motion-capture-setup). Here we provide a short introduction on how to use [Anipose](https://anipose.readthedocs.io/en/latest/) to upgrade your DeepLabCut projects for 3D pose reconstruction:

* [Using Anipose for 3D Pose Reconstruction](UsingAnipose3D.ipynb)

## Example Analysis with PigeonSuperModel Tracking

Need some inspiration? In the following notebooks we give you some examples of what you can do with tracking data after using the PigeonSuperModel:

* [Locomotion tracking in Pigeons](LocomotionTrackingPigeon.ipynb)