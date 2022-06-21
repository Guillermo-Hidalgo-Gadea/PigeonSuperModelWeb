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

In the next pages we provide you with commented jupyter notebooks to guide you through the entire process.

Click **[here](DeepLabCut.md)** for the DeepLabCut tutorial.

:::{note}
We started the PigeonSuperModel in [DeepLabCut](https://deeplabcut.github.io/DeepLabCut), so this has been our software of choice for a while now. Only after finishing the first models we decided to make the dataset systems agnostic and include further models, so the entire project may still be a little skewed towards DeepLabCut. Although we certainly recommend DeepLabCut as a great open source toolbox for markerless pose tracking, we want to acknowledge new, very promising approaches being released every few months.
Especially, but not exclusively, [SLEAP](https://sleap.ai/) for fast model training and multi-animal tracking, and [JARVIS](https://jarvis-mocap.github.io/jarvis-docs/) for training 3D-CNN instead of 2D-CNNs with post-hoc triangulation. Let us know what system you prefer and help us include it in the PigeonSuperModel.
:::

If you need any further help with DeepLabCut beyond the code snippets provided, just [get in touch](GetInTouch.md). We are happy to point you in the right direction and recommend our favorite beginner friendly tutorials. You can also chek our [DeepLabCut Guide](DLC_StudentGuide.ipynb) and our seminar website on [Tracking Animal Behavior](https://guillermo-hidalgo-gadea.github.io/Seminar-TrackingAnimalBehavior/intro.html) at the Ruhr University Bochum with some useful tipps for [troubleshooting](https://guillermo-hidalgo-gadea.github.io/Seminar-TrackingAnimalBehavior/Exercise3.html#troubleshooting) your DeepLabCut projects.

### SLEAP

:::{note}
This section is coming soon.
:::

