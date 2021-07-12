# Real-time 2D Multi-Person Pose Estimation on CPU: Lightweight OpenPose

This repository is based on the paper [Real-time 2D Multi-Person Pose Estimation on CPU: Lightweight OpenPose](https://arxiv.org/pdf/1811.12004.pdf) and the repository [lightweight-human-pose-estimation.pytorch](https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch). This work heavily optimizes the [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) approach to reach real-time inference on CPU with negliable accuracy drop. For more information about training check the repository [lightweight-human-pose-estimation.pytorch](https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch).


<p align="center">
  <img src="video_files/tik_tok_kakashi_processed_.gif" />
</p>

## Table of Contents
(:fire: Of course the content from [lightweight-human-pose-estimation.pytorch](https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch) is availabel)
* [Requirements](#requirements)
* [Usage for video analysis](#usage-for-video-analysis)
* [Understanding of json file](#understanding-of-json-file)

## Requirements

* Ubuntu 16.04
* Python 3.6
* PyTorch 1.9.0+cu102 (should also work with 0.4.1, but not tested)
* also check the file `requirements.txt`

## Usage for video analysis

1. clone or download this repository `git clone https://github.com/GerasimovIV/open-pose-pytorch.git`
2. download the pre-trained model from [google drive](https://drive.google.com/drive/u/1/folders/1VY6HT5-lb762AdNhvuus0-Scwx8icUTx) and put it in the project folder. (for example, in the folder `project_path/checkpoints`)
3. run `pip install -r requirements.txt`
4. run `python demo.py --checkpoint-path ./checkpoints/checkpoint_iter_370000.pth --video ./video_files/tik_tok_kakashi.mp4`. 
* If you want to run only on cpu you should add `--cpu`. (Instead of `--video ./video_files/tik_tok_kakashi.mp4` you can use your custom video)
* By default the processed video and the .json file will be recorded in the same folder where the original was, however there is an opportunity to change this by setting `--filename_poses filename.json` (for .json file) and `--out_filename_video filename.mp4` (for video file)
## Understanding of .json file

.json file will contain the information about any persons and any of their limbs in any frame. 

```
list in .json file = [frame_1, frame_2, ...]
                         |
                         +---[person_1, person_2, ...]
                                 |
                                 +---pose_mass

pose_mass = [nose,
              |
              +---[x, y]
             neck,
              |
              +---[x, y]
             r_sho,
              |
              +---[x, y]
             r_elb',
              |
              +---[x, y]
             r_wri,
              |
              +---[x, y]
             l_sho,
              |
              +---[x, y]
             l_elb,
              |
              +---[x, y]
             l_wri,
              |
              +---[x, y]
             r_hip, 
              |
              +---[x, y]
             r_knee,
              |
              +---[x, y]
             r_ank,
              |
              +---[x, y]
             l_hip,
              |
              +---[x, y]
             l_knee,
              |
              +---[x, y]
             l_ank,
              |
              +---[x, y]
             r_eye, 
              |
              +---[x, y]
             l_eye,
              |
              +---[x, y]
             r_ear, 
              |
              +---[x, y]
             l_ear]            ​
```

## Speed test on GPU
This repository was tested in the [Google Colab](). That means that on the video card Tesla K80. (you can compare it with GeForce GTX 1080 Ti [here](https://technical.city/ru/video/GeForce-GTX-1080-Ti-protiv-Tesla-K80)) According to the [this source](https://technical.city/ru/video/GeForce-GTX-1080-Ti-protiv-Tesla-K80) the process on the GeForce GTX 1080 Ti will be 2 times faster then on the Tesla K80.

In the Google Colab platform I achieved the result in speed: 38.07it/s without writing .json file and 27.07it/s with writing .json file

### My suggestion for speeding up
In this repository the processing of video like that:
1. Take one frame from vide
2. Do .unsqueese(0) (creating zero dimension like bath imitation with batch_size = 1)
3. Process frame

However, due to the not very large weight of the network itself, it is possible to send a batch larger than 1 during testing, for example, send the first 64 frames from the video immediately in an ordered form. In this case, it turns out to process several frames from the video at once, which can significantly speed up the processing process.
