#!/usr/bin/env python
# coding: utf-8

# # How to use the PigeonSuperModel
# 
# Download this notebook in the upper right corner as `.ipynb` file and start it from within your DeepLabCut environment. If you need to install DeepLabCut first, please check [here](https://pigeonsupermodel.com/DLC_StudentGuide.html#installation). 
# 
# This notebook will show you how to create a pretrained project with the PigeonSuperModel using the DeepLabCut ModelZoo to analyze your own pigeon video data:
# 
# * Preliminary Settings
# * Create Pretrained Model
# * Model Settings
# * Analyze New Videos
# * Filter Predictions (**optional**)
# * Create Labeled Videos (**optional**)

# ## Some preliminary settings
# 
# Remember to start this notebook from within your deeplabcut anaconda environment to have access to the packages below.

# In[1]:


import os
import urllib
import cv2
import deeplabcut


# The PigeonSuperModel is not yet included in the DeepLabCut model zoo, therefore, you will have to download it directly from our [GitLab repository](https://gitlab.ruhr-uni-bochum.de/ikn/pigeonsupermodel/-/tree/main/models/DeepLabCut). To do so, you will need to make some small changes in your local DeepLabCut installation directory. The function `monkeypatch()` below helps you do exatly that. First, it locates a file named `pretrained_model_urls.yaml` in your local DeepLabCut installation and adds the new URLs to reach the PigeonSuperModel repository. In a last step, it adds the names of the PigeonSuperModels to the `modelzoo.py` Modeloptions as valid model names. After this, you are all set to use the oficial function `deeplabcut.create_pretrained_project()` to create a pretrained project with the PigeonSuperModel.
# 
# :::{note}
# This monkeypatch is hopefully outdated soon, when the PigeonSuperModel is officially supported by the DeepLabCut ModelZoo. 
# :::

# In[42]:


def monkeypatch():
    '''
    This function locates a file named 'pose_estimation_tensorflow/models/pretrained/pretrained_model_urls.yaml' in your local DeepLabCut
    installation and adds the new URLs below to reach the PigeonSUperModel repository.
    In a last step, the names of the PigeonSuperModels are added to the 'modelzoo.py' Modeloptions as valid model names.
    '''
    
    import os
    import deeplabcut
    from deeplabcut.utils import auxiliaryfunctions
    from deeplabcut.create_project import modelzoo

    # locate the `pretrained_model_urls.yaml` file in your local DeepLabCut installation (hardcoded based on deeplabcut dir structure)
    neturls_path = os.path.join(auxiliaryfunctions.get_deeplabcut_path(), 'pose_estimation_tensorflow', 'models', 'pretrained', 'pretrained_model_urls.yaml')

    edits = {'PigeonSuperModel_resnet_50':  'https://gitlab.ruhr-uni-bochum.de/ikn/pigeonsupermodel/-/raw/main/models/DeepLabCut/DLC_PigeonSuperModel_01_resnet_50_iteration-2_shuffle-3.tar.gz',
             'PigeonSuperModel_resnet_101': 'https://gitlab.ruhr-uni-bochum.de/ikn/pigeonsupermodel/-/raw/main/models/DeepLabCut/DLC_PigeonSuperModel_01_resnet_101_iteration-2_shuffle-4.tar.gz', 
             'PigeonSuperModel_resnet_152': 'https://gitlab.ruhr-uni-bochum.de/ikn/pigeonsupermodel/-/raw/main/models/DeepLabCut/DLC_PigeonSuperModel_01_resnet_152_iteration-2_shuffle-5.tar.gz'}
    
    # add new model to the neturls file     
    deeplabcut.auxiliaryfunctions.edit_config(neturls_path, edits)

    # add new model to locally loaded Modeloptions from modelzoo.py
    modelzoo.Modeloptions.extend(['PigeonSuperModel_resnet_50', 'PigeonSuperModel_resnet_101', 'PigeonSuperModel_resnet_152'])
    
# you may need admin rights on your computer to edit the files above
monkeypatch()


# ## Create your local PigeonSuperModel project
# 
# First, you should start by setting a path to where your project should be created, and giving your new project a salient but short name.

# In[46]:


# give it a place to be
projectpath = r'D:/'

# give it a name
projectname = r'My2PigeonSuperModel'


# Next, we will use DeepLabCuts own function `deeplabcut.create_pretrained_project()` to create a pretrained project. Unfortunately, (or maybe by design?) this function assumes you want to directly include your videos to the project `videodir`, which may be not the most efficient way to go when you work with large videos (videos will be copied, not moved, which may take quite a while and use up space unnecessarily.
# 
# My recommendation is to use the cell block below to create a 1-sec dummy video to initialize your pretrained project. Then change any settings you want to in the config file, and finally select the videos you whant to analyze from a different directory to save time and storage. 

# In[48]:


# create a dir with pre-trained DLC models
model_dir = os.path.join(projectpath, projectname)
try:
    os.makedirs(model_dir)
    os.chdir(model_dir)

    # create dummy video
    logolink = 'https://gitlab.ruhr-uni-bochum.de/ikn/pigeonsupermodel/-/raw/main/PigeonSuperModel.png?inline=false'
    logo = os.path.join(model_dir, 'logo.png')
    urllib.request.urlretrieve(logolink, logo);

    dummyvideo = os.path.join(model_dir, 'logo.mp4')
    img_array = []
    for i in range(20):
        img = cv2.imread(logo)
        height, width, layers = img.shape
        img_array.append(img)

    out = cv2.VideoWriter(dummyvideo, cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

    video_path = dummyvideo
except:
    print('Error: The project directory could not be created. See if the model already exists, and check your write permissions on that disk.')


# Now you can create a pretrained DeepLabCut project. If prefere, you could directly create a list of videos to include in the project `[video_path]` and even activate `analyzevideo=True` to start analyzing right away, but I would advise to start slow, and check your settings of your new project first.

# In[ ]:


# create pre-trained model from PigeonSuperModel
config_path, _ = deeplabcut.create_pretrained_project(
    projectname,
    'PigeonSuperModel',
    [video_path],
    videotype='mp4',
    copy_videos=True,
    working_directory=os.path.join(projectpath, projectname),
    model='PigeonSuperModel_resnet_152',
    analyzevideo=False,
    filtered=False,
    createlabeledvideo=False,
    )


# In[45]:


# delete dummy videos created before
os.remove(dummyvideo)
os.remove(logo)


# ## Check project settings
# 
# Now that you have your local copy of the PigeonSuperModel, you can open your `config.yaml` file to check your settings, specially the skeleton and your prefered plotting configuration.
# Alternatively, you can use the function `deeplabcut.auxiliaryfunctions.edit_config()` to pass any changes to the `config.yaml` file as below. 

# In[52]:


# manually edit your config.yaml as needed
edits = {
    'skeleton': [
        ['BT(BeakTip)', 'LC(LowerCere)'], 
        ['LC(LowerCere)', 'UC(UpperCere)'], 
        ['UC(UpperCere)', 'H(Head)'], 
        ['H(Head)', 'LE(LeftEye)'], 
        ['H(Head)', 'RE(RightEye)'], 
        ['LE(LeftEye)', 'RE(RightEye)'], 
        ['LE(LeftEye)', 'UC(UpperCere)'], 
        ['LE(LeftEye)', 'UN(UpperNeck)'], 
        ['RE(RightEye)', 'UC(UpperCere)'], 
        ['RE(RightEye)', 'UN(UpperNeck)'], 
        ['LE(LeftEye)', 'C(Chin)'], 
        ['RE(RightEye)', 'C(Chin)'], 
        ['H(Head)', 'UN(UpperNeck)'], 
        ['UN(UpperNeck)', 'UHN(UpperHalfNeck)'], 
        ['UHN(UpperHalfNeck)', 'MN(MiddleNeck)'], 
        ['MN(MiddleNeck)', 'LHN(LowerHalfNeck)'], 
        ['LHN(LowerHalfNeck)', 'US(UpperSpine=LN)'], 
        ['US(UpperSpine=LN)', 'UHS(UpperHalfSpine)'], 
        ['UHS(UpperHalfSpine)', 'MS(MiddleSpine)'], 
        ['MS(MiddleSpine)', 'LHS(LowerHalfSpine)'], 
        ['LHS(LowerHalfSpine)', 'LS(LowerSpine)'], 
        ['LS(LowerSpine)', 'TC(TailCenter)'], 
        ['LS(LowerSpine)', 'TL(TailLeft)'], 
        ['LS(LowerSpine)', 'TR(TailRight)'], 
        ['TL(TailLeft)', 'TC(TailCenter)'], 
        ['TC(TailCenter)', 'TR(TailRight)'], 
        ['US(UpperSpine=LN)', 'LWS(LeftWingShoulder)'], 
        ['LWS(LeftWingShoulder)', 'LWE(LeftWingElbow)'], 
        ['LWE(LeftWingElbow)', 'LWW(LeftWingWriwst)'], 
        ['LWW(LeftWingWriwst)', 'LWT(LeftWingTip)'], 
        ['US(UpperSpine=LN)', 'RWS(RightWingShoulder)'], 
        ['RWS(RightWingShoulder)', 'RWE(RightWingElbow)'], 
        ['RWE(RightWingElbow)', 'RWW(RightWingWriwst)'], 
        ['RWW(RightWingWriwst)', 'RWT(RightWingTip)'], 
        ['LWS(LeftWingShoulder)', 'LC(LeftChest)'], 
        ['LC(LeftChest)', 'LHC(LeftHalfChest)'], 
        ['LHC(LeftHalfChest)', 'MC(MiddleChest)'], 
        ['MC(MiddleChest)', 'RHC(RightHalfChest)'], 
        ['RHC(RightHalfChest)', 'RC(RightChest)'], 
        ['RC(RightChest)', 'RWS(RightWingShoulder)'], 
        ['MC(MiddleChest)', 'MT(MiddleThroat)'], 
        ['MT(MiddleThroat)', 'C(Chin)'], 
        ['C(Chin)', 'BT(BeakTip)'], 
        ['RF(RightFoot)', 'RA(RightAnkle)'], 
        ['RA(RightAnkle)', 'RT(RightTibia)'], 
        ['RT(RightTibia)', 'RWS(RightWingShoulder)'], 
        ['RT(RightTibia)', 'LS(LowerSpine)'], 
        ['RT(RightTibia)', 'MC(MiddleChest)'], 
        ['LF(LeftFoot)', 'LA(LeftAnkle)'], 
        ['LA(LeftAnkle)', 'LT(LeftTibia)'], 
        ['LT(LeftTibia)', 'LWS(LeftWingShoulder)'], 
        ['LT(LeftTibia)', 'LS(LowerSpine)'], 
        ['LT(LeftTibia)', 'MC(MiddleChest)'], 
        ['RC(RightChest)', 'MT(MiddleThroat)'], 
        ['LC(LeftChest)', 'MT(MiddleThroat)'], 
        ['LHC(LeftHalfChest)', 'MT(MiddleThroat)'], 
        ['RHC(RightHalfChest)', 'MT(MiddleThroat)'], 
        ['C(Chin)', 'LHC(LeftHalfChest)'], 
        ['C(Chin)', 'RHC(RightHalfChest)'], 
        ['C(Chin)', 'LC(LeftChest)'], 
        ['C(Chin)', 'RC(RightChest)'], 
        ['C(Chin)', 'LWS(LeftWingShoulder)'], 
        ['C(Chin)', 'RWS(RightWingShoulder)'], 
        ['US(UpperSpine=LN)', 'RWT(RightWingTip)'], 
        ['RWS(RightWingShoulder)', 'RWT(RightWingTip)'], 
        ['RWE(RightWingElbow)', 'RWT(RightWingTip)'], 
        ['US(UpperSpine=LN)', 'LWT(LeftWingTip)'], 
        ['LWS(LeftWingShoulder)', 'LWT(LeftWingTip)'], 
        ['LWE(LeftWingElbow)', 'LWT(LeftWingTip)'], 
        ['RT(RightTibia)', 'RC(RightChest)'], 
        ['RT(RightTibia)', 'RHC(RightHalfChest)'], 
        ['LT(LeftTibia)', 'LC(LeftChest)'], 
        ['LT(LeftTibia)', 'LHC(LeftHalfChest)'], 
        ['RWS(RightWingShoulder)', 'TR(TailRight)'], 
        ['LWS(LeftWingShoulder)', 'TL(TailLeft)'], 
        ['UN(UpperNeck)', 'RWS(RightWingShoulder)'], 
        ['UN(UpperNeck)', 'RWE(RightWingElbow)'], 
        ['UN(UpperNeck)', 'LWS(LeftWingShoulder)'], 
        ['UN(UpperNeck)', 'LWE(LeftWingElbow)'], 
        ['UN(UpperNeck)', 'UHN(UpperHalfNeck)'],
        ],
    'dotsize': 7,  # size of the dots!
    'colormap': 'inferno',  # any matplotlib colormap!
    'pcutoff': 0.5,  # the higher the threshold, the more conservative the plotting!
}

# write new skeleton into config.yaml file
deeplabcut.auxiliaryfunctions.edit_config(config_path, edits);


# ## Analyze new videos
# 
# Now that your new pretrained project is ready to go, you can start analyzing your own videos. You could open the project from the GUI in anaconda with `python -m deeplabcut`, or just run the analysis from this notebook. To analyze selected videos create a `videolist`, and to analyze all videos within a given directory, pass the `videodir`. 

# In[ ]:


# define a list of videos
videolist = ['C:\\Users\\computername\\Videos\\reachingvideo1.avi', 
            'C:\\Users\\computername\\Videos\\reachingvideo2.avi', 
            'C:\\Users\\computername\\Videos\\reachingvideo3.avi']

# define entire video virectory
videodir = 'C:\\Users\\computername\\Videos'

# define output directory for DLC outputs
outputdir = 'C:\\Users\\computername\\DLC_Outputs'


# In[ ]:


# analyze list of videos
deeplabcut.analyze_videos(config_path, videolist, save_as_csv=True, destfolder=outputdir, videotype='mp4')


# In[ ]:


# analyze entire directory
deeplabcut.analyze_videos(config_path, [videodir], save_as_csv=True, destfolder=outputdir, videotype='mp4')


# ## Filter Predictions (Optional)

# In[ ]:


deeplabcut.filterpredictions(config_path, videolist, videotype='mp4', filtertype= 'arima', ARdegree=5, MAdegree=2)


# ## Create Labeled Videos (Optional)

# In[ ]:


deeplabcut.create_labeled_video(config_path, videolist, videotype='mp4', filtered=True, trailpoints=10, draw_skeleton = True, keypoints_only=False)


# In[ ]:


deeplabcut.plot_trajectories(config_path, videolist)

