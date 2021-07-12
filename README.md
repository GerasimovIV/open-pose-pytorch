# Real-time 2D Multi-Person Pose Estimation on CPU: Lightweight OpenPose

This repository is based on the paper [Real-time 2D Multi-Person Pose Estimation on CPU: Lightweight OpenPose](https://arxiv.org/pdf/1811.12004.pdf) and the repository [lightweight-human-pose-estimation.pytorch](https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch). This work heavily optimizes the [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) approach to reach real-time inference on CPU with negliable accuracy drop. For more information about training check the repository [lightweight-human-pose-estimation.pytorch](https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch).


<p align="center">
  <img src="video_files/tik_tok_kakashi_processed_.gif" />
</p>

## Table of Contents
(:fire: Of course the content from [lightweight-human-pose-estimation.pytorch](https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch) is availabel)
* [Requirements](#requirements)
* [Usage for video analysis](#usage-for-video-analysis)

## Requirements

* Ubuntu 16.04
* Python 3.6
* PyTorch 1.9.0+cu102 (should also work with 0.4.1, but not tested)
* also check the file `requirements.txt`

## Usage for video analysis

1. clone or download this repository `git clone ...`
2. download the pre-trained model from [google drive](https://drive.google.com/drive/u/1/folders/1VY6HT5-lb762AdNhvuus0-Scwx8icUTx) and put it in the project folder. (for example, in the folder `project_path/checkpoints`)
3. run `pip install -r requirements.txt`
4. run `python demo.py --checkpoint-path ./checkpoints/checkpoint_iter_370000.pth --video ./video_files/tik_tok_kakashi.mp4`. If you want to run only on cpu you should add `--cpu`