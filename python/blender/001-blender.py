import bpy
import numpy as np
from math import sin, cos, radians, pi

cube_add = bpy.ops.mesh.primitive_cube_add
obj_resize = bpy.ops.transform.resize
cursor = bpy.context.scene.cursor_location

def draw_cube(color, idx, theta, radial_distance, vertical_step, scale_factor):
    x = cursor.x + radial_distance * cos(theta)
    y = cursor.y + radial_distance * sin(theta)
    z = cursor.z + vertical_step * idx
    cube_add(location=(x, y, z))
    obj_scale_factor = (1 + scale_factor) ** idx
    obj_resize(value=(obj_scale_factor, obj_scale_factor, 1))
    
    # Apply the material to the object.
    active_obj = bpy.context.selected_objects[0]
    active_obj.active_material = color

def main():
    radial_distance = 8

    x_size = 1
    y_size = 1
    z_size = 1
    scale_factor = 0.1
    vertical_step = 1

    # Place the cursor at the origin.
    # Need to understand issue with context to get this to work.
    # bpy.ops.view3d.snap_cursor_to_center()

    # Draw on Layer 0
    bpy.context.scene.layers[0] = True
    
    # Create new material for object
    new_color = bpy.data.materials.new('Some Color')
    new_color.diffuse_color = (1, 0, 1)

    for idx, theta in enumerate(np.arange(0, 2 * pi, 2 * pi / 8)):
        draw_cube(new_color, idx, theta, radial_distance, vertical_step, scale_factor)
                
if __name__ == '__main__':
    main()