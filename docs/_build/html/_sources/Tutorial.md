# Tutorials

On this page we show you how to use the pre-trained models on your own data. 

:::{note}
We started the PigeonSuperModel in [DeepLabCut](https://deeplabcut.github.io/DeepLabCut), so this has been our software of choice for a while now. While we certainly recommend DeepLabCut as a great open source toolbox for markerless pose tracking, we want to acknowledge new, very promising approaches being released every few months. Especially, but not exclusively, [SLEAP](https://sleap.ai/) for fast model training and multi-animal tracking, and [JARVIS](https://jarvis-mocap.github.io/jarvis-docs/) for training 3D-CNN instead of 2D-CNNs with post-hoc triangulation. Let us know what system you prefer and help us include it in the PigeonSuperModel.
:::

In short, you will have to:

1. _Download_ your PigeonSuperModel of choice
2. _Analyze_ your videos (GPU recommended)
3. _Extract and refine_ outlier frames (**optional**)
4. _Re-train_ the model with your expanded dataset (**optional**)

Below, we provide you with commented jupyter notebooks to guide you through the entire process.

## How to use the pre-trained models
:::{note}
Deprecated since DeepLabCut 2.3 model zoo migrated to hugging face. 
:::

The easiest way to use our pre-trained models is to download them with DeepLabCut ModelZoo. This notebook will show you how to do that:

* [How to use the PigeonSuperModel](HowToPigeonSuperModel.ipynb)

## How to use the labeled dataset

You want more? After creating your own PigeonSuperModel project and labeling some frames of your own, you can download and merge our entire labeled dataset to increse the size of your own training dataset. Check out the step by step guide in the notebook below:

* [How to use the PigeonSuperModel Dataset](HowToPigeonSuperModelDataset.ipynb)

## Other useful DeepLabCut Guides and HowTos

Need some further help? Check our step by step guide:

* [DeepLabCut - A Student’s Quick Start Guide](DLC_StudentGuide.ipynb)

You can also brows some of our seminar websites on:

* [Tracking Animal Behavior](https://guillermo-hidalgo-gadea.github.io/Seminar-TrackingAnimalBehavior/intro.html) 
* [Computational Ethology](https://guillermo-hidalgo-gadea.github.io/Seminar-ComputationalEthology/intro.html)

## 3D Pose Reconstruction

Why stop at 2D tracking when your tracked animals move in 3D space? Pigeons in particular have a naturally upright pose, which makes 2D poses often hard to interpret. For some help on multi-camera recording see [syncFLIR](https://gitlab.ruhr-uni-bochum.de/ikn/syncflir) and [JARVIS](https://jarvis-mocap.github.io/jarvis-docs//2021-10-29-manual.html#designing-a-3d-motion-capture-setup). Here we provide a short introduction on how to use [Anipose](https://anipose.readthedocs.io/en/latest/) to upgrade your DeepLabCut projects for 3D pose reconstruction:

* [Using Anipose for 3D Pose Reconstruction](UsingAnipose3D.ipynb)

Need some inspiration? In the following notebooks we give you some examples of what you can do with tracking data after using the PigeonSuperModel:

* [Locomotion tracking in Pigeons](LocomotionTrackingPigeon.ipynb)