import numpy as np
from transforms3d.quaternions import quat2mat
from human_skeleton import get_joint_info


rawdata = np.load("rawdata.npz", allow_pickle=True)["data"].item()
person1_bvh_data = rawdata["/joints"]
person2_bvh_data = rawdata["/joints2"]

print("Frame number of person1's raw data =", len(person1_bvh_data))
print("Frame number of person2's raw data =", len(person2_bvh_data))

joint_info = get_joint_info()

for frame_idx in range(len(person1_bvh_data)):
    
    # load the human BVH pose of frame <frame_idx> of Person 1
    bvh = person1_bvh_data[frame_idx]  # list with 59 items, representing the local translation and orientation of each joint

    print("joint number =", len(bvh))  # 59
    assert len(bvh) == 59
    
    for (relation, pose) in zip(joint_info, bvh):
        
        current_joint = relation[0]
        parent_joint = relation[1]
        
        local_translation = pose["position"] * 0.01  # cm -> m
        local_orientation = quat2mat(pose["orientation"])  # quaternion (w, x, y, z) -> rotation matrix
        local_transformation = np.eye(4)
        local_transformation[:3, :3] = local_orientation
        local_transformation[:3, 3] = local_translation
        
        print("[6D relative transformation] {} to {} =".format(current_joint, parent_joint), local_transformation)

    break
