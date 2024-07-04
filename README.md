## CORE4D Toolkit

### File Definitions

* ```rawdata.npz```: The raw data from our data capturing system, including the BVH files of the two persons, the 6D transformations of the object, and timestamps. The frame rate is 90 FPS.

* ```person1.npz```: Our processed SMPL-X parameters of the motion of Person 1. The motion is an intermediate clip of the raw data. The frame rate of the motion is 15 FPS.

* ```person2.npz```: Our processed SMPL-X parameters of the motion of Person 2. The motion is an intermediate clip of the raw data. The frame rate of the motion is 15 FPS.

### Environment Setup

```
pip install numpy==1.24.3
pip install transforms3d==0.4.1
```

### Extract BVH from the Raw Data

To load the ```rawdata.npz```, please use ```rawdata_loader.py```.

The BVH human skeleton includes 59 joints shown in the figure ```human_bvh_skeleton.pdf```.
