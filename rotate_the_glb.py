import os 
import trimesh 
from scipy.spatial.transform import Rotation as R   
import numpy as np 

def rotate_one_glb_for_model_viewer(glb_path):
    mesh = trimesh.load(glb_path)
    transform_mat = np.eye(4)
    transform_mat[:3, :3] = R.from_euler('XZ', [-90, 180], degrees=True).as_matrix() 
    mesh.apply_transform(transform_mat)
    mesh.export(glb_path)
    
glb_dir = "static/3d"
glb_subset_dir = ["book", "knob", "microwave", "plate2"]
for subset in glb_subset_dir:
    
    glb_dir_path = os.path.join(glb_dir, subset)
    mesh_filenames_to_rotate = os.listdir(glb_dir_path)
    for mesh_filename in mesh_filenames_to_rotate:
        glb_path = os.path.join(glb_dir_path, mesh_filename)
        rotate_one_glb_for_model_viewer(glb_path)
    
