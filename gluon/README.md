# Computer vision models on MXNet/Gluon

[![PyPI](https://img.shields.io/pypi/v/gluoncv2.svg)](https://pypi.python.org/pypi/gluoncv2)
[![Downloads](https://pepy.tech/badge/gluoncv2)](https://pepy.tech/project/gluoncv2)

This is a collection of image classification and segmentation models. Many of them are pretrained on
[ImageNet-1K](http://www.image-net.org), [CIFAR-10/100](https://www.cs.toronto.edu/~kriz/cifar.html),
[SVHN](http://ufldl.stanford.edu/housenumbers), [CUB-200-2011](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html),
[Pascal VOC2012](http://host.robots.ox.ac.uk/pascal/VOC/voc2012), [ADE20K](http://groups.csail.mit.edu/vision/datasets/ADE20K),
[Cityscapes](https://www.cityscapes-dataset.com), and [COCO](http://cocodataset.org) datasets and loaded automatically
during use. All pretrained models require the same ordinary normalization. Scripts for training/evaluating/converting
models are in the [`imgclsmob`](https://github.com/osmr/imgclsmob) repo.

## List of implemented models

- AlexNet (['One weird trick for parallelizing convolutional neural networks'](https://arxiv.org/abs/1404.5997))
- ZFNet (['Visualizing and Understanding Convolutional Networks'](https://arxiv.org/abs/1311.2901))
- VGG/BN-VGG (['Very Deep Convolutional Networks for Large-Scale Image Recognition'](https://arxiv.org/abs/1409.1556))
- BN-Inception (['Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift'](https://arxiv.org/abs/1502.03167))
- ResNet (['Deep Residual Learning for Image Recognition'](https://arxiv.org/abs/1512.03385))
- PreResNet (['Identity Mappings in Deep Residual Networks'](https://arxiv.org/abs/1603.05027))
- ResNeXt (['Aggregated Residual Transformations for Deep Neural Networks'](http://arxiv.org/abs/1611.05431))
- SENet/SE-ResNet/SE-PreResNet/SE-ResNeXt (['Squeeze-and-Excitation Networks'](https://arxiv.org/abs/1709.01507))
- IBN-ResNet/IBN-ResNeXt/IBN-DenseNet (['Two at Once: Enhancing Learning and Generalization Capacities via IBN-Net'](https://arxiv.org/abs/1807.09441))
- AirNet/AirNeXt (['Attention Inspiring Receptive-Fields Network for Learning Invariant Representations'](https://ieeexplore.ieee.org/document/8510896))
- BAM-ResNet (['BAM: Bottleneck Attention Module'](https://arxiv.org/abs/1807.06514))
- CBAM-ResNet (['CBAM: Convolutional Block Attention Module'](https://arxiv.org/abs/1807.06521))
- ResAttNet (['Residual Attention Network for Image Classification'](https://arxiv.org/abs/1704.06904))
- SKNet (['Selective Kernel Networks'](https://arxiv.org/abs/1903.06586))
- DIA-ResNet (['DIANet: Dense-and-Implicit Attention Network'](https://arxiv.org/abs/1905.10671))
- PyramidNet (['Deep Pyramidal Residual Networks'](https://arxiv.org/abs/1610.02915))
- DiracNetV2 (['DiracNets: Training Very Deep Neural Networks Without Skip-Connections'](https://arxiv.org/abs/1706.00388))
- ShaResNet (['ShaResNet: reducing residual network parameter number by sharing weights'](https://arxiv.org/abs/1702.08782))
- CRU-Net (['Sharing Residual Units Through Collective Tensor Factorization To Improve Deep Neural Networks'](https://www.ijcai.org/proceedings/2018/88))
- DenseNet (['Densely Connected Convolutional Networks'](https://arxiv.org/abs/1608.06993))
- CondenseNet (['CondenseNet: An Efficient DenseNet using Learned Group Convolutions'](https://arxiv.org/abs/1711.09224))
- SparseNet (['Sparsely Aggregated Convolutional Networks'](https://arxiv.org/abs/1801.05895))
- PeleeNet (['Pelee: A Real-Time Object Detection System on Mobile Devices'](https://arxiv.org/abs/1804.06882))
- Oct-ResNet (['Drop an Octave: Reducing Spatial Redundancy in Convolutional Neural Networks with Octave Convolution'](https://arxiv.org/abs/1904.05049))
- Res2Net (['Res2Net: A New Multi-scale Backbone Architecture'](https://arxiv.org/abs/1904.01169))
- WRN (['Wide Residual Networks'](https://arxiv.org/abs/1605.07146))
- WRN-1bit (['Training wide residual networks for deployment using a single bit for each weight'](https://arxiv.org/abs/1802.08530))
- DRN-C/DRN-D (['Dilated Residual Networks'](https://arxiv.org/abs/1705.09914))
- DPN (['Dual Path Networks'](https://arxiv.org/abs/1707.01629))
- DarkNet Ref/Tiny/19 (['Darknet: Open source neural networks in c'](https://github.com/pjreddie/darknet))
- DarkNet-53 (['YOLOv3: An Incremental Improvement'](https://arxiv.org/abs/1804.02767))
- ChannelNet (['ChannelNets: Compact and Efficient Convolutional Neural Networks via Channel-Wise Convolutions'](https://arxiv.org/abs/1809.01330))
- iSQRT-COV-ResNet (['Towards Faster Training of Global Covariance Pooling Networks by Iterative Matrix Square Root Normalization'](https://arxiv.org/abs/1712.01034))
- i-RevNet (['i-RevNet: Deep Invertible Networks'](https://arxiv.org/abs/1802.07088))
- BagNet (['Approximating CNNs with Bag-of-local-Features models works surprisingly well on ImageNet'](https://openreview.net/pdf?id=SkfMWhAqYQ))
- DLA (['Deep Layer Aggregation'](https://arxiv.org/abs/1707.06484))
- MSDNet (['Multi-Scale Dense Networks for Resource Efficient Image Classification'](https://arxiv.org/abs/1703.09844))
- FishNet (['FishNet: A Versatile Backbone for Image, Region, and Pixel Level Prediction'](http://papers.nips.cc/paper/7356-fishnet-a-versatile-backbone-for-image-region-and-pixel-level-prediction.pdf))
- ESPNetv2 (['ESPNetv2: A Light-weight, Power Efficient, and General Purpose Convolutional Neural Network'](https://arxiv.org/abs/1811.11431))
- X-DenseNet (['Deep Expander Networks: Efficient Deep Networks from Graph Theory'](https://arxiv.org/abs/1711.08757))
- SqueezeNet/SqueezeResNet (['SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and <0.5MB model size'](https://arxiv.org/abs/1602.07360))
- SqueezeNext (['SqueezeNext: Hardware-Aware Neural Network Design'](https://arxiv.org/abs/1803.10615))
- ShuffleNet (['ShuffleNet: An Extremely Efficient Convolutional Neural Network for Mobile Devices'](https://arxiv.org/abs/1707.01083))
- ShuffleNetV2 (['ShuffleNet V2: Practical Guidelines for Efficient CNN Architecture Design'](https://arxiv.org/abs/1807.11164))
- MENet (['Merging and Evolution: Improving Convolutional Neural Networks for Mobile Applications'](https://arxiv.org/abs/1803.09127))
- MobileNet (['MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications'](https://arxiv.org/abs/1704.04861))
- FD-MobileNet (['FD-MobileNet: Improved MobileNet with A Fast Downsampling Strategy'](https://arxiv.org/abs/1802.03750))
- MobileNetV2 (['MobileNetV2: Inverted Residuals and Linear Bottlenecks'](https://arxiv.org/abs/1801.04381))
- MobileNetV3 (['Searching for MobileNetV3'](https://arxiv.org/abs/1905.02244))
- IGCV3 (['IGCV3: Interleaved Low-Rank Group Convolutions for Efficient Deep Neural Networks'](https://arxiv.org/abs/1806.00178))
- MnasNet (['MnasNet: Platform-Aware Neural Architecture Search for Mobile'](https://arxiv.org/abs/1807.11626))
- DARTS (['DARTS: Differentiable Architecture Search'](https://arxiv.org/abs/1806.09055))
- ProxylessNAS (['ProxylessNAS: Direct Neural Architecture Search on Target Task and Hardware'](https://arxiv.org/abs/1812.00332))
- FBNet (['FBNet: Hardware-Aware Efficient ConvNet Design via Differentiable Neural Architecture Search'](https://arxiv.org/abs/1812.03443))
- Xception (['Xception: Deep Learning with Depthwise Separable Convolutions'](https://arxiv.org/abs/1610.02357))
- InceptionV3 (['Rethinking the Inception Architecture for Computer Vision'](https://arxiv.org/abs/1512.00567))
- InceptionV4/InceptionResNetV2 (['Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning'](https://arxiv.org/abs/1602.07261))
- PolyNet (['PolyNet: A Pursuit of Structural Diversity in Very Deep Networks'](https://arxiv.org/abs/1611.05725))
- NASNet (['Learning Transferable Architectures for Scalable Image Recognition'](https://arxiv.org/abs/1707.07012))
- PNASNet (['Progressive Neural Architecture Search'](https://arxiv.org/abs/1712.00559))
- SPNASNet (['Single-Path NAS: Designing Hardware-Efficient ConvNets in less than 4 Hours'](https://arxiv.org/abs/1904.02877))
- EfficientNet (['EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks'](https://arxiv.org/abs/1905.11946))
- MixNet (['MixConv: Mixed Depthwise Convolutional Kernels'](https://arxiv.org/abs/1907.09595))
- NIN (['Network In Network'](https://arxiv.org/abs/1312.4400))
- RoR-3 (['Residual Networks of Residual Networks: Multilevel Residual Networks'](https://arxiv.org/abs/1608.02908))
- RiR (['Resnet in Resnet: Generalizing Residual Architectures'](https://arxiv.org/abs/1603.08029))
- ResDrop-ResNet (['Deep Networks with Stochastic Depth'](https://arxiv.org/abs/1603.09382))
- Shake-Shake-ResNet (['Shake-Shake regularization'](https://arxiv.org/abs/1705.07485))
- ShakeDrop-ResNet (['ShakeDrop Regularization for Deep Residual Learning'](https://arxiv.org/abs/1802.02375))
- FractalNet (['FractalNet: Ultra-Deep Neural Networks without Residuals'](https://arxiv.org/abs/1605.07648))
- NTS-Net (['Learning to Navigate for Fine-grained Classification'](https://arxiv.org/abs/1809.00287))
- FCN-8s (['Fully Convolutional Networks for Semantic Segmentation'](https://arxiv.org/abs/1411.4038))
- PSPNet (['Pyramid Scene Parsing Network'](https://arxiv.org/abs/1612.01105))
- DeepLabv3 (['Rethinking Atrous Convolution for Semantic Image Segmentation'](https://arxiv.org/abs/1706.05587))

## Installation

To use the models in your project, simply install the `gluoncv2` package with `mxnet`:
```
pip install gluoncv2 mxnet>=1.2.1
```
To enable different hardware supports such as GPUs, check out [MXNet variants](https://pypi.org/project/mxnet).
For example, you can install with CUDA-9.2 supported MXNet:
```
pip install gluoncv2 mxnet-cu92>=1.2.1
```

## Usage

Example of using a pretrained ResNet-18 model:
```
from gluoncv2.model_provider import get_model as glcv2_get_model
import mxnet as mx

net = glcv2_get_model("resnet18", pretrained=True)
x = mx.nd.zeros((1, 3, 224, 224), ctx=mx.cpu())
y = net(x)
```

## Pretrained models

### ImageNet-1K

Some remarks:
- Top1/Top5 are the standard 1-crop Top-1/Top-5 errors (in percents) on the validation subset of the ImageNet-1K dataset.
- FLOPs/2 is the number of FLOPs divided by two to be similar to the number of MACs.
- ResNet/PreResNet with b-suffix is a version of the networks with the stride in the second convolution of the
bottleneck block. Respectively a network without b-suffix has the stride in the first convolution.
- ResNet/PreResNet models do not use biases in convolutions at all.
- CondenseNet models are only so-called converted versions.
- ShuffleNetV2 and ShuffleNetV2b are different implementations of the same architecture.
- ResNet(D) is a dilated ResNet intended for use as an feature extractor in some segmentation networks.

| Model | Top1 | Top5 | Params | FLOPs/2 | Remarks |
| --- | ---: | ---: | ---: | ---: | --- |
| AlexNet | 40.46 | 17.70 | 62,378,344 | 1,132.33M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.394/alexnet-1770-3883d21e.params.log)) |
| AlexNet-b | 41.08 | 18.53 | 61,100,840 | 714.83M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.384/alexnetb-1853-9762fd33.params.log)) |
| ZFNet | 39.21 | 16.78 | 62,357,608 | 1,170.33M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.395/zfnet-1678-3299fdce.params.log)) |
| ZFNet-b | 35.81 | 14.59 | 107,627,624 | 2,479.13M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.400/zfnetb-1459-7a654810.params.log)) |
| VGG-11 | 29.59 | 10.16 | 132,863,336 | 7,615.87M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.381/vgg11-1016-3d78e0ec.params.log)) |
| VGG-13 | 28.37 | 9.50 | 133,047,848 | 11,317.65M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.388/vgg13-0950-d2bcaaf3.params.log)) |
| VGG-16 | 26.61 | 8.32 | 138,357,544 | 15,480.10M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.401/vgg16-0832-22fe503a.params.log)) |
| VGG-19 | 25.88 | 8.23 | 143,667,240 | 19,642.55M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.109/vgg19-0823-0e2a1e0a.params.log)) |
| BN-VGG-11 | 28.56 | 9.34 | 132,866,088 | 7,630.21M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.339/bn_vgg11-0934-3f79cab1.params.log)) |
| BN-VGG-13 | 27.68 | 8.87 | 133,050,792 | 11,341.62M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.353/bn_vgg13-0887-540243b0.params.log)) |
| BN-VGG-16 | 25.50 | 7.57 | 138,361,768 | 15,506.38M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.359/bn_vgg16-0757-90441925.params.log)) |
| BN-VGG-19 | 23.91 | 6.89 | 143,672,744 | 19,671.15M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.360/bn_vgg19-0689-cd8f4229.params.log)) |
| BN-VGG-11b | 29.24 | 9.75 | 132,868,840 | 7,630.72M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.407/bn_vgg11b-0975-685ae89d.params.log)) |
| BN-VGG-13b | 29.48 | 10.16 | 133,053,736 | 11,342.14M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.110/bn_vgg13b-1016-f384ff52.params.log)) |
| BN-VGG-16b | 26.89 | 8.65 | 138,365,992 | 15,507.20M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.110/bn_vgg16b-0865-b5e33db8.params.log)) |
| BN-VGG-19b | 25.66 | 8.15 | 143,678,248 | 19,672.26M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.110/bn_vgg19b-0815-3a0e43e6.params.log)) |
| BN-Inception | 25.12 | 7.54 | 11,295,240 | 2,048.06M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.405/bninception-0754-75225419.params.log)) |
| ResNet-10 | 34.61 | 13.85 | 5,418,792 | 894.04M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.248/resnet10-1385-a9964274.params.log)) |
| ResNet-12 | 33.42 | 13.03 | 5,492,776 | 1,126.25M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.253/resnet12-1303-8f492c28.params.log)) |
| ResNet-14 | 32.18 | 12.20 | 5,788,200 | 1,357.94M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.256/resnet14-1220-fcdddcef.params.log)) |
| ResNet-BC-14b | 30.26 | 11.16 | 10,064,936 | 1,479.12M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.309/resnetbc14b-1116-c4ffed61.params.log)) |
| ResNet-16 | 30.24 | 10.88 | 6,968,872 | 1,589.34M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.259/resnet16-1088-2bc07547.params.log)) |
| ResNet-18 x0.25 | 39.31 | 17.40 | 3,937,400 | 270.94M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.262/resnet18_wd4-1740-a74ea15d.params.log)) |
| ResNet-18 x0.5 | 33.41 | 12.84 | 5,804,296 | 608.70M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.263/resnet18_wd2-1284-9a515406.params.log)) |
| ResNet-18 x0.75 | 30.00 | 10.66 | 8,476,056 | 1,129.45M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.266/resnet18_w3d4-1066-1a574a41.params.log)) |
| ResNet-18 | 28.09 | 9.51 | 11,689,512 | 1,820.41M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.153/resnet18-0951-98a2545b.params.log)) |
| ResNet-26 | 26.14 | 8.37 | 17,960,232 | 2,746.79M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.305/resnet26-0837-d81d836f.params.log)) |
| ResNet-BC-26b | 24.86 | 7.58 | 15,995,176 | 2,356.67M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.313/resnetbc26b-0758-2b5e8d08.params.log)) |
| ResNet-34 | 24.53 | 7.43 | 21,797,672 | 3,672.68M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.291/resnet34-0743-5cdeeccd.params.log)) |
| ResNet-BC-38b | 23.50 | 6.72 | 21,925,416 | 3,234.21M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.328/resnetbc38b-0672-82094464.params.log)) |
| ResNet-50 | 22.15 | 6.04 | 25,557,032 | 3,877.95M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.329/resnet50-0604-a71d1d2a.params.log)) |
| ResNet-50b | 22.06 | 6.11 | 25,557,032 | 4,110.48M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.308/resnet50b-0611-ca12f8d8.params.log)) |
| ResNet-101 | 21.66 | 5.99 | 44,549,160 | 7,597.95M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.1/resnet101-0599-a6d3a5f4.params.log)) |
| ResNet-101b | 20.26 | 5.12 | 44,549,160 | 7,830.48M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.357/resnet101b-0512-af5c4233.params.log)) |
| ResNet-152 | 20.76 | 5.35 | 60,192,808 | 11,321.85M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.144/resnet152-0535-bbdd7ed1.params.log)) |
| ResNet-152b | 19.63 | 4.80 | 60,192,808 | 11,554.38M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.378/resnet152b-0480-7277968c.params.log)) |
| PreResNet-10 | 34.65 | 14.01 | 5,417,128 | 894.19M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.249/preresnet10-1401-2b96c081.params.log)) |
| PreResNet-12 | 33.57 | 13.21 | 5,491,112 | 1,126.40M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.257/preresnet12-1321-b628efb5.params.log)) |
| PreResNet-14 | 32.29 | 12.18 | 5,786,536 | 1,358.09M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.260/preresnet14-1218-d65fa628.params.log)) |
| PreResNet-BC-14b | 30.67 | 11.51 | 10,057,384 | 1,476.62M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.315/preresnetbc14b-1151-c712a235.params.log)) |
| PreResNet-16 | 30.21 | 10.81 | 6,967,208 | 1,589.49M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.261/preresnet16-1081-5b00b55f.params.log)) |
| PreResNet-18 x0.25 | 39.62 | 17.78 | 3,935,960 | 270.93M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.272/preresnet18_wd4-1778-3d949d1a.params.log)) |
| PreResNet-18 x0.5 | 33.67 | 13.19 | 5,802,440 | 608.73M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.273/preresnet18_wd2-1319-63e55c24.params.log)) |
| PreResNet-18 x0.75 | 29.96 | 10.68 | 8,473,784 | 1,129.51M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.274/preresnet18_w3d4-1068-eb569861.params.log)) |
| PreResNet-18 | 28.16 | 9.51 | 11,687,848 | 1,820.56M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.140/preresnet18-0951-71279a0b.params.log)) |
| PreResNet-26 | 26.03 | 8.34 | 17,958,568 | 2,746.94M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.316/preresnet26-0834-c2ecba09.params.log)) |
| PreResNet-BC-26b | 25.21 | 7.86 | 15,987,624 | 2,354.16M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.325/preresnetbc26b-0786-265f591f.params.log)) |
| PreResNet-34 | 24.55 | 7.51 | 21,796,008 | 3,672.83M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.300/preresnet34-0751-ba9c829e.params.log)) |
| PreResNet-BC-38b | 22.67 | 6.33 | 21,917,864 | 3,231.70M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.348/preresnetbc38b-0633-809d2def.params.log)) |
| PreResNet-50 | 22.27 | 6.20 | 25,549,480 | 3,875.44M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.330/preresnet50-0620-50f13b2d.params.log)) |
| PreResNet-50b | 22.36 | 6.32 | 25,549,480 | 4,107.97M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.307/preresnet50b-0632-951de2dc.params.log)) |
| PreResNet-101 | 21.45 | 5.75 | 44,541,608 | 7,595.44M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.2/preresnet101-0575-e2887e53.params.log)) |
| PreResNet-101b | 20.85 | 5.40 | 44,541,608 | 7,827.97M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.351/preresnet101b-0540-3839a473.params.log)) |
| PreResNet-152 | 20.70 | 5.32 | 60,185,256 | 11,319.34M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.14/preresnet152-0532-31505f71.params.log)) |
| PreResNet-152b | 19.90 | 5.00 | 60,185,256 | 11,551.87M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.386/preresnet152b-0500-6929c862.params.log)) |
| PreResNet-200b | 21.10 | 5.64 | 64,666,280 | 15,068.63M | From [tornadomeet/ResNet] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.45/preresnet200b-0564-38f849a6.params.log)) |
| PreResNet-269b | 20.71 | 5.56 | 102,065,832 | 20,101.11M | From [soeaver/mxnet-model] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.239/preresnet269b-0556-f386e3e7.params.log)) |
| ResNeXt-14 (16x4d) | 31.66 | 12.23 | 7,127,336 | 1,045.77M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.370/resnext14_16x4d-1223-1f8072e8.params.log)) |
| ResNeXt-14 (32x2d) | 32.16 | 12.47 | 7,029,416 | 1,031.32M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.371/resnext14_32x2d-1247-2ca8cc25.params.log)) |
| ResNeXt-14 (32x4d) | 29.95 | 11.10 | 9,411,880 | 1,603.46M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.327/resnext14_32x4d-1110-9be6190e.params.log)) |
| ResNeXt-26 (32x2d) | 26.34 | 8.50 | 9,924,136 | 1,461.06M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.373/resnext26_32x2d-0850-a1fb4451.params.log)) |
| ResNeXt-26 (32x4d) | 23.93 | 7.21 | 15,389,480 | 2,488.07M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.332/resnext26_32x4d-0721-5264d7ef.params.log)) |
| ResNeXt-101 (32x4d) | 21.32 | 5.79 | 44,177,704 | 8,003.45M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.10/resnext101_32x4d-0579-9afbfdbc.params.log)) |
| ResNeXt-101 (64x4d) | 20.60 | 5.41 | 83,455,272 | 15,500.27M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.10/resnext101_64x4d-0541-0d4fd87b.params.log)) |
| SE-ResNet-10 | 33.55 | 13.29 | 5,463,332 | 894.08M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.354/seresnet10-1329-af28e6d0.params.log)) |
| SE-ResNet-18 | 27.95 | 9.20 | 11,778,592 | 1,820.51M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.355/seresnet18-0920-85a6b1da.params.log)) |
| SE-ResNet-26 | 25.42 | 8.03 | 18,093,852 | 2,746.93M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.363/seresnet26-0803-9f900419.params.log)) |
| SE-ResNet-BC-26b | 23.44 | 6.82 | 17,395,976 | 2,358.07M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.366/seresnetbc26b-0682-15ae6e19.params.log)) |
| SE-ResNet-BC-38b | 21.44 | 5.75 | 24,026,616 | 3,236.32M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.374/seresnetbc38b-0575-f80f0c3c.params.log)) |
| SE-ResNet-50 | 22.51 | 6.44 | 28,088,024 | 3,880.49M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.11/seresnet50-0644-10954a84.params.log)) |
| SE-ResNet-50b | 20.58 | 5.33 | 28,088,024 | 4,113.02M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.387/seresnet50b-0533-0d8f0d23.params.log)) |
| SE-ResNet-101 | 21.92 | 5.89 | 49,326,872 | 7,602.76M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.11/seresnet101-0589-4c10238d.params.log)) |
| SE-ResNet-152 | 21.48 | 5.77 | 66,821,848 | 11,328.52M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.11/seresnet152-0577-de6f099d.params.log)) |
| SE-PreResNet-10 | 33.60 | 13.06 | 5,461,668 | 894.23M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.377/sepreresnet10-1306-cbdd1053.params.log)) |
| SE-PreResNet-18 | 27.67 | 9.38 | 11,776,928 | 1,820.66M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.380/sepreresnet18-0938-f9645ed3.params.log)) |
| SE-PreResNet-BC-26b | 22.95 | 6.36 | 17,388,424 | 2,355.57M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.399/sepreresnetbc26b-0636-33c94c9d.params.log)) |
| SE-PreResNet-BC-38b | 21.42 | 5.63 | 24,019,064 | 3,233.81M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.409/sepreresnetbc38b-0563-d8f0fbd3.params.log)) |
| SE-ResNeXt-50 (32x4d) | 21.06 | 5.58 | 27,559,896 | 4,258.40M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.12/seresnext50_32x4d-0558-a49f8fb0.params.log)) |
| SE-ResNeXt-101 (32x4d) | 19.99 | 5.00 | 48,955,416 | 8,008.26M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.12/seresnext101_32x4d-0500-cf161260.params.log)) |
| SENet-16 | 25.34 | 8.06 | 31,366,168 | 5,080.55M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.341/senet16-0806-ba268021.params.log)) |
| SENet-28 | 21.68 | 5.91 | 36,453,768 | 5,731.20M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.356/senet28-0591-d5297a35.params.log)) |
| SENet-154 | 18.84 | 4.65 | 115,088,984 | 20,745.78M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.13/senet154-0465-dd244507.params.log)) |
| IBN-ResNet-50 | 23.56 | 6.68 | 25,557,032 | 4,110.48M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibn_resnet50-0668-db527596.params.log)) |
| IBN-ResNet-101 | 21.89 | 5.87 | 44,549,160 | 7,830.48M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibn_resnet101-0587-946e7f10.params.log)) |
| IBN(b)-ResNet-50 | 23.91 | 6.97 | 25,558,568 | 4,112.89M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibnb_resnet50-0697-0aea51d2.params.log)) |
| IBN-ResNeXt-101 (32x4d) | 21.43 | 5.62 | 44,177,704 | 8,003.45M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibn_resnext101_32x4d-0562-05ddba79.params.log)) |
| IBN-DenseNet-121 | 24.98 | 7.47 | 7,978,856 | 2,872.13M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibn_densenet121-0747-1434d379.params.log)) |
| IBN-DenseNet-169 | 23.78 | 6.82 | 14,149,480 | 3,403.89M | From [XingangPan/IBN-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.127/ibn_densenet169-0682-6d7c48c5.params.log)) |
| AirNet50-1x64d (r=2) | 22.48 | 6.21 | 27,425,864 | 4,772.11M | From [soeaver/AirNet-PyTorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.120/airnet50_1x64d_r2-0621-347358cc.params.log)) |
| AirNet50-1x64d (r=16) | 22.91 | 6.46 | 25,714,952 | 4,399.97M | From [soeaver/AirNet-PyTorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.120/airnet50_1x64d_r16-0646-0b847b99.params.log)) |
| AirNeXt50-32x4d (r=2) | 21.51 | 5.75 | 27,604,296 | 5,339.58M | From [soeaver/AirNet-PyTorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.120/airnext50_32x4d_r2-0575-ab104fb5.params.log)) |
| BAM-ResNet-50 | 23.68 | 6.96 | 25,915,099 | 4,196.09M | From [Jongchan/attention-module] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.124/bam_resnet50-0696-7e573b61.params.log)) |
| CBAM-ResNet-50 | 23.02 | 6.38 | 28,089,624 | 4,116.97M | From [Jongchan/attention-module] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.125/cbam_resnet50-0638-78be5665.params.log)) |
| PyramidNet-101 (a=360) | 22.72 | 6.52 | 42,455,070 | 8,743.54M | From [dyhan0920/Pyramid...PyTorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.104/pyramidnet101_a360-0652-08d5a5d1.params.log)) |
| DiracNetV2-18 | 30.61 | 11.17 | 11,511,784 | 1,796.62M | From [szagoruyko/diracnets] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.111/diracnet18v2-1117-27601f6f.params.log)) |
| DiracNetV2-34 | 27.93 | 9.46 | 21,616,232 | 3,646.93M | From [szagoruyko/diracnets] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.111/diracnet34v2-0946-1faa6f12.params.log)) |
| CRU-Net-56 | 25.72 | 8.25 | 25,609,384 | 5,660.66M | From [cypw/CRU-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.197/crunet56-0825-ad16523b.params.log)) |
| DenseNet-121 | 23.25 | 6.85 | 7,978,856 | 2,872.13M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.314/densenet121-0685-d3a1fae8.params.log)) |
| DenseNet-161 | 22.40 | 6.18 | 28,681,000 | 7,793.16M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.3/densenet161-0618-52e30516.params.log)) |
| DenseNet-169 | 22.10 | 6.05 | 14,149,480 | 3,403.89M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.406/densenet169-0605-9c045c86.params.log)) |
| DenseNet-201 | 22.71 | 6.36 | 20,013,928 | 4,347.15M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.3/densenet201-0636-65b5d389.params.log)) |
| CondenseNet-74 (C=G=4) | 26.82 | 8.64 | 4,773,944 | 546.06M | From [ShichenLiu/CondenseNet] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.4/condensenet74_c4_g4-0864-cde68fa2.params.log)) |
| CondenseNet-74 (C=G=8) | 29.76 | 10.49 | 2,935,416 | 291.52M | From [ShichenLiu/CondenseNet] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.4/condensenet74_c8_g8-1049-4cf4a08e.params.log)) |
| PeleeNet | 31.71 | 11.25 | 2,802,248 | 514.87M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.141/peleenet-1125-38d4fb24.params.log)) |
| WRN-50-2 | 22.15 | 6.12 | 68,849,128 | 11,405.42M | From [szagoruyko/functional-zoo] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.113/wrn50_2-0612-f8013e68.params.log)) |
| DRN-C-26 | 25.68 | 7.89 | 21,126,584 | 16,993.90M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnc26-0789-ee56ffab.params.log)) |
| DRN-C-42 | 23.80 | 6.92 | 31,234,744 | 25,093.75M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnc42-0692-f89c26d6.params.log)) |
| DRN-C-58 | 22.35 | 6.27 | 40,542,008 | 32,489.94M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnc58-0627-44cbf15c.params.log)) |
| DRN-D-22 | 26.67 | 8.52 | 16,393,752 | 13,051.33M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnd22-0852-08574752.params.log)) |
| DRN-D-38 | 24.51 | 7.36 | 26,501,912 | 21,151.19M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnd38-0736-c7d53bc0.params.log)) |
| DRN-D-54 | 22.05 | 6.27 | 35,809,176 | 28,547.38M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnd54-0627-87d44c87.params.log)) |
| DRN-D-105 | 21.31 | 5.81 | 54,801,304 | 43,442.43M | From [fyu/drn] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.116/drnd105-0581-ab12d662.params.log)) |
| DPN-68 | 22.87 | 6.58 | 12,611,602 | 2,351.84M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.310/dpn68-0658-07251919.params.log)) |
| DPN-98 | 20.23 | 5.28 | 61,570,728 | 11,716.51M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.17/dpn98-0528-fa5d6fca.params.log)) |
| DPN-131 | 20.03 | 5.22 | 79,254,504 | 16,076.15M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.17/dpn131-0522-35ac2f82.params.log)) |
| DarkNet Tiny | 40.31 | 17.46 | 1,042,104 | 500.85M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.69/darknet_tiny-1746-16501793.params.log)) |
| DarkNet Ref | 38.00 | 16.68 | 7,319,416 | 367.59M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.64/darknet_ref-1668-3011b4e1.params.log)) |
| DarkNet-53 | 21.44 | 5.56 | 41,609,928 | 7,133.86M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.150/darknet53-0556-e9486353.params.log)) |
| i-RevNet-301 | 26.97 | 8.97 | 125,120,356 | 14,453.87M | From [jhjacobsen/pytorch-i-revnet] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.251/irevnet301-0897-cef9b5bf.params.log)) |
| BagNet-9 | 59.57 | 35.44 | 15,688,744 | 16,049.19M | From [wielandbrendel/bag...models] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.255/bagnet9-3544-ea1ae645.params.log)) |
| BagNet-17 | 44.76 | 21.52 | 16,213,032 | 15,768.77M | From [wielandbrendel/bag...models] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.255/bagnet17-2152-4b3a6212.params.log)) |
| BagNet-33 | 36.43 | 14.95 | 18,310,184 | 16,371.52M | From [wielandbrendel/bag...models] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.255/bagnet33-1495-87527d82.params.log)) |
| DLA-34 | 26.14 | 8.21 | 15,742,104 | 3,071.37M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla34-0821-1127fa0a.params.log)) |
| DLA-46-C | 33.84 | 12.86 | 1,301,400 | 585.45M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.182/dla46c-1286-5b38b67f.params.log)) |
| DLA-X-46-C | 32.96 | 12.25 | 1,068,440 | 546.72M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.293/dla46xc-1225-e570f5f0.params.log)) |
| DLA-60 | 23.84 | 7.08 | 22,036,632 | 4,255.49M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla60-0708-954571d6.params.log)) |
| DLA-X-60 | 22.48 | 6.21 | 17,352,344 | 3,543.68M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla60x-0621-35774214.params.log)) |
| DLA-X-60-C | 30.67 | 10.74 | 1,319,832 | 596.06M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.289/dla60xc-1074-1b4e4048.params.log)) |
| DLA-102 | 22.87 | 6.44 | 33,268,888 | 7,190.95M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla102-0644-cadbb1cc.params.log)) |
| DLA-X-102 | 21.97 | 6.02 | 26,309,272 | 5,884.94M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla102x-0602-193568a7.params.log)) |
| DLA-X2-102 | 21.12 | 5.53 | 41,282,200 | 9,340.61M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla102x2-0553-30c8f409.params.log)) |
| DLA-169 | 21.95 | 5.87 | 53,389,720 | 11,593.20M | From [ucbdrive/dla] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.202/dla169-0587-4f3e6a6e.params.log)) |
| FishNet-150 | 22.85 | 6.38 | 24,959,400 | 6,435.02M | From [kevin-ssy/FishNet] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.168/fishnet150-0638-5cbd08ec.params.log)) |
| ESPNetv2 x0.5 | 43.61 | 21.07 | 1,241,332 | 35.36M | From [sacmehta/ESPNetv2] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.238/espnetv2_wd2-2107-f2e17f0a.params.log)) |
| ESPNetv2 x1.0 | 35.33 | 14.27 | 1,670,072 | 98.09M | From [sacmehta/ESPNetv2] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.238/espnetv2_w1-1427-538f31fb.params.log)) |
| ESPNetv2 x1.25 | 33.14 | 12.73 | 1,965,440 | 138.18M | From [sacmehta/ESPNetv2] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.238/espnetv2_w5d4-1273-b119ad9e.params.log)) |
| ESPNetv2 x1.5 | 32.04 | 11.94 | 2,314,856 | 185.77M | From [sacmehta/ESPNetv2] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.238/espnetv2_w3d2-1194-3804a850.params.log)) |
| ESPNetv2 x2.0 | 28.91 | 9.94 | 3,498,136 | 306.93M | From [sacmehta/ESPNetv2] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.238/espnetv2_w2-0994-c212d81a.params.log)) |
| SqueezeNet v1.0 | 38.73 | 17.34 | 1,248,424 | 823.67M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.128/squeezenet_v1_0-1734-e6f8b0e8.params.log)) |
| SqueezeNet v1.1 | 39.09 | 17.39 | 1,235,496 | 352.02M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.88/squeezenet_v1_1-1739-d7a1483a.params.log)) |
| SqueezeResNet v1.0 | 39.32 | 17.67 | 1,248,424 | 823.67M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.178/squeezeresnet_v1_0-1767-66474b9b.params.log)) |
| SqueezeResNet v1.1 | 39.83 | 17.84 | 1,235,496 | 352.02M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.70/squeezeresnet_v1_1-1784-26064b82.params.log)) |
| 1.0-SqNxt-23 | 42.25 | 18.66 | 724,056 | 287.28M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.171/sqnxt23_w1-1866-73b700c4.params.log)) |
| 1.0-SqNxt-23v5 | 40.43 | 17.43 | 921,816 | 285.82M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.172/sqnxt23v5_w1-1743-7a83722e.params.log)) |
| 1.5-SqNxt-23 | 34.46 | 13.21 | 1,511,824 | 552.39M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.210/sqnxt23_w3d2-1321-4d733bcd.params.log)) |
| 1.5-SqNxt-23v5 | 33.48 | 12.68 | 1,953,616 | 550.97M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.212/sqnxt23v5_w3d2-1268-4f98bbd3.params.log)) |
| 2.0-SqNxt-23 | 30.24 | 10.63 | 2,583,752 | 898.48M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.240/sqnxt23_w2-1063-95d9b55a.params.log)) |
| 2.0-SqNxt-23v5 | 29.27 | 10.24 | 3,366,344 | 897.60M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.216/sqnxt23v5_w2-1024-707246f3.params.log)) |
| ShuffleNet x0.25 (g=1) | 62.00 | 36.77 | 209,746 | 12.35M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.134/shufflenet_g1_wd4-3677-ee58f368.params.log)) |
| ShuffleNet x0.25 (g=3) | 61.34 | 36.17 | 305,902 | 13.09M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.135/shufflenet_g3_wd4-3617-bd08e3ed.params.log)) |
| ShuffleNet x0.5 (g=1) | 46.22 | 22.38 | 534,484 | 41.16M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.174/shufflenet_g1_wd2-2238-f77dcd18.params.log)) |
| ShuffleNet x0.5 (g=3) | 43.83 | 20.60 | 718,324 | 41.70M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.167/shufflenet_g3_wd2-2060-ea6737a5.params.log)) |
| ShuffleNet x0.75 (g=1) | 39.25 | 16.75 | 975,214 | 86.42M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.218/shufflenet_g1_w3d4-1675-2f1530aa.params.log)) |
| ShuffleNet x0.75 (g=3) | 37.81 | 16.09 | 1,238,266 | 85.82M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.219/shufflenet_g3_w3d4-1609-e008e926.params.log)) |
| ShuffleNet x1.0 (g=1) | 34.41 | 13.50 | 1,531,936 | 148.13M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.223/shufflenet_g1_w1-1350-01934ee8.params.log)) |
| ShuffleNet x1.0 (g=2) | 33.98 | 13.32 | 1,733,848 | 147.60M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.241/shufflenet_g2_w1-1332-f5a1479f.params.log)) |
| ShuffleNet x1.0 (g=3) | 33.96 | 13.29 | 1,865,728 | 145.46M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.244/shufflenet_g3_w1-1329-ac58d62c.params.log)) |
| ShuffleNet x1.0 (g=4) | 33.84 | 13.10 | 1,968,344 | 143.33M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.245/shufflenet_g4_w1-1310-73c039eb.params.log)) |
| ShuffleNet x1.0 (g=8) | 33.65 | 13.19 | 2,434,768 | 150.76M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.250/shufflenet_g8_w1-1319-9a50ddd9.params.log)) |
| ShuffleNetV2 x0.5 | 40.61 | 18.30 | 1,366,792 | 43.31M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.90/shufflenetv2_wd2-1830-156953de.params.log)) |
| ShuffleNetV2 x1.0 | 30.94 | 11.23 | 2,278,604 | 149.72M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.133/shufflenetv2_w1-1123-27435039.params.log)) |
| ShuffleNetV2 x1.5 | 27.17 | 9.13 | 4,406,098 | 320.77M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.288/shufflenetv2_w3d2-0913-f132506c.params.log)) |
| ShuffleNetV2 x2.0 | 25.80 | 8.23 | 7,601,686 | 595.84M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.301/shufflenetv2_w2-0823-2d67ac62.params.log)) |
| ShuffleNetV2b x0.5 | 39.81 | 17.82 | 1,366,792 | 43.31M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.157/shufflenetv2b_wd2-1782-845a9c43.params.log)) |
| ShuffleNetV2b x1.0 | 30.39 | 11.01 | 2,279,760 | 150.62M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.161/shufflenetv2b_w1-1101-f679702f.params.log)) |
| ShuffleNetV2b x1.5 | 26.90 | 8.79 | 4,410,194 | 323.98M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.203/shufflenetv2b_w3d2-0879-4022da3a.params.log)) |
| ShuffleNetV2b x2.0 | 25.20 | 8.10 | 7,611,290 | 603.37M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.242/shufflenetv2b_w2-0810-7429df75.params.log)) |
| 108-MENet-8x1 (g=3) | 43.62 | 20.30 | 654,516 | 42.68M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.89/menet108_8x1_g3-2030-aa07f925.params.log)) |
| 128-MENet-8x1 (g=4) | 42.10 | 19.13 | 750,796 | 45.98M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.103/menet128_8x1_g4-1913-0c890a76.params.log)) |
| 128-MENet-8x1 (g=4) | 42.10 | 19.13 | 750,796 | 45.98M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.103/menet128_8x1_g4-1913-0c890a76.params.log)) |
| 160-MENet-8x1 (g=8) | 43.47 | 20.28 | 850,120 | 45.63M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.154/menet160_8x1_g8-2028-4f28279a.params.log)) |
| 256-MENet-12x1 (g=4) | 32.23 | 12.16 | 1,888,240 | 150.65M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.152/menet256_12x1_g4-1216-7caf63d1.params.log)) |
| 348-MENet-12x1 (g=3) | 27.85 | 9.36 | 3,368,128 | 312.00M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.173/menet348_12x1_g3-0936-62c72b0b.params.log)) |
| 352-MENet-12x1 (g=8) | 31.30 | 11.67 | 2,272,872 | 157.35M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.198/menet352_12x1_g8-1167-5892fea4.params.log)) |
| 456-MENet-24x1 (g=3) | 25.02 | 7.80 | 5,304,784 | 567.90M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.237/menet456_24x1_g3-0780-7a89b32c.params.log)) |
| MobileNet x0.25 | 45.78 | 22.18 | 470,072 | 44.09M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.62/mobilenet_wd4-2218-3185cdd2.params.log)) |
| MobileNet x0.5 | 33.94 | 13.30 | 1,331,592 | 155.42M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.156/mobilenet_wd2-1330-94f13ae1.params.log)) |
| MobileNet x0.75 | 29.85 | 10.51 | 2,585,560 | 333.99M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.130/mobilenet_w3d4-1051-6361d4b4.params.log)) |
| MobileNet x1.0 | 26.43 | 8.65 | 4,231,976 | 579.80M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.155/mobilenet_w1-0865-eafd91e9.params.log)) |
| FD-MobileNet x0.25 | 55.44 | 30.53 | 383,160 | 12.95M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.177/fdmobilenet_wd4-3053-d4f18e5b.params.log)) |
| FD-MobileNet x0.5 | 42.62 | 19.69 | 993,928 | 41.84M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.83/fdmobilenet_wd2-1969-242b9fa8.params.log)) |
| FD-MobileNet x0.75 | 37.91 | 16.01 | 1,833,304 | 86.68M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.159/fdmobilenet_w3d4-1601-cb10c3e1.params.log)) |
| FD-MobileNet x1.0 | 33.80 | 13.12 | 2,901,288 | 147.46M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.162/fdmobilenet_w1-1312-95fa0092.params.log)) |
| MobileNetV2 x0.25 | 48.08 | 24.12 | 1,516,392 | 34.24M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.137/mobilenetv2_wd4-2412-d92b5b2d.params.log)) |
| MobileNetV2 x0.5 | 35.63 | 14.42 | 1,964,736 | 100.13M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.170/mobilenetv2_wd2-1442-d7c586c7.params.log)) |
| MobileNetV2 x0.75 | 29.78 | 10.44 | 2,627,592 | 198.50M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.230/mobilenetv2_w3d4-1044-768454f4.params.log)) |
| MobileNetV2 x1.0 | 26.77 | 8.64 | 3,504,960 | 329.36M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.213/mobilenetv2_w1-0864-6e58b1cb.params.log)) |
| MobileNetV3 L/224/1.0 | 24.63 | 7.69 | 5,481,752 | 226.80M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.411/mobilenetv3_large_w1-0769-7f4b9203.params.log)) |
| IGCV3 x0.25 | 53.43 | 28.30 | 1,534,020 | 41.29M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.142/igcv3_wd4-2830-71abf6e0.params.log)) |
| IGCV3 x0.5 | 39.41 | 17.03 | 1,985,528 | 111.12M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.132/igcv3_wd2-1703-145b7089.params.log)) |
| IGCV3 x0.75 | 30.71 | 10.96 | 2,638,084 | 210.95M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.207/igcv3_w3d4-1096-3c7c86fc.params.log)) |
| IGCV3 x1.0 | 27.73 | 9.00 | 3,491,688 | 340.79M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.243/igcv3_w1-0900-e2c3da1c.params.log)) |
| MnasNet | 31.32 | 11.44 | 4,308,816 | 317.67M | From [zeusees/Mnasnet...Model] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.117/mnasnet-1144-c972fec0.params.log)) |
| DARTS | 27.23 | 8.97 | 4,718,752 | 539.86M | From [quark0/darts] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.118/darts-0897-aafd6452.params.log)) |
| ProxylessNAS CPU | 24.78 | 7.50 | 4,361,648 | 459.96M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.324/proxylessnas_cpu-0750-256da7c8.params.log)) |
| ProxylessNAS GPU | 24.67 | 7.24 | 7,119,848 | 476.08M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.333/proxylessnas_gpu-0724-d9ce8096.params.log)) |
| ProxylessNAS Mobile | 25.31 | 7.80 | 4,080,512 | 332.46M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.326/proxylessnas_mobile-0780-b8bb5a64.params.log)) |
| ProxylessNAS Mob-14 | 22.96 | 6.51 | 6,857,568 | 597.10M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.331/proxylessnas_mobile14-0651-f08baec8.params.log)) |
| FBNet-Cb | 25.47 | 7.86 | 5,572,200 | 399.26M | From [rwightman/pyt...models] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.415/fbnet_cb-0786-5e8f8775.params.log)) |
| Xception | 20.99 | 5.56 | 22,855,952 | 8,403.63M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.115/xception-0556-bd2c1684.params.log)) |
| InceptionV3 | 21.22 | 5.59 | 23,834,568 | 5,743.06M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.92/inceptionv3-0559-6c087967.params.log)) |
| InceptionV4 | 20.60 | 5.25 | 42,679,816 | 12,304.93M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.105/inceptionv4-0525-f7aa9536.params.log)) |
| InceptionResNetV2 | 19.96 | 4.94 | 55,843,464 | 13,188.64M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.107/inceptionresnetv2-0494-3328f7fa.params.log)) |
| PolyNet | 19.09 | 4.53 | 95,366,600 | 34,821.34M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.96/polynet-0453-74280314.params.log)) |
| NASNet-A 4@1056 | 25.37 | 7.95 | 5,289,978 | 584.90M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.97/nasnet_4a1056-0795-5c78908e.params.log)) |
| NASNet-A 6@4032 | 18.17 | 4.24 | 88,753,150 | 23,976.44M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.101/nasnet_6a4032-0424-73cca5fe.params.log)) |
| PNASNet-5-Large | 17.90 | 4.28 | 86,057,668 | 25,140.77M | From [Cadene/pretrained...pytorch] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.114/pnasnet5large-0428-998a548f.params.log)) |
| SPNASNet | 26.92 | 8.67 | 4,421,616 | 346.73M | From [rwightman/pyt...models] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.416/spnasnet-0867-a223136f.params.log)) |
| EfficientNet-B0 | 24.50 | 7.22 | 5,288,548 | 413.13M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.364/efficientnet_b0-0722-041a8346.params.log)) |
| EfficientNet-B1 | 22.89 | 6.26 | 7,794,184 | 730.44M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.376/efficientnet_b1-0626-455dcb2a.params.log)) |
| EfficientNet-B0b | 22.96 | 6.70 | 5,288,548 | 413.13M | From [rwightman/pyt...models] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.403/efficientnet_b0b-0670-8892ba58.params.log)) |
| EfficientNet-B1b | 20.98 | 5.65 | 7,794,184 | 730.44M | From [rwightman/pyt...models] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.403/efficientnet_b1b-0565-c29a1b67.params.log)) |
| EfficientNet-B2b | 19.94 | 5.16 | 9,109,994 | 1,049.29M | From [rwightman/pyt...models] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.403/efficientnet_b2b-0516-7532826e.params.log)) |
| EfficientNet-B3b | 18.60 | 4.31 | 12,233,232 | 1,923.98M | From [rwightman/pyt...models] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.403/efficientnet_b3b-0431-1e342ec2.params.log)) |
| EfficientNet-B4b | 17.25 | 3.76 | 19,341,616 | 4,597.56M | From [rwightman/pyt...models] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.403/efficientnet_b4b-0376-b60e1779.params.log)) |
| EfficientNet-B5b | 16.39 | 3.34 | 30,389,784 | 10,674.67M | From [rwightman/pyt...models] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.403/efficientnet_b5b-0334-cd70ae71.params.log)) |
| EfficientNet-B6b | 15.96 | 3.12 | 43,040,704 | 19,761.35M | From [rwightman/pyt...models] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.403/efficientnet_b6b-0312-f581d9f0.params.log)) |
| EfficientNet-B7b | 15.70 | 3.11 | 66,347,960 | 38,949.07M | From [rwightman/pyt...models] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.403/efficientnet_b7b-0311-2b8a6040.params.log)) |
| MixNet-S | 24.32 | 7.39 | 4,134,606 | 260.26M | From [rwightman/pyt...models] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.412/mixnet_s-0739-54434771.params.log)) |
| MixNet-M | 23.31 | 6.78 | 5,014,382 | 366.05M | From [rwightman/pyt...models] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.413/mixnet_m-0678-810b8967.params.log)) |
| MixNet-L | 21.53 | 6.03 | 7,329,252 | 590.45M | From [rwightman/pyt...models] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.414/mixnet_l-0603-0576f35d.params.log)) |
| ResNet(D)-50b | 20.79 | 5.49 | 25,680,808 | 20,496.80M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.296/resnetd50b-0549-17d6004b.params.log)) |
| ResNet(D)-101b | 19.49 | 4.61 | 44,672,936 | 35,391.85M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.296/resnetd101b-0461-fead1bcb.params.log)) |
| ResNet(D)-152b | 19.39 | 4.67 | 60,316,584 | 47,661.38M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.296/resnetd152b-0467-d0fe2fe0.params.log)) |

### CIFAR-10

Some remarks:
- Testing subset is used for validation purpose.
- `Features` means feature extractor output size.

| Model | Error, % | Features | Params | FLOPs/2 | Remarks |
| --- | ---: | ---: |  ---: | ---: | --- |
| NIN | 7.43 | 192 | 966,986 | 222.97M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.175/nin_cifar10-0743-9696dc1a.params.log)) |
| ResNet-20 | 5.97 | 64 | 272,474 | 41.29M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.163/resnet20_cifar10-0597-13c5ab19.params.log)) |
| ResNet-56 | 4.52 | 64 | 855,770 | 127.06M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.163/resnet56_cifar10-0452-a73e63e9.params.log)) |
| ResNet-110 | 3.69 | 64 | 1,730,714 | 255.70M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.163/resnet110_cifar10-0369-f89f1c4d.params.log)) |
| ResNet-164(BN) | 3.68 | 256 | 1,704,154 | 255.31M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.179/resnet164bn_cifar10-0368-e7941eee.params.log)) |
| ResNet-272(BN) | 3.33 | 256 | 2,816,986 | 420.61M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.368/resnet272bn_cifar10-0333-99dc36ca.params.log)) |
| ResNet-542(BN) | 3.43 | 256 | 5,599,066 | 833.87M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.369/resnet542bn_cifar10-0343-e687b254.params.log)) |
| ResNet-1001 | 3.28 | 256 | 10,328,602 | 1,536.40M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.201/resnet1001_cifar10-0328-bb979d53.params.log)) |
| ResNet-1202 | 3.53 | 64 | 19,424,026 | 2,857.17M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.214/resnet1202_cifar10-0353-377510a6.params.log)) |
| PreResNet-20 | 6.51 | 64 | 272,282 | 41.27M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.164/preresnet20_cifar10-0651-daa89573.params.log)) |
| PreResNet-56 | 4.49 | 64 | 855,578 | 127.03M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.164/preresnet56_cifar10-0449-cb37cb9d.params.log)) |
| PreResNet-110 | 3.86 | 64 | 1,730,522 | 255.68M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.164/preresnet110_cifar10-0386-d6d4b7bd.params.log)) |
| PreResNet-164(BN) | 3.64 | 256 | 1,703,258 | 255.08M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.196/preresnet164bn_cifar10-0364-7ecf30cb.params.log)) |
| PreResNet-272(BN) | 3.25 | 256 | 2,816,090 | 420.38M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.389/preresnet272bn_cifar10-0325-944ba29d.params.log)) |
| PreResNet-542(BN) | 3.14 | 256 | 5,598,170 | 833.64M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.391/preresnet542bn_cifar10-0314-ac40a67b.params.log)) |
| PreResNet-1001 | 2.65 | 256 | 10,327,706 | 1,536.18M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.209/preresnet1001_cifar10-0265-50507ff7.params.log)) |
| PreResNet-1202 | 3.39 | 64 | 19,423,834 | 2,857.14M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.246/preresnet1202_cifar10-0339-942cf6f2.params.log)) |
| ResNeXt-20 (1x64d) | 4.33 | 1024 | 3,446,602 | 538.36M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_1x64d_cifar10-0433-0661d12e.params.log)) |
| ResNeXt-20 (2x32d) | 4.53 | 1024 | 2,672,458 | 425.15M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_2x32d_cifar10-0453-afb48ca4.params.log)) |
| ResNeXt-20 (4x16d) | 4.70 | 1024 | 2,285,386 | 368.55M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_4x16d_cifar10-0470-ae1ba869.params.log)) |
| ResNeXt-20 (8x8d) | 4.66 | 1024 | 2,091,850 | 340.25M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_8x8d_cifar10-0466-280e5f89.params.log)) |
| ResNeXt-20 (16x4d) | 4.04 | 1024 | 1,995,082 | 326.10M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_16x4d_cifar10-0404-426b5b2f.params.log)) |
| ResNeXt-20 (32x2d) | 4.61 | 1024 | 1,946,698 | 319.03M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_32x2d_cifar10-0461-2d6ee836.params.log)) |
| ResNeXt-20 (64x1d) | 4.93 | 1024 | 1,922,506 | 315.49M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_64x1d_cifar10-0493-6618e9ac.params.log)) |
| ResNeXt-20 (2x64d) | 4.03 | 1024 | 6,198,602 | 987.98M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_2x64d_cifar10-0403-6f0c138f.params.log)) |
| ResNeXt-20 (4x32d) | 3.73 | 1024 | 4,650,314 | 761.57M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_4x32d_cifar10-0373-cf696060.params.log)) |
| ResNeXt-20 (8x16d) | 4.04 | 1024 | 3,876,170 | 648.37M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_8x16d_cifar10-0404-4d7f7281.params.log)) |
| ResNeXt-20 (16x8d) | 3.94 | 1024 | 3,489,098 | 591.77M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_16x8d_cifar10-0394-f81d0566.params.log)) |
| ResNeXt-20 (32x4d) | 4.20 | 1024 | 3,295,562 | 563.47M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_32x4d_cifar10-0420-a3658939.params.log)) |
| ResNeXt-20 (64x2d) | 4.38 | 1024 | 3,198,794 | 549.32M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_64x2d_cifar10-0438-32fe188b.params.log)) |
| ResNeXt-56 (1x64d) | 2.87 | 1024 | 9,317,194 | 1,399.33M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_1x64d_cifar10-0287-8edd977c.params.log)) |
| ResNeXt-56 (2x32d) | 3.01 | 1024 | 6,994,762 | 1,059.72M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_2x32d_cifar10-0301-d0284dff.params.log)) |
| ResNeXt-56 (4x16d) | 3.11 | 1024 | 5,833,546 | 889.91M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_4x16d_cifar10-0311-add022e7.params.log)) |
| ResNeXt-56 (8x8d) | 3.07 | 1024 | 5,252,938 | 805.01M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_8x8d_cifar10-0307-4f0b7246.params.log)) |
| ResNeXt-56 (16x4d) | 3.12 | 1024 | 4,962,634 | 762.56M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_16x4d_cifar10-0312-93d71b61.params.log)) |
| ResNeXt-56 (32x2d) | 3.14 | 1024 | 4,817,482 | 741.34M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_32x2d_cifar10-0314-ea8b4335.params.log)) |
| ResNeXt-56 (64x1d) | 3.41 | 1024 | 4,744,906 | 730.72M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_64x1d_cifar10-0341-12a684ad.params.log)) |
| ResNeXt-29 (32x4d) | 3.15 | 1024 | 4,775,754 | 780.55M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.169/resnext29_32x4d_cifar10-0315-c8a1beda.params.log)) |
| ResNeXt-29 (16x64d) | 2.41 | 1024 | 68,155,210 | 10,709.34M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.176/resnext29_16x64d_cifar10-0241-76b97a4d.params.log)) |
| ResNeXt-272 (1x64d) | 2.55 | 1024 | 44,540,746 | 6,565.15M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.372/resnext272_1x64d_cifar10-0255-c1a3fddc.params.log)) |
| ResNeXt-272 (2x32d) | 2.74 | 1024 | 32,928,586 | 4,867.11M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.375/resnext272_2x32d_cifar10-0274-23b391ce.params.log)) |
| SE-ResNet-20 | 6.01 | 64 | 274,847 | 41.30M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.362/seresnet20_cifar10-0601-3411e5ad.params.log)) |
| SE-ResNet-56 | 4.13 | 64 | 862,889 | 127.07M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.362/seresnet56_cifar10-0413-21bac136.params.log)) |
| SE-ResNet-110 | 3.63 | 64 | 1,744,952 | 255.72M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.362/seresnet110_cifar10-0363-fa3f09a8.params.log)) |
| SE-ResNet-164(BN) | 3.39 | 256 | 1,906,258 | 255.52M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.362/seresnet164bn_cifar10-0339-11c92315.params.log)) |
| SE-ResNet-272(BN) | 3.39 | 256 | 3,153,826 | 420.96M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.390/seresnet272bn_cifar10-0339-da4073ad.params.log)) |
| SE-ResNet-542(BN) | 3.47 | 256 | 6,272,746 | 834.57M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.385/seresnet542bn_cifar10-0347-e64d9ca4.params.log)) |
| SE-PreResNet-20 | 6.18 | 64 | 274,559 | 41.30M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.379/sepreresnet20_cifar10-0618-e55551e6.params.log)) |
| SE-PreResNet-56 | 4.51 | 64 | 862,601 | 127.07M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.379/sepreresnet56_cifar10-0451-56c29934.params.log)) |
| SE-PreResNet-110 | 4.54 | 64 | 1,744,664 | 255.72M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.379/sepreresnet110_cifar10-0454-67eea1cc.params.log)) |
| SE-PreResNet-164(BN) | 3.73 | 256 | 1,904,882 | 255.29M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.379/sepreresnet164bn_cifar10-0373-ac72ac7f.params.log)) |
| SE-PreResNet-272(BN) | 3.39 | 256 | 3,152,450 | 420.73M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.379/sepreresnet272bn_cifar10-0339-3e47d575.params.log)) |
| SE-PreResNet-542(BN) | 3.08 | 256 | 6,271,370 | 834.34M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.382/sepreresnet542bn_cifar10-0308-05f7d4a6.params.log)) |
| PyramidNet-110 (a=48) | 3.72 | 64 | 1,772,706 | 408.37M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.184/pyramidnet110_a48_cifar10-0372-35b94d05.params.log)) |
| PyramidNet-110 (a=84) | 2.98 | 100 | 3,904,446 | 778.15M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.185/pyramidnet110_a84_cifar10-0298-81710d7a.params.log)) |
| PyramidNet-110 (a=270) | 2.51 | 286 | 28,485,477 | 4,730.60M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.194/pyramidnet110_a270_cifar10-0251-1e769ce5.params.log)) |
| PyramidNet-164 (a=270, BN) | 2.42 | 1144 | 27,216,021 | 4,608.81M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.264/pyramidnet164_a270_bn_cifar10-0242-c4a79ea3.params.log)) |
| PyramidNet-200 (a=240, BN) | 2.44 | 1024 | 26,752,702 | 4,563.40M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.268/pyramidnet200_a240_bn_cifar10-0244-52f4d43e.params.log)) |
| PyramidNet-236 (a=220, BN) | 2.47 | 944 | 26,969,046 | 4,631.32M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.285/pyramidnet236_a220_bn_cifar10-0247-1bd295a7.params.log)) |
| PyramidNet-272 (a=200, BN) | 2.39 | 864 | 26,210,842 | 4,541.36M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.284/pyramidnet272_a200_bn_cifar10-0239-d7b23c54.params.log)) |
| DenseNet-40 (k=12) | 5.61 | 258 | 599,050 | 210.80M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.193/densenet40_k12_cifar10-0561-28dc0035.params.log)) |
| DenseNet-BC-40 (k=12) | 6.43 | 132 | 176,122 | 74.89M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.231/densenet40_k12_bc_cifar10-0643-7fdeda31.params.log)) |
| DenseNet-BC-40 (k=24) | 4.52 | 264 | 690,346 | 293.09M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.220/densenet40_k24_bc_cifar10-0452-13fa807e.params.log)) |
| DenseNet-BC-40 (k=36) | 4.04 | 396 | 1,542,682 | 654.60M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.224/densenet40_k36_bc_cifar10-0404-4c154567.params.log)) |
| DenseNet-100 (k=12) | 3.66 | 678 | 4,068,490 | 1,353.55M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.205/densenet100_k12_cifar10-0366-4e371ccb.params.log)) |
| DenseNet-100 (k=24) | 3.13 | 1356 | 16,114,138 | 5,354.19M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.252/densenet100_k24_cifar10-0313-9f795bac.params.log)) |
| DenseNet-BC-100 (k=12) | 4.16 | 342 | 769,162 | 298.45M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.189/densenet100_k12_bc_cifar10-0416-6685d1f4.params.log)) |
| DenseNet-BC-190 (k=40) | 2.52 | 2190 | 25,624,430 | 9,400.45M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.286/densenet190_k40_bc_cifar10-0252-87b15be0.params.log)) |
| DenseNet-BC-250 (k=24) | 2.67 | 1734 | 15,324,406 | 5,519.54M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.290/densenet250_k24_bc_cifar10-0267-dad68693.params.log)) |
| X-DenseNet-BC-40-2 (k=24) | 5.31 | 264 | 690,346 | 293.09M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.226/xdensenet40_2_k24_bc_cifar10-0531-66c9d384.params.log)) |
| X-DenseNet-BC-40-2 (k=36) | 4.37 | 396 | 1,542,682 | 654.60M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.233/xdensenet40_2_k36_bc_cifar10-0437-e9bf4192.params.log)) |
| WRN-16-10 | 2.93 | 640 | 17,116,634 | 2,414.04M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.166/wrn16_10_cifar10-0293-ecf1c17c.params.log)) |
| WRN-28-10 | 2.39 | 640 | 36,479,194 | 5,246.98M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.166/wrn28_10_cifar10-0239-16f3c8a2.params.log)) |
| WRN-40-8 | 2.37 | 512 | 35,748,314 | 5,176.90M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.166/wrn40_8_cifar10-0237-3b81d261.params.log)) |
| WRN-20-10-1bit | 3.26 | 640 | 26,737,140 | 4,019.14M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.302/wrn20_10_1bit_cifar10-0326-c1a8ba4f.params.log)) |
| WRN-20-10-32bit | 3.14 | 640 | 26,737,140 | 4,019.14M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.302/wrn20_10_32bit_cifar10-0314-35549618.params.log)) |
| RoR-3-56 | 5.43 | 64 | 762,746 | 113.43M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.228/ror3_56_cifar10-0543-ee31a69a.params.log)) |
| RoR-3-110 | 4.35 | 64 | 1,637,690 | 242.07M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.235/ror3_110_cifar10-0435-03599165.params.log)) |
| RoR-3-164 | 3.93 | 64 | 2,512,634 | 370.72M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.294/ror3_164_cifar10-0393-cc11aa06.params.log)) |
| RiR | 3.28 | 384 | 9,492,980 | 1,281.08M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.292/rir_cifar10-0328-5bed6f35.params.log)) |
| Shake-Shake-ResNet-20-2x16d | 5.15 | 64 | 541,082 | 81.78M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.215/shakeshakeresnet20_2x16d_cifar10-0515-a7b8a2f7.params.log)) |
| Shake-Shake-ResNet-26-2x32d | 3.17 | 64 | 2,923,162 | 428.89M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.217/shakeshakeresnet26_2x32d_cifar10-0317-21e60e62.params.log)) |
| DIA-ResNet-20 | 6.22 | 64 | 286,866 | 41.34M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.340/diaresnet20_cifar10-0622-3e47641d.params.log)) |
| DIA-ResNet-56 | 5.05 | 64 | 870,162 | 127.18M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.340/diaresnet56_cifar10-0505-45df6974.params.log)) |
| DIA-ResNet-110 | 4.10 | 64 | 1,745,106 | 255.94M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.340/diaresnet110_cifar10-0410-56f547ec.params.log)) |
| DIA-ResNet-164(BN) | 3.50 | 256 | 1,923,002 | 259.18M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.340/diaresnet164bn_cifar10-0350-533e7c6a.params.log)) |
| DIA-PreResNet-20 | 6.42 | 64 | 286,674 | 41.31M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.343/diapreresnet20_cifar10-0642-ec36098c.params.log)) |
| DIA-PreResNet-56 | 4.83 | 64 | 869,970 | 127.15M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.343/diapreresnet56_cifar10-0483-cba6950f.params.log)) |
| DIA-PreResNet-110 | 4.25 | 64 | 1,744,914 | 255.92M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.343/diapreresnet110_cifar10-0425-f4eae5ab.params.log)) |
| DIA-PreResNet-164(BN) | 3.56 | 256 | 1,922,106 | 258.95M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.343/diapreresnet164bn_cifar10-0356-9cf07392.params.log)) |

### CIFAR-100

Some remarks:
- Testing subset is used for validation purpose.

| Model | Error, % | Params | FLOPs/2 | Remarks |
| --- | ---: | ---: | ---: | --- |
| NIN | 28.39 | 984,356 | 224.08M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.183/nin_cifar100-2839-eed0e9af.params.log)) |
| ResNet-20 | 29.64 | 278,324 | 41.30M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.180/resnet20_cifar100-2964-4e144352.params.log)) |
| ResNet-56 | 24.88 | 861,620 | 127.06M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.181/resnet56_cifar100-2488-59097710.params.log)) |
| ResNet-110 | 22.80 | 1,736,564 | 255.71M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.190/resnet110_cifar100-2280-6c5fa14b.params.log)) |
| ResNet-164(BN) | 20.44 | 1,727,284 | 255.33M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.182/resnet164bn_cifar100-2044-c7db7b5e.params.log)) |
| ResNet-272(BN) | 20.07 | 2,840,116 | 420.63M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.368/resnet272bn_cifar100-2007-088af5c2.params.log)) |
| ResNet-542(BN) | 19.32 | 5,622,196 | 833.89M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.369/resnet542bn_cifar100-1932-df8bd526.params.log)) |
| ResNet-1001 | 19.79 | 10,351,732 | 1,536.43M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.254/resnet1001_cifar100-1979-692d9516.params.log)) |
| ResNet-1202 | 21.56 | 19,429,876 | 2,857.17M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.410/resnet1202_cifar100-2156-1d94f9cc.params.log)) |
| PreResNet-20 | 30.22 | 278,132 | 41.28M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.187/preresnet20_cifar100-3022-37f15365.params.log)) |
| PreResNet-56 | 25.05 | 861,428 | 127.04M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.188/preresnet56_cifar100-2505-4c39e83f.params.log)) |
| PreResNet-110 | 22.67 | 1,736,372 | 255.68M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.191/preresnet110_cifar100-2267-18cf4161.params.log)) |
| PreResNet-164(BN) | 20.18 | 1,726,388 | 255.10M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.192/preresnet164bn_cifar100-2018-a20557c8.params.log)) |
| PreResNet-272(BN) | 19.63 | 2,839,220 | 420.40M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.389/preresnet272bn_cifar100-1963-38e296be.params.log)) |
| PreResNet-542(BN) | 18.71 | 5,621,300 | 833.66M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.391/preresnet542bn_cifar100-1871-d536ad01.params.log)) |
| PreResNet-1001 | 18.41 | 10,350,836 | 1,536.20M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.283/preresnet1001_cifar100-1841-185e033d.params.log)) |
| ResNeXt-20 (1x64d) | 21.97 | 3,538,852 | 538.45M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_1x64d_cifar100-2197-e7073542.params.log)) |
| ResNeXt-20 (2x32d) | 22.55 | 2,764,708 | 425.25M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_2x32d_cifar100-2255-995281ee.params.log)) |
| ResNeXt-20 (4x16d) | 23.04 | 2,377,636 | 368.65M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_4x16d_cifar100-2304-2c9d578a.params.log)) |
| ResNeXt-20 (8x8d) | 22.82 | 2,184,100 | 340.34M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_8x8d_cifar100-2282-363f03e8.params.log)) |
| ResNeXt-20 (16x4d) | 22.82 | 2,087,332 | 326.19M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_16x4d_cifar100-2282-508d3227.params.log)) |
| ResNeXt-20 (32x2d) | 21.73 | 2,038,948 | 319.12M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_32x2d_cifar100-2322-ce652014.params.log)) |
| ResNeXt-20 (64x1d) | 23.53 | 2,014,756 | 315.58M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_64x1d_cifar100-2353-9c789af4.params.log)) |
| ResNeXt-20 (2x64d) | 20.60 | 6,290,852 | 988.07M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_2x64d_cifar100-2060-5f6dfa3f.params.log)) |
| ResNeXt-20 (4x32d) | 21.31 | 4,742,564 | 761.66M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_4x32d_cifar100-2131-2c558efc.params.log)) |
| ResNeXt-20 (8x16d) | 21.72 | 3,968,420 | 648.46M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_8x16d_cifar100-2172-3fc47c70.params.log)) |
| ResNeXt-20 (16x8d) | 21.73 | 3,581,348 | 591.86M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_16x8d_cifar100-2173-a246aea5.params.log)) |
| ResNeXt-20 (32x4d) | 22.13 | 3,387,812 | 563.56M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_32x4d_cifar100-2213-5b2ffba8.params.log)) |
| ResNeXt-20 (64x2d) | 22.35 | 3,291,044 | 549.41M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_64x2d_cifar100-2235-62fcc38a.params.log)) |
| ResNeXt-56 (1x64d) | 18.25 | 9,409,444 | 1,399.42M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_1x64d_cifar100-1825-b78642c1.params.log)) |
| ResNeXt-56 (2x32d) | 17.86 | 7,087,012 | 1,059.81M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_2x32d_cifar100-1786-32205070.params.log)) |
| ResNeXt-56 (4x16d) | 18.09 | 5,925,796 | 890.01M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_4x16d_cifar100-1809-366de7b5.params.log)) |
| ResNeXt-56 (8x8d) | 18.06 | 5,345,188 | 805.10M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_8x8d_cifar100-1806-827a485e.params.log)) |
| ResNeXt-56 (16x4d) | 18.24 | 5,054,884 | 762.65M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_16x4d_cifar100-1824-9cb7a132.params.log)) |
| ResNeXt-56 (32x2d) | 18.60 | 4,909,732 | 741.43M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_32x2d_cifar100-1860-3f65de93.params.log)) |
| ResNeXt-56 (64x1d) | 18.16 | 4,837,156 | 730.81M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_64x1d_cifar100-1816-b80f4315.params.log)) |
| ResNeXt-29 (32x4d) | 19.50 | 4,868,004 | 780.64M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.200/resnext29_32x4d_cifar100-1950-5f2eedcd.params.log)) |
| ResNeXt-29 (16x64d) | 16.93 | 68,247,460 | 10,709.43M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.322/resnext29_16x64d_cifar100-1693-1fcec90d.params.log)) |
| ResNeXt-272 (1x64d) | 19.11 | 44,632,996 | 6,565.25M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.372/resnext272_1x64d_cifar100-1911-e0b3656a.params.log)) |
| ResNeXt-272 (2x32d) | 18.34 | 33,020,836 | 4,867.20M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.375/resnext272_2x32d_cifar100-1834-4802083b.params.log)) |
| SE-ResNet-20 | 28.54 | 280,697 | 41.30M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.362/seresnet20_cifar100-2854-184ad148.params.log)) |
| SE-ResNet-56 | 22.94 | 868,739 | 127.07M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.362/seresnet56_cifar100-2294-989d4d92.params.log)) |
| SE-ResNet-110 | 20.86 | 1,750,802 | 255.72M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.362/seresnet110_cifar100-2086-5345be41.params.log)) |
| SE-ResNet-164(BN) | 19.95 | 1,929,388 | 255.54M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.362/seresnet164bn_cifar100-1995-6c9dc66b.params.log)) |
| SE-ResNet-272(BN) | 19.07 | 3,176,956 | 420.98M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.390/seresnet272bn_cifar100-1907-754af937.params.log)) |
| SE-ResNet-542(BN) | 18.87 | 6,295,876 | 834.59M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.385/seresnet542bn_cifar100-1887-cd76c769.params.log)) |
| SE-PreResNet-20 | 28.31 | 280,409 | 41.31M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.379/sepreresnet20_cifar100-2831-ee5d3bd6.params.log)) |
| SE-PreResNet-56 | 23.05 | 868,451 | 127.08M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.379/sepreresnet56_cifar100-2305-313a7a30.params.log)) |
| SE-PreResNet-110 | 22.61 | 1,750,514 | 255.73M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.379/sepreresnet110_cifar100-2261-3291a56b.params.log)) |
| SE-PreResNet-164(BN) | 20.05 | 1,928,012 | 255.31M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.379/sepreresnet164bn_cifar100-2005-d9399367.params.log)) |
| SE-PreResNet-272(BN) | 19.13 | 3,175,580 | 420.75M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.379/sepreresnet272bn_cifar100-1913-d243b058.params.log)) |
| SE-PreResNet-542(BN) | 19.45 | 6,294,500 | 834.36M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.382/sepreresnet542bn_cifar100-1945-4dd0e21d.params.log)) |
| PyramidNet-110 (a=48) | 20.95 | 1,778,556 | 408.38M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.186/pyramidnet110_a48_cifar100-2095-00fd42a0.params.log)) |
| PyramidNet-110 (a=84) | 18.87 | 3,913,536 | 778.16M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.199/pyramidnet110_a84_cifar100-1887-6712d5dc.params.log)) |
| PyramidNet-110 (a=270) | 17.10 | 28,511,307 | 4,730.62M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.319/pyramidnet110_a270_cifar100-1710-2732fc64.params.log)) |
| PyramidNet-164 (a=270, BN) | 16.70 | 27,319,071 | 4,608.91M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.312/pyramidnet164_a270_bn_cifar100-1670-08f46c7f.params.log)) |
| PyramidNet-200 (a=240, BN) | 16.09 | 26,844,952 | 4,563.49M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.317/pyramidnet200_a240_bn_cifar100-1609-e61e7e7e.params.log)) |
| PyramidNet-236 (a=220, BN) | 16.34 | 27,054,096 | 4,631.41M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.312/pyramidnet236_a220_bn_cifar100-1634-f066b3c6.params.log)) |
| PyramidNet-272 (a=200, BN) | 16.19 | 26,288,692 | 4,541.43M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.312/pyramidnet272_a200_bn_cifar100-1619-486e9427.params.log)) |
| DenseNet-40 (k=12) | 24.90 | 622,360 | 210.82M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.195/densenet40_k12_cifar100-2490-908f02ba.params.log)) |
| DenseNet-BC-40 (k=12) | 28.41 | 188,092 | 74.90M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.232/densenet40_k12_bc_cifar100-2841-35cd8e6a.params.log)) |
| DenseNet-BC-40 (k=24) | 22.67 | 714,196 | 293.11M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.221/densenet40_k24_bc_cifar100-2267-2c4ef7c4.params.log)) |
| DenseNet-BC-40 (k=36) | 20.50 | 1,578,412 | 654.64M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.225/densenet40_k36_bc_cifar100-2050-d7275d39.params.log)) |
| DenseNet-100 (k=12) | 19.64 | 4,129,600 | 1,353.62M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.206/densenet100_k12_cifar100-1964-2ed5ec27.params.log)) |
| DenseNet-100 (k=24) | 18.08 | 16,236,268 | 5,354.32M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.318/densenet100_k24_cifar100-1808-9bfa3e9c.params.log)) |
| DenseNet-BC-100 (k=12) | 21.19 | 800,032 | 298.48M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.208/densenet100_k12_bc_cifar100-2119-fbd8a54c.params.log)) |
| DenseNet-BC-250 (k=24) | 17.39 | 15,480,556 | 5,519.69M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.303/densenet250_k24_bc_cifar100-1739-598e91b7.params.log)) |
| X-DenseNet-BC-40-2 (k=24) | 23.96 | 714,196 | 293.11M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.227/xdensenet40_2_k24_bc_cifar100-2396-73d5ba88.params.log)) |
| X-DenseNet-BC-40-2 (k=36) | 21.65 | 1,578,412 | 654.64M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.234/xdensenet40_2_k36_bc_cifar100-2165-78b6e754.params.log)) |
| WRN-16-10 | 18.95 | 17,174,324 | 2,414.09M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.204/wrn16_10_cifar100-1895-bcb5c89c.params.log)) |
| WRN-28-10 | 17.88 | 36,536,884 | 5,247.04M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.320/wrn28_10_cifar100-1788-67ec43c6.params.log)) |
| WRN-40-8 | 18.03 | 35,794,484 | 5,176.95M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.321/wrn40_8_cifar100-1803-114f6be2.params.log)) |
| WRN-20-10-1bit | 19.04 | 26,794,920 | 4,022.81M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.302/wrn20_10_1bit_cifar100-1904-adae01d6.params.log)) |
| WRN-20-10-32bit | 18.12 | 26,794,920 | 4,022.81M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.302/wrn20_10_32bit_cifar100-1812-d064f38a.params.log)) |
| RoR-3-56 | 25.49 | 768,596 | 113.43M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.229/ror3_56_cifar100-2549-43345593.params.log)) |
| RoR-3-110 | 23.64 | 1,643,540 | 242.08M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.236/ror3_110_cifar100-2364-b8c4d317.params.log)) |
| RoR-3-164 | 22.34 | 2,518,484 | 370.72M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.294/ror3_164_cifar100-2234-eb6a7fb8.params.log)) |
| RiR | 19.23 | 9,527,720 | 1,283.29M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.292/rir_cifar100-1923-c4256383.params.log)) |
| Shake-Shake-ResNet-20-2x16d | 29.22 | 546,932 | 81.79M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.247/shakeshakeresnet20_2x16d_cifar100-2922-e46e31a7.params.log)) |
| Shake-Shake-ResNet-26-2x32d | 18.80 | 2,934,772 | 428.90M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.222/shakeshakeresnet26_2x32d_cifar100-1880-bd46a741.params.log)) |
| DIA-ResNet-20 | 27.71 | 292,716 | 41.34M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.342/diaresnet20_cifar100-2771-3a58490e.params.log)) |
| DIA-ResNet-56 | 24.35 | 876,012 | 127.18M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.342/diaresnet56_cifar100-2435-e45b7f28.params.log)) |
| DIA-ResNet-110 | 22.11 | 1,750,956 | 255.95M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.342/diaresnet110_cifar100-2211-e99fad4e.params.log)) |
| DIA-ResNet-164(BN) | 19.53 | 1,946,132 | 259.20M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.342/diaresnet164bn_cifar100-1953-43fa3821.params.log)) |
| DIA-PreResNet-20 | 28.37 | 292,524 | 41.32M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.343/diapreresnet20_cifar100-2837-32f0f1be.params.log)) |
| DIA-PreResNet-56 | 25.05 | 875,820 | 127.16M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.343/diapreresnet56_cifar100-2505-c9f8bd43.params.log)) |
| DIA-PreResNet-110 | 22.69 | 1,750,764 | 255.92M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.343/diapreresnet110_cifar100-2269-78d79bab.params.log)) |
| DIA-PreResNet-164(BN) | 19.99 | 1,945,236 | 258.97M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.343/diapreresnet164bn_cifar100-1999-1625154f.params.log)) |

### SVHN

| Model | Error, % | Params | FLOPs/2 | Remarks |
| --- | ---: | ---: | ---: | --- |
| NIN | 3.76 | 966,986 | 222.97M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.270/nin_svhn-0376-7cb75018.params.log)) |
| ResNet-20 | 3.43 | 272,474 | 41.29M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.265/resnet20_svhn-0343-7ac0d94a.params.log)) |
| ResNet-56 | 2.75 | 855,770 | 127.06M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.265/resnet56_svhn-0275-e676e421.params.log)) |
| ResNet-110 | 2.45 | 1,730,714 | 255.70M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.265/resnet110_svhn-0245-0570b594.params.log)) |
| ResNet-164(BN) | 2.42 | 1,704,154 | 255.31M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.267/resnet164bn_svhn-0242-8cdce674.params.log)) |
| ResNet-272(BN) | 2.43 | 2,816,986 | 420.61M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.368/resnet272bn_svhn-0243-39d741c8.params.log)) |
| ResNet-542(BN) | 2.34 | 5,599,066 | 833.87M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.369/resnet542bn_svhn-0234-4f78075c.params.log)) |
| ResNet-1001 | 2.41 | 10,328,602 | 1,536.40M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.408/resnet1001_svhn-0241-031fb0ce.params.log)) |
| PreResNet-20 | 3.22 | 272,282 | 41.27M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.269/preresnet20_svhn-0322-608cee12.params.log)) |
| PreResNet-56 | 2.80 | 855,578 | 127.03M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.269/preresnet56_svhn-0280-b974c2c9.params.log)) |
| PreResNet-110 | 2.79 | 1,730,522 | 255.68M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.269/preresnet110_svhn-0279-6804450b.params.log)) |
| PreResNet-164(BN) | 2.58 | 1,703,258 | 255.08M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.269/preresnet164bn_svhn-0258-4aeee06a.params.log)) |
| PreResNet-272(BN) | 2.34 | 2,816,090 | 420.38M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.389/preresnet272bn_svhn-0234-7ff97873.params.log)) |
| PreResNet-542(BN) | 2.36 | 5,598,170 | 833.64M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.391/preresnet542bn_svhn-0236-3a4633f1.params.log)) |
| ResNeXt-20 (1x64d) | 2.98 | 3,446,602 | 538.36M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_1x64d_svhn-0298-3c7febc8.params.log)) |
| ResNeXt-20 (2x32d) | 2.96 | 2,672,458 | 425.15M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_2x32d_svhn-0296-54189677.params.log)) |
| ResNeXt-20 (4x16d) | 3.17 | 2,285,386 | 368.55M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_4x16d_svhn-0317-6691c8f5.params.log)) |
| ResNeXt-20 (8x8d) | 3.18 | 2,091,850 | 340.25M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_8x8d_svhn-0318-c1536efb.params.log)) |
| ResNeXt-20 (16x4d) | 3.21 | 1,995,082 | 326.10M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_16x4d_svhn-0321-854df3b7.params.log)) |
| ResNeXt-20 (32x2d) | 3.27 | 1,946,698 | 319.03M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_32x2d_svhn-0327-2499ff6d.params.log)) |
| ResNeXt-20 (64x1d) | 3.42 | 1,922,506 | 315.49M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_64x1d_svhn-0342-2591ea44.params.log)) |
| ResNeXt-20 (2x64d) | 2.83 | 6,198,602 | 987.98M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_2x64d_svhn-0283-9c77f074.params.log)) |
| ResNeXt-20 (4x32d) | 2.98 | 4,650,314 | 761.57M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_4x32d_svhn-0298-1da9a7bf.params.log)) |
| ResNeXt-20 (8x16d) | 3.01 | 3,876,170 | 648.37M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_8x16d_svhn-0301-41b28fd3.params.log)) |
| ResNeXt-20 (16x8d) | 2.93 | 3,489,098 | 591.77M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_16x8d_svhn-0293-31f4b14e.params.log)) |
| ResNeXt-20 (32x4d) | 3.09 | 3,295,562 | 563.47M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_32x4d_svhn-0309-ddbef9ac.params.log)) |
| ResNeXt-20 (64x2d) | 3.14 | 3,198,794 | 549.32M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.365/resnext20_64x2d_svhn-0314-4c01490b.params.log)) |
| ResNeXt-56 (1x64d) | 2.42 | 9,317,194 | 1,399.33M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_1x64d_svhn-0242-860c610c.params.log)) |
| ResNeXt-56 (2x32d) | 2.46 | 6,994,762 | 1,059.72M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_2x32d_svhn-0246-ffb8df9b.params.log)) |
| ResNeXt-56 (4x16d) | 2.44 | 5,833,546 | 889.91M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_4x16d_svhn-0244-f7b697f9.params.log)) |
| ResNeXt-56 (8x8d) | 2.47 | 5,252,938 | 805.01M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_8x8d_svhn-0247-f0550cd0.params.log)) |
| ResNeXt-56 (16x4d) | 2.56 | 4,962,634 | 762.56M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_16x4d_svhn-0256-943386bd.params.log)) |
| ResNeXt-56 (32x2d) | 2.53 | 4,817,482 | 741.34M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_32x2d_svhn-0253-ba8c809d.params.log)) |
| ResNeXt-56 (64x1d) | 2.55 | 4,744,906 | 730.72M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.367/resnext56_64x1d_svhn-0255-144bab62.params.log)) |
| ResNeXt-29 (32x4d) | 2.80 | 4,775,754 | 780.55M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.275/resnext29_32x4d_svhn-0280-dcb6aef9.params.log)) |
| ResNeXt-29 (16x64d) | 2.68 | 68,155,210 | 10,709.34M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.358/resnext29_16x64d_svhn-0268-c57307f3.params.log)) |
| ResNeXt-272 (1x64d) | 2.35 | 44,540,746 | 6,565.15M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.372/resnext272_1x64d_svhn-0235-025ee7b9.params.log)) |
| ResNeXt-272 (2x32d) | 2.44 | 32,928,586 | 4,867.11M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.375/resnext272_2x32d_svhn-0244-b65ddfe3.params.log)) |
| SE-ResNet-20 | 3.23 | 274,847 | 41.30M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.362/seresnet20_svhn-0323-a3a3c677.params.log)) |
| SE-ResNet-56 | 2.64 | 862,889 | 127.07M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.362/seresnet56_svhn-0264-63a155ac.params.log)) |
| SE-ResNet-110 | 2.35 | 1,744,952 | 255.72M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.362/seresnet110_svhn-0235-d129498a.params.log)) |
| SE-ResNet-164(BN) | 2.45 | 1,906,258 | 255.52M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.362/seresnet164bn_svhn-0245-d97ea6c8.params.log)) |
| SE-ResNet-272(BN) | 2.38 | 3,153,826 | 420.96M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.390/seresnet272bn_svhn-0238-9ffe8aca.params.log)) |
| SE-ResNet-542(BN) | 2.26 | 6,272,746 | 834.57M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.385/seresnet542bn_svhn-0226-05ce3771.params.log)) |
| SE-PreResNet-20 | 3.24 | 274,559 | 41.30M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.379/sepreresnet20_svhn-0324-d5bb6768.params.log)) |
| SE-PreResNet-56 | 2.71 | 862,601 | 127.07M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.379/sepreresnet56_svhn-0271-f556af3d.params.log)) |
| SE-PreResNet-110 | 2.59 | 1,744,664 | 255.72M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.379/sepreresnet110_svhn-0259-5c09cacb.params.log)) |
| SE-PreResNet-164(BN) | 2.56 | 1,904,882 | 255.29M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.379/sepreresnet164bn_svhn-0256-a45d1a65.params.log)) |
| SE-PreResNet-272(BN) | 2.49 | 3,152,450 | 420.73M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.379/sepreresnet272bn_svhn-0249-34b910cd.params.log)) |
| SE-PreResNet-542(BN) | 2.47 | 6,271,370 | 834.34M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.382/sepreresnet542bn_svhn-0247-456035da.params.log)) |
| PyramidNet-110 (a=48) | 2.47 | 1,772,706 | 408.37M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.281/pyramidnet110_a48_svhn-0247-d8a5c6e2.params.log)) |
| PyramidNet-110 (a=84) | 2.43 | 3,904,446 | 778.15M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.392/pyramidnet110_a84_svhn-0243-473cc640.params.log)) |
| PyramidNet-110 (a=270) | 2.38 | 28,485,477 | 4,730.60M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.393/pyramidnet110_a270_svhn-0238-034be542.params.log)) |
| PyramidNet-164 (a=270, BN) | 2.33 | 27,216,021 | 4,608.81M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.396/pyramidnet164_a270_bn_svhn-0233-27b67f14.params.log)) |
| PyramidNet-200 (a=240, BN) | 2.32 | 26,752,702 | 4,563.40M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.397/pyramidnet200_a240_bn_svhn-0232-02bf262e.params.log)) |
| PyramidNet-236 (a=220, BN) | 2.35 | 26,969,046 | 4,631.32M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.398/pyramidnet236_a220_bn_svhn-0235-1a0c0711.params.log)) |
| PyramidNet-272 (a=200, BN) | 2.40 | 26,210,842 | 4,541.36M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.404/pyramidnet272_a200_bn_svhn-0240-dcd9af34.params.log)) |
| DenseNet-40 (k=12) | 3.05 | 599,050 | 210.80M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.278/densenet40_k12_svhn-0305-645564c1.params.log)) |
| DenseNet-BC-40 (k=12) | 3.20 | 176,122 | 74.89M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.279/densenet40_k12_bc_svhn-0320-6f2f9824.params.log)) |
| DenseNet-BC-40 (k=24) | 2.90 | 690,346 | 293.09M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.280/densenet40_k24_bc_svhn-0290-03e136dd.params.log)) |
| DenseNet-BC-40 (k=36) | 2.60 | 1,542,682 | 654.60M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.311/densenet40_k36_bc_svhn-0260-b81ec8d6.params.log)) |
| DenseNet-100 (k=12) | 2.60 | 4,068,490 | 1,353.55M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.311/densenet100_k12_svhn-0260-3e2b34b2.params.log)) |
| X-DenseNet-BC-40-2 (k=24) | 2.87 | 690,346 | 293.09M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.306/xdensenet40_2_k24_bc_svhn-0287-745f374b.params.log)) |
| X-DenseNet-BC-40-2 (k=36) | 2.74 | 1,542,682 | 654.60M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.306/xdensenet40_2_k36_bc_svhn-0274-4377e891.params.log)) |
| WRN-16-10 | 2.78 | 17,116,634 | 2,414.04M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.271/wrn16_10_svhn-0278-76f4e136.params.log)) |
| WRN-28-10 | 2.71 | 36,479,194 | 5,246.98M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.276/wrn28_10_svhn-0271-fcd7a6b0.params.log)) |
| WRN-40-8 | 2.54 | 35,748,314 | 5,176.90M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.277/wrn40_8_svhn-0254-be7a21da.params.log)) |
| WRN-20-10-1bit | 2.73 | 26,737,140 | 4,019.14M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.302/wrn20_10_1bit_svhn-0273-ce9f819c.params.log)) |
| WRN-20-10-32bit | 2.59 | 26,737,140 | 4,019.14M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.302/wrn20_10_32bit_svhn-0259-d9e8b46e.params.log)) |
| RoR-3-56 | 2.69 | 762,746 | 113.43M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.287/ror3_56_svhn-0269-56617cf9.params.log)) |
| RoR-3-110 | 2.57 | 1,637,690 | 242.07M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.287/ror3_110_svhn-0257-0677b7df.params.log)) |
| RoR-3-164 | 2.73 | 2,512,634 | 370.72M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.294/ror3_164_svhn-0273-b008c1b0.params.log)) |
| RiR | 2.68 | 9,492,980 | 1,281.08M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.292/rir_svhn-0268-1c0718de.params.log)) |
| Shake-Shake-ResNet-20-2x16d | 3.17 | 541,082 | 81.78M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.295/shakeshakeresnet20_2x16d_svhn-0317-7a48fde5.params.log)) |
| Shake-Shake-ResNet-26-2x32d | 2.62 | 2,923,162 | 428.89M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.295/shakeshakeresnet26_2x32d_svhn-0262-f1dbb8ef.params.log)) |
| DIA-ResNet-20 | 3.23 | 286,866 | 41.34M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.340/diaresnet20_svhn-0323-579535dd.params.log)) |
| DIA-ResNet-56 | 2.68 | 870,162 | 127.18M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.340/diaresnet56_svhn-0268-8f2c0574.params.log)) |
| DIA-ResNet-110 | 2.47 | 1,745,106 | 255.94M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.340/diaresnet110_svhn-0247-c587ac09.params.log)) |
| DIA-ResNet-164(BN) | 2.44 | 1,923,002 | 259.18M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.340/diaresnet164bn_svhn-0244-eba062dc.params.log)) |
| DIA-PreResNet-20 | 3.03 | 286,674 | 41.31M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.343/diapreresnet20_svhn-0303-e33be387.params.log)) |
| DIA-PreResNet-56 | 2.80 | 869,970 | 127.15M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.343/diapreresnet56_svhn-0280-98a2a0ba.params.log)) |
| DIA-PreResNet-110 | 2.42 | 1,744,914 | 255.92M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.343/diapreresnet110_svhn-0242-decb3765.params.log)) |
| DIA-PreResNet-164(BN) | 2.56 | 1,922,106 | 258.95M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.343/diapreresnet164bn_svhn-0256-8476c5c9.params.log)) |

### CUB-200-2011

| Model | Error, % | Params | FLOPs/2 | Remarks |
| --- | ---: | ---: | ---: | --- |
| ResNet-10 | 27.65 | 5,008,392 | 893.63M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.335/resnet10_cub-2765-9dab9a49.params.log)) |
| ResNet-12 | 26.58 | 5,082,376 | 1,125.84M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.336/resnet12_cub-2658-a46b8ec2.params.log)) |
| ResNet-14 | 24.35 | 5,377,800 | 1,357.53M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.337/resnet14_cub-2435-0b9801b2.params.log)) |
| ResNet-16 | 23.21 | 6,558,472 | 1,588.93M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.338/resnet16_cub-2321-031374ad.params.log)) |
| ResNet-18 | 23.30 | 11,279,112 | 1,820.00M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.344/resnet18_cub-2330-e7271200.params.log)) |
| ResNet-26 | 22.52 | 17,549,832 | 2,746.38M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.345/resnet26_cub-2252-61cce1ea.params.log)) |
| SE-ResNet-10 | 27.39 | 5,052,932 | 893.67M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.361/seresnet10_cub-2739-7060c03f.params.log)) |
| SE-ResNet-12 | 26.04 | 5,127,496 | 1,125.88M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.361/seresnet12_cub-2604-ee095118.params.log)) |
| SE-ResNet-14 | 23.63 | 5,425,104 | 1,357.58M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.361/seresnet14_cub-2363-5d2049d5.params.log)) |
| SE-ResNet-16 | 23.21 | 6,614,240 | 1,588.99M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.361/seresnet16_cub-2321-576e58ef.params.log)) |
| SE-ResNet-18 | 23.08 | 11,368,192 | 1,820.10M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.361/seresnet18_cub-2308-3d2496d6.params.log)) |
| SE-ResNet-26 | 22.51 | 17,683,452 | 2,746.52M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.361/seresnet26_cub-2251-8d54edb2.params.log)) |
| MobileNet x1.0 | 23.46 | 3,411,976 | 578.98M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.346/mobilenet_w1_cub-2346-efcad3dc.params.log)) |
| ProxylessNAS Mobile | 21.88 | 3,055,712 | 331.44M | Training ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.347/proxylessnas_mobile_cub-2188-36d33231.params.log)) |
| NTS-Net | 13.26 | 28,623,333 | 33,361.39M | From [yangze0930/NTS-Net] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.334/ntsnet_cub-1326-75ae8cdc.params.log)) |

### Pascal VOC20102

| Model | Extractor | Pix.Acc.,% | mIoU,% | Params | FLOPs/2 | Remarks |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| PSPNet | ResNet(D)-101b | 98.09 | 81.44 | 65,708,501 | 230,586.69M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.297/pspnet_resnetd101b_voc-8144-e15319bf.params.log)) |
| DeepLabv3 | ResNet(D)-101b | 97.95 | 80.24 | 58,754,773 | 47,624.54M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.298/deeplabv3_resnetd101b_voc-8024-8ee3099c.params.log)) |
| DeepLabv3 | ResNet(D)-152b | 98.11 | 81.20 | 74,398,421 | 59,894.06M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.298/deeplabv3_resnetd152b_voc-8120-88fb315d.params.log)) |
| FCN-8s(d) | ResNet(D)-101b | 97.80 | 80.40 | 52,072,917 | 196,562.96M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.299/fcn8sd_resnetd101b_voc-8040-f6c67c75.params.log)) |

### ADE20K

| Model | Extractor | Pix.Acc.,% | mIoU,% | Params | FLOPs/2 | Remarks |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| PSPNet | ResNet(D)-50b | 79.37 | 36.87 | 46,782,550 | 162,410.82M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.297/pspnet_resnetd50b_ade20k-3687-f0dcdf73.params.log)) |
| PSPNet | ResNet(D)-101b | 79.93 | 37.97 | 65,774,678 | 230,824.47M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.297/pspnet_resnetd101b_ade20k-3797-c1280aea.params.log)) |
| DeepLabv3 | ResNet(D)-50b | 79.72 | 37.13 | 39,795,798 | 32,755.38M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.298/deeplabv3_resnetd50b_ade20k-3713-5d5e2f74.params.log)) |
| DeepLabv3 | ResNet(D)-101b | 80.21 | 37.84 | 58,787,926 | 47,650.43M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.298/deeplabv3_resnetd101b_ade20k-3784-6224836f.params.log)) |
| FCN-8s(d) | ResNet(D)-50b | 76.92 | 33.39 | 33,146,966 | 128,387.08M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.299/fcn8sd_resnetd50b_ade20k-3339-9856c5ee.params.log)) |
| FCN-8s(d) | ResNet(D)-101b | 79.01 | 35.88 | 52,139,094 | 196,800.73M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.299/fcn8sd_resnetd101b_ade20k-3588-081774b2.params.log)) |

### Cityscapes

| Model | Extractor | Pix.Acc.,% | mIoU,% | Params | FLOPs/2 | Remarks |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| PSPNet | ResNet(D)-101b | 96.17 | 71.72 | 65,707,475 | 230,583.01M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.297/pspnet_resnetd101b_cityscapes-7172-d5ad2fa4.params.log)) |

### COCO

| Model | Extractor | Pix.Acc.,% | mIoU,% | Params | FLOPs/2 | Remarks |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| PSPNet | ResNet(D)-101b | 92.05 | 67.41 | 65,708,501 | 230,586.69M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.297/pspnet_resnetd101b_coco-6741-87582b79.params.log)) |
| DeepLabv3 | ResNet(D)-101b | 92.19 | 67.73 | 58,754,773 | 47,624.54M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.298/deeplabv3_resnetd101b_coco-6773-74dc9914.params.log)) |
| DeepLabv3 | ResNet(D)-152b | 92.24 | 68.99 | 74,398,421 | 275,084.22M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.298/deeplabv3_resnetd152b_coco-6899-edd79b4c.params.log)) |
| FCN-8s(d) | ResNet(D)-101b | 91.44 | 60.11 | 52,072,917 | 196,562.96M | From [dmlc/gluon-cv] ([log](https://github.com/osmr/imgclsmob/releases/download/v0.0.299/fcn8sd_resnetd101b_coco-6011-05e97cc5.params.log)) |

[dmlc/gluon-cv]: https://github.com/dmlc/gluon-cv
[tornadomeet/ResNet]: https://github.com/tornadomeet/ResNet
[Cadene/pretrained...pytorch]: https://github.com/Cadene/pretrained-models.pytorch
[ShichenLiu/CondenseNet]: https://github.com/ShichenLiu/CondenseNet
[clavichord93/MENet]: https://github.com/clavichord93/MENet
[clavichord93/FD-MobileNet]: https://github.com/clavichord93/FD-MobileNet
[tensorpack/tensorpack]: https://github.com/tensorpack/tensorpack
[dyhan0920/Pyramid...PyTorch]: https://github.com/dyhan0920/PyramidNet-PyTorch
[zeusees/Mnasnet...Model]: https://github.com/zeusees/Mnasnet-Pretrained-Model
[szagoruyko/diracnets]: https://github.com/szagoruyko/diracnets
[szagoruyko/functional-zoo]: https://github.com/szagoruyko/functional-zoo
[fyu/drn]: https://github.com/fyu/drn
[quark0/darts]: https://github.com/quark0/darts
[soeaver/AirNet-PyTorch]: https://github.com/soeaver/AirNet-PyTorch
[soeaver/mxnet-model]: https://github.com/soeaver/mxnet-model
[Jongchan/attention-module]: https://github.com/Jongchan/attention-module
[XingangPan/IBN-Net]: https://github.com/XingangPan/IBN-Net
[cypw/CRU-Net]: https://github.com/cypw/CRU-Net
[kevin-ssy/FishNet]: https://github.com/kevin-ssy/FishNet
[ucbdrive/dla]: https://github.com/ucbdrive/dla
[sacmehta/ESPNetv2]: https://github.com/sacmehta/ESPNetv2
[jhjacobsen/pytorch-i-revnet]: https://github.com/jhjacobsen/pytorch-i-revnet
[wielandbrendel/bag...models]: https://github.com/wielandbrendel/bag-of-local-features-models
[MIT-HAN-LAB/ProxylessNAS]: https://github.com/MIT-HAN-LAB/ProxylessNAS
[yangze0930/NTS-Net]: https://github.com/yangze0930/NTS-Net
[rwightman/pyt...models]: https://github.com/rwightman/pytorch-image-models