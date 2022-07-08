#!/usr/bin/env python
# coding: utf-8

# # Using Anipose for 3D Pose Reconstruction
# 
# Download this notebook in the upper right corner as .ipynb file and start it from within your Anipose environment. If you need to install DeepLabCut first, please check [here](https://anipose.readthedocs.io/en/latest/installation.html).
# 
# This notebook will show you how to start an anipose project for 3D pose reconstruction using your trained DeepLabCut models:
# 
# * Create Anipose Project
#     * Directory Structure
#     * Config.toml file
#     * Videos
# * Update Project Specific Settings
# * Anipose Pipeline
#     * Analyze
#     * Filter
#     * Calibrate
#     * Triangulate
#     * 2D labeled videos (**optional**)
#     * 3D labeled videos (**optional**)
#     * Filter 3D poses (**optional**)
# 

# In[ ]:


# start from anipose environment
import os
import toml


# ## Create Anipose Project

# In[ ]:


# choose project name and working directory
new_project_directory = r'D:\NewAniposeProject'
new_project_name = 'PigeonTriangulation'

# get list of new sessions
sessionlist = [
    'session1',
    'session2',
    ]


# ### Create Directory Structure

# In[ ]:


# create project structure
for session in sessionlist:
    # make videos-raw folder for behavior
    videopath = os.path.join(new_project_directory, new_project_name, session, 'videos-raw')
    os.makedirs(videopath)

    # make calibration folder
    calibrationpath = os.path.join(new_project_directory, new_project_name, session, 'calibration')
    os.makedirs(calibrationpath)

# save project directory
projectpath = os.path.join(new_project_directory, new_project_name)
os.chdir(projectpath)

print(f'Done! New Anipose Project created: {os.getcwd()}')


# ### Create config.toml file

# In[ ]:


# default from anipos: https://github.com/lambdaloop/anipose/blob/master/anipose/anipose.py
DEFAULT_CONFIG = {
    'video_extension': 'avi',
    'converted_video_speed': 1,
    'calibration': {
        'animal_calibration': False,
        'calibration_init': None,
        'fisheye': False
    },
    'manual_verification': {
        'manually_verify': False
    },
    'triangulation': {
        'ransac': False,
        'optim': False,
        'scale_smooth': 2,
        'scale_length': 2,
        'scale_length_weak': 1,
        'reproj_error_threshold': 5,
        'score_threshold': 0.8,
        'n_deriv_smooth': 3,
        'constraints': [],
        'constraints_weak': []
    },
    'pipeline': {
        'videos_raw': 'videos-raw',
        'videos_raw_mp4': 'videos-raw-mp4',
        'pose_2d': 'pose-2d',
        'pose_2d_filter': 'pose-2d-filtered',
        'pose_2d_projected': 'pose-2d-proj',
        'pose_3d': 'pose-3d',
        'pose_3d_filter': 'pose-3d-filtered',
        'videos_labeled_2d': 'videos-labeled',
        'videos_labeled_2d_filter': 'videos-labeled-filtered',
        'calibration_videos': 'calibration',
        'calibration_results': 'calibration',
        'videos_labeled_3d': 'videos-3d',
        'videos_labeled_3d_filter': 'videos-3d-filtered',
        'angles': 'angles',
        'summaries': 'summaries',
        'videos_combined': 'videos-combined',
        'videos_compare': 'videos-compare',
        'videos_2d_projected': 'videos-2d-proj',
    },
    'filter': {
        'enabled': False,
        'type': 'medfilt',
        'medfilt': 13,
        'offset_threshold': 25,
        'score_threshold': 0.05,
        'spline': True,
        'n_back': 5,
        'multiprocessing': False
    },
    'filter3d': {
        'enabled': False
    }
}

# create config.toml file
configfile = os.path.join(projectpath, 'config.toml')

with open(configfile, 'w') as f:
     new_toml_string = toml.dump(DEFAULT_CONFIG, f)
print(new_toml_string)


# ### Move videos to populate project

# In[ ]:


# set directories with video data 
calibration_path = r'E:\StopSignalSkinnerbox_local\calibration'
behavior_path = r'E:\StopSignalSkinnerbox_local\concatenated'


# In[ ]:


# populate new project
copy = False # copy or move
list_of_sessions = os.listdir(projectpath)
calibration_videos = os.listdir(calibration_path)
behavior_videos = os.listdir(behavior_path)


for session in list_of_sessions:
    # check if directories are populated
    session_dirs = os.listdir(os.path.join(projectpath, session))
    
    # subset relevant videos 
    date = session[0:10] #YYYY_MM_DD_(conditions!!)_P007_camR/L.mp4 #session naming convention: 2022_04_25_P403
    id = session[11:]
    videos_to_move = []
    videos_moved = []
    session_calibration_videos = [video for video in calibration_videos if id in video if date in video]
    session_behavior_videos = [video for video in behavior_videos if id in video if date in video]

    for dir in session_dirs:
        done = os.listdir(os.path.join(projectpath, session, dir))
        
        # find videos for
        if dir == 'calibration':
            videos_to_move.extend([os.path.join(calibration_path,video) for video in session_calibration_videos if video not in done])
            videos_moved.extend([os.path.join(projectpath, session, dir, video) for video in session_calibration_videos if video not in done])        
        else:
            videos_to_move.extend([os.path.join(behavior_path, video) for video in session_behavior_videos if video not in done])
            videos_moved.extend([os.path.join(projectpath, session, dir, video) for video in session_behavior_videos if video not in done])  

    # move or copy
    print(f'Moving {len(videos_to_move)} videos for session {session}:')

    if copy:
        for video1, video2 in zip(videos_to_move, videos_moved):
            copy_command = f'copy {video1} {video2}'
            os.system(copy_command)
            print(f'{video2} coped!')
    else:
        for video1, video2 in zip(videos_to_move, videos_moved):
            os.rename(video1, video2)
            print(f'{video2} moved!')


# ## Update project Specific Settings

# In[ ]:


# make quick changes to config.toml
def change_toml(edits, configfile):
    # read config
    myconfig = toml.load(configfile)
    # change config
    for key, value in edits.items():
        myconfig[key] = value
    # dump config
    with open(configfile, 'w') as f:
        new_toml_string = toml.dump(myconfig, f)
    print(new_toml_string)

# check video extension by content
def check_videotype(projectpath, dir):
    session = os.listdir(projectpath)[0]
    path = os.path.join(projectpath, session, dir)  
    videotype = os.listdir(path)[0].split('.')[-1]
    return videotype


# In[ ]:


# edit project specific anipose configurations
edits = {
    'project': projectpath, 
    'model_folder': '',             # change path to deeplabcut project here
    'nesting': 1, 
    'video_extension': 'mp4',       # change video type here
    'pipeline': {
        'videos_raw': 'videos-raw',
        'pose_2d': 'pose-2d',
        'calibration_videos': 'calibration',
    },
    'calibration': {                # change calibration settings here
        'board_type': 'charuco', 
        'board_size': [10, 10], 
        'board_marker_bits': 4, 
        'board_marker_dict_number': 50, 
        'board_marker_length': 14, 
        'board_square_side_length': 20, 
        'animal_calibration': False, 
        'fisheye': False,
        }, 
    'manual_verification': {
        'manually_verify': False,
        },
    'labeling': {                   # change labeling settings here
        'scheme': [
            ['US(UpperSpine=LN)', 'UHS(UpperHalfSpine)', 'MS(MiddleSpine)', 'LHS(LowerHalfSpine)', 'LS(LowerSpine)', 'TC(TailCenter)', 'TR(TailRight)', 'TL(TailLeft)', 'TC(TailCenter)'], 
            ['H(Head)', 'UN(UpperNeck)', 'UHN(UpperHalfNeck)', 'MN(MiddleNeck)', 'LHN(LowerHalfNeck)', 'US(UpperSpine=LN)'], 
            ['BT(BeakTip)', 'LC(LowerCere)', 'UC(UpperCere)', 'RE(RightEye)', 'LE(LeftEye)', 'UC(UpperCere)', 'H(Head)'], 
            ['LWS(LeftWingShoulder)', 'LWE(LeftWingElbow)', 'LWW(LeftWingWriwst)', 'LWT(LeftWingTip)', 'LWS(LeftWingShoulder)', 'US(UpperSpine=LN)', 'RWS(RightWingShoulder)', 'RWE(RightWingElbow)', 'RWW(RightWingWriwst)', 'RWT(RightWingTip)', 'RWS(RightWingShoulder)'], 
            ['LWS(LeftWingShoulder)', 'LC(LeftChest)', 'LHC(LeftHalfChest)', 'MC(MiddleChest)', 'RHC(RightHalfChest)', 'RC(RightChest)', 'RWS(RightWingShoulder)', 'LWS(LeftWingShoulder)'], 
            ['BT(BeakTip)', 'C(Chin)', 'MT(MiddleThroat)', 'MC(MiddleChest)'], 
            ['RWS(RightWingShoulder)', 'RT(RightTibia)', 'RA(RightAnkle)', 'RF(RightFoot)'], 
            ['LWS(LeftWingShoulder)', 'LT(LeftTibia)', 'LA(LeftAnkle)', 'LF(LeftFoot)'], ]
            }, 
    }


# In[ ]:


# change config.toml
change_toml(edits, configfile)


# ## Anipose Pipeline

# ### 1. Analyze Videos
# 
# This may take a while. Anipose lists the videos in `videos-raw` in each session and uses the DeepLabCut project listed in the config.toml file to extract pose coordinates. This step requires a GPU.
# 
# Open a new anaconda prompt:
# ```
# conda activate anipose
# cd <projectpath>
# anipose analyze
# ```

# ### 2. Filter Predictions
# 
# Remember to change any project specific settings above before filtering the data.
# 
# ```
# conda activate anipose
# cd <projectpath>
# anipose filter
# ```

# ### 3. Calibrate
# 
# Remember to change any project specific settings above before calibrating your cameras.
# 
# ```
# conda activate anipose
# cd <projectpath>
# anipose calibrate
# ```

# ### 4. Triangulate
# 
# Remember to change any project specific settings above before triangulating your data, specifically the `constraints` for spatial optimization.
# 
# ```
# conda activate anipose
# cd <projectpath>
# anipose triangulate
# ```

# ### 5. Create 2D labeled Videos (**Optional**)
# 
# Remember to change any project specific settings above before labeling videos, specifically the `scheme`, i.e. skeleton.
# 
# ```
# conda activate anipose
# cd <projectpath>
# anipose label-2d
# ```

# ### 6. Create 3D labeled Videos (**Optional**)
# 
# Remember to change any project specific settings above before labeling videos, specifically the `scheme`, i.e. skeleton.
# 
# ```
# conda activate anipose
# cd <projectpath>
# anipose label-3d
# ```

# ### 7. Filter 3D Pose Reconstruction (**Optional**)
# 
# ```
# conda activate anipose
# cd <projectpath>
# anipose filter-3d
# ```
