# PySlowFast-CBAM

PySlowFast-CBAM is an open source video understanding codebase from FAIR that provides state-of-the-art video classification models with efficient training. This repository includes implementations of the following methods:

- [SlowFast Networks for Video Recognition](https://arxiv.org/abs/1812.03982)
- [Non-local Neural Networks](https://arxiv.org/abs/1711.07971)
- [A Multigrid Method for Efficiently Training Video Models](https://arxiv.org/abs/1912.00998)
- [X3D: Progressive Network Expansion for Efficient Video Recognition](https://arxiv.org/abs/2004.04730)
- [Multiscale Vision Transformers](https://arxiv.org/abs/2104.11227.pdf)

<div align="center">
  <img src="demo/ava_demo.gif" width="600px"/>
</div>

## Introduction

Action Recognition is a visual task of identifying different action categories from video clips. In recent decades, with the rise of deep learning technology, the recognition rate of action recognition methods based on deep learning has been greatly improved compared with traditional methods. However, the recognition effect of the above methods is still unsatisfactory when analyzing the video with multiple targets or the video with irregular shooting angles. To solve the above problems, this paper proposes an action recognition method called SlowFast-CBAM. It mainly includes two parts of innovation as follows. Firstly, the self-attention mechanism module is added to the slow path and the fast path respectively, to highlight the surrounding environment's characteristics and action. Secondly, the training dataset is pre-processed, and the separately placed action video frames are placed into the corresponding action folders. With the above improvements, this method can better focus on the feature information, ignore other information, and integrate it with the SlowFast network. Through a series of experiments, it is proved that the proposed method can better highlight the characteristics of the people who perform the actions to mark the action more accurately and increase the accuracy of action recognition.

## Authors
Yonggong Ren, Yuzhu Lin, Honglin Shao, Bo Fu, Dang N. H. Thanh 

## License

PySlowFast is released under the [Apache 2.0 license](LICENSE).

## Model Zoo and Baselines

We provide a large set of baseline results and trained models available for download in the PySlowFast [Model Zoo](MODEL_ZOO.md).

## Installation

Please find installation instructions for PyTorch and PySlowFast in [INSTALL.md](INSTALL.md). You may follow the instructions in [DATASET.md](slowfast/datasets/DATASET.md) to prepare the datasets.

## Quick Start

Follow the example in [GETTING_STARTED.md](GETTING_STARTED.md) to start playing video models with PySlowFast.

## Visualization Tools

We offer a range of visualization tools for the train/eval/test processes, model analysis, and for running inference with trained model.
More information at [Visualization Tools](VISUALIZATION_TOOLS.md).

