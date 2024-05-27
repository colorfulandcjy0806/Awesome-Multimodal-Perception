# Awesome-Multimodal-Perception 🌈
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
如果你希望阅读本文档的中文版本，请点击[这里](./README.md)。 

If you would like to read the English version of this document, please click [Here](./English.md).

欢迎来到 `Awesome-Multimodal-Perception` 仓库，这里收集了我在多模态感知领域学习和研究过程中遇到的一系列精彩论文。多模态感知技术是实现人工智能系统感知能力的关键，涵盖了从图像和视频分析到语音和文字理解的广泛技术。这个领域的研究有助于推动机器学习、人机交互、自然语言处理等多个方向的发展。

在这个仓库中，你将找到我认为最有影响力和最具启发性的论文列表，它们分为不同的类型，并附有论文和代码的链接，以及一些精彩的解读，希望能对你的学习和研究有所帮助。

## 📖 论文列表

| 序号 | 类型            | 论文名称                                                     | 作者                                                         | 发表单位                         | 期刊/会议           | 论文地址                              | 代码地址                                           | 我的解读                                    |
| ---- | --------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------- | ------------------- | ------------------------------------- | -------------------------------------------------- | ------------------------------------------- |
| 1    | 相机+激光雷达融合 | VirtualPainting: Addressing Sparsity with Virtual Points and Distance-Aware Data Augmentation for 3D Object Detection | Sudip Dhakal,Dominic Carrillo,Deyuan Qu,Michael Nutt,Qing Yang,Song Fu | University of North Texas Denton | 无                  | [📄](https://arxiv.org/abs/2312.16141) | [💻](https://arxiv.org/abs/2312.16141)              | [🔍](https://zhuanlan.zhihu.com/p/685337158) |
| 2    | Transformer架构 | Swin Transformer: Hierarchical Vision Transformer using Shifted Windows | Ze Liu,Yutong Lin,Yue Cao,Han Hu,Yixuan Wei,Zheng Zhang,Stephen Lin,Baining Guo | Microsoft Research Asia          | ICCV2021 Best paper | [📄](https://arxiv.org/abs/2103.14030) | [💻](https://github.com/microsoft/Swin-Transformer) | [🔍](https://zhuanlan.zhihu.com/p/685551585) |
| 3 | 3D目标检测（纯视觉） | UniMODE: Unified Monocular 3D Object Detection | Zhuoling Li, Xiaogang Xu, SerNam Lim, Hengshuang Zhao | The University of Hong Kong、Zhejiang University、University of Central Florida | CVPR2024 | [📄](https://arxiv.org/abs/2402.18573) | [💻](https://arxiv.org/abs/2402.18573) | [🔍](https://zhuanlan.zhihu.com/p/686228362) |
| 4 | 相机+激光雷达融合 | DeepFusion: Lidar-Camera Deep Fusion for Multi-Modal 3D Object Detection | Yingwei Li, Adams Wei Yu, Tianjian Meng, Ben Caine, Jiquan Ngiam, Daiyi Peng, Junyang Shen, Bo Wu, Yifeng Lu, Denny Zhou, Quoc V. Le, Alan Yuille, Mingxing Tan | Johns Hopkins University、Google | CVPR2022 | [📄](https://arxiv.org/abs/2203.08195v1) | [💻](https://github.com/tensorflow/lingvo/blob/master/lingvo/tasks/car/deep_fusion.py) | [🔍](https://zhuanlan.zhihu.com/p/687676198) |
| 5 | 3D目标检(纯视觉) | Enhancing 3D Object Detection with 2D Detection-Guided Query Anchors | Haoxuanye Ji,Pengpeng Liang,Erkang Cheng | 郑州大学、Nullmax | CVPR2024 | [📄](https://arxiv.org/abs/2403.06093) | [💻](https://arxiv.org/abs/2403.06093) | [🔍](https://zhuanlan.zhihu.com/p/688934983) |
| 6 | 3D目标检(纯视觉) | Object as Query: Lifting any 2D Object Detector to 3D Detection | Zitian Wang,Zehao Huang,Jiahui Fu,Naiyan Wang,Si Liu | 北京航空航天大学人工智能研究院、图森未来 | ICCV2023 | [📄](https://arxiv.org/abs/2301.02364) | [💻](https://github.com/tusen-ai/MV2D?tab=readme-ov-file) | [🔍](https://zhuanlan.zhihu.com/p/690036659) |
| 7 | 3D目标检(纯视觉) | MonoCD: Monocular 3D Object Detection with Complementary Depths | Longfei Yan, Pei Yan, Shengzhou Xiong, Xuanyu Xiang, Yihua Tan | 华中科技大学人工智能与自动化学院 | CVPR2024 | [📄](https://arxiv.org/abs/2404.03181) | [💻](https://github.com/elvintanhust/MonoCD) | [🔍](https://zhuanlan.zhihu.com/p/691322485) |
| 8 | 相机+激光雷达+雷达融合 | FUTR3D: A Unified Sensor Fusion Framework for 3D Detection | Xuanyao Chen,Tianyuan Zhang,Yue Wang,Yilun Wang,Hang Zhao | 上海期智研究院、复旦大学、CMU、清华大学、MIT、Li Auto | 无 | [📄](https://arxiv.org/abs/2203.10642) | [💻](https://github.com/Tsinghua-MARS-Lab/futr3d) | [🔍](https://zhuanlan.zhihu.com/p/692602887) |
| 9 | 相机+激光雷达融合 | BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation | Zhijian Liu, Haotian Tang, Alexander Amini, Xinyu Yang, Huizi Mao, Daniela Rus, Song Han | MIT、上海交通大学 | ICRA 2023 | [📄](https://arxiv.org/abs/2205.13542) | [💻](https://github.com/mit-han-lab/bevfusion) | [🔍](https://zhuanlan.zhihu.com/p/692741500) |
| 10 | 3D目标检测（纯视觉） | Sparse4D: Multi-view 3D Object Detection with Sparse Spatial-Temporal Fusion | Xuewu Lin, Tianwei Lin, Zixiang Pei, Lichao Huang, Zhizhong Su | 地平线 | 无 | [📄](https://arxiv.org/abs/2211.10581) | [💻](https://github.com/linxuewu/Sparse4D) | [🔍](https://zhuanlan.zhihu.com/p/693836118) |
| 11 | 相机+激光雷达融合 | SparseLIF: High-Performance Sparse LiDAR-Camera Fusion for 3D Object Detection | Hongcheng Zhang, Liu Liang, Pengxin Zeng, Xiao Song, Zhe Wang | 商汤科技、四川大学 | 无 | [📄](https://arxiv.org/abs/2403.07284) | [💻](https://arxiv.org/abs/2403.07284) | [🔍](https://zhuanlan.zhihu.com/p/695115688) |
| 12 | 3D目标检(纯视觉) | HENet: Hybrid Encoding for End-to-end Multi-task 3D Perception from Multi-view Cameras | Zhongyu Xia, ZhiWei Lin, Xinhao Wang, Yongtao Wang, Yun Xing, Shengxiang Qi, Nan Dong, Ming-Hsuan Yang | 北京大学王选所、长安汽车、加利福尼亚大学 | 无 | [📄](https://arxiv.org/abs/2404.02517) | [💻](https://github.com/VDIGPKU/HENet) | [🔍](https://zhuanlan.zhihu.com/p/696957422) |
| 13 | 相机+激光雷达融合 | Cross Modal Transformer: Towards Fast and Robust 3D Object Detection | Junjie Yan, Yingfei Liu, Jianjian Sun, Fan Jia, Shuailin Li, Tiancai Wang, Xiangyu Zhang | 旷视科技 | ICCV2023 | [📄](https://arxiv.org/abs/2301.01283) | [💻](https://github.com/junjie18/CMT) | [🔍](https://zhuanlan.zhihu.com/p/698801629) |
| 14 | 相机+激光雷达融合 | SparseFusion: Fusing Multi-Modal Sparse Representations for Multi-Sensor 3D Object Detection | Yichen Xie, Chenfeng Xu, Marie-Julie Rakotosaona, Patrick Rim, Federico Tombari, Kurt Keutzer, Masayoshi Tomizuka, Wei Zhan | 加州大学伯克利分校、Google、加州理工学院 | ICCV2023 | [📄](https://arxiv.org/abs/2304.14340) | [💻](https://github.com/yichen928/SparseFusion) | [🔍](https://zhuanlan.zhihu.com/p/699956228) |
| ...  | ...             | ...                                                          | ...                                                          | ...                              | ...                 | ...                                   | ...                                                | ...                                         |

## 🤝 如何贡献

这个项目欢迎任何形式的贡献，无论是新增论文、提供解读、添加代码链接，还是改进仓库的结构。如果你有任何想法或资源希望分享，请通过 issue 或者 pull request 的方式提交。

## 🌟 致谢

感谢所有在多模态感知领域做出贡献的研究者和开发者。你们的工作极大地推动了这个领域的进步，并为我们提供了丰富的学习资源。

---

希望这个仓库能成为你多模态感知学习和研究旅程中的宝贵资源。如果你觉得这里的内容对你有帮助，欢迎给予星标支持！
