# Tutorial

## How to use the PigeonSuperModel

On the next pages we show you how to use the pre-trained models on your own data. 

In short, you will have to:

1. _Download_ your PigeonSuperModel of choice
2. _Analyze_ your videos (GPU recommended)
4. _Extract and refine_ outlier frames (**optional**)
5. _Re-train_ the model with your expanded dataset (**optional**)
6. _Submit_ your new PigeonSuperModel to [GitLab](https://gitlab.ruhr-uni-bochum.de/ikn/pigeonsupermodel) (**optional**)



### DeepLabCut

In the **[next pages](DeepLabCut.md)** we provide you with commented jupyter notebooks to guide you through the entire process.

:::{note}
We started the PigeonSuperModel in [DeepLabCut](https://deeplabcut.github.io/DeepLabCut), so this has been our software of choice for a while now. Only after finishing the first models we decided to make the dataset systems agnostic and include further models, so the entire project may still be a little skewed towards DeepLabCut. Although we certainly recommend DeepLabCut as a great open source toolbox for markerless pose tracking, we want to acknowledge new, very promising approaches being released every few months.
Especially, but not exclusively, [SLEAP](https://sleap.ai/) for fast model training and multi-animal tracking, and [JARVIS](https://jarvis-mocap.github.io/jarvis-docs/) for training 3D-CNN instead of 2D-CNNs with post-hoc triangulation. Let us know what system you prefer and help us include it in the PigeonSuperModel.
:::


### SLEAP

:::{note}
This section is coming soon.
:::

