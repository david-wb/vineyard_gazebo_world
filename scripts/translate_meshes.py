import trimesh
import os
import glob

# Directory containing the models
models_dir = "./models"

# Find all .obj files in ./models/... recursively
obj_files = glob.glob(os.path.join(models_dir, "**", "map_*.obj"), recursive=True)

for obj_file in obj_files:
    print(f"Processing {obj_file}...")
    
    # Load the mesh
    mesh = trimesh.load(obj_file)
    
    # Apply translation: move down by 150.0 units along z-axis
    translation = [0, 0, 5.0]
    mesh.apply_translation(translation)
    
    # Save the modified mesh, overwriting the original file
    mesh.export(obj_file)
    print(f"Modified {obj_file} (shifted z)")

print("All .obj files processed.")