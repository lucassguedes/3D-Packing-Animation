import bpy


container_side= 3
number_of_boxes = 15

#boxes_dimensions = [[3, 1, 1],
#                    [3, 1, 1],
#                    [3, 1, 1],
#                    [1, 1, 1],
#                    [1, 1, 1],
#                    [1, 1, 1],
#                    [1, 1, 1],
#                    [1, 1, 1],
#                    [1, 1, 1],
#                    [2, 1, 1],
#                    [2, 1, 1],
#                    [2, 1, 1],
#                    [2, 1, 1],
#                    [2, 1, 1],
#                    [2, 1, 1]]
#                    
#boxes_positions = [[0, 2, 0],
#                   [0, 1, 1],
#                   [0, 1, 2],
#                   [0, 0, 1],
#                   [2, 0, 2],
#                   [2, 0, 0],
#                   [2, 1, 0],
#                   [2, 2, 1],
#                   [0, 2, 2],
#                   [1, 0, 1],
#                   [0, 0, 0],
#                   [1, 2, 2],
#                   [0, 1, 0],
#                   [0, 0, 2],
#                   [0, 2, 1]]       
                   
                   
#boxes_dimensions = [[1.0, 3.0, 1.0],
#                    [1.0, 3.0, 1.0],
#                    [1.0, 3.0, 1.0],
#                    [1.0, 1.0, 1.0],
#                    [1.0, 1.0, 1.0],
#                    [1.0, 1.0, 1.0],
#                    [1.0, 1.0, 1.0],
#                    [1.0, 1.0, 1.0],
#                    [1.0, 1.0, 1.0],
#                    [1.0, 2.0, 1.0],
#                    [1.0, 2.0, 1.0],
#                    [1.0, 1.0, 2.0],
#                    [1.0, 1.0, 2.0],
#                    [1.0, 1.0, 2.0],
#                    [1.0, 1.0, 2.0]]
#                    
#                    
#boxes_positions = [[2.0, 0.0, 1.0],
#                   [1.0, 0.0, 0.0],
#                   [2.0, 0.0, 0.0],
#                   [1.0, 0.0, 1.0],
#                   [0.0, 0.0, 1.0],
#                   [0.0, 0.0, 0.0],
#                   [2.0, 0.0, 2.0],
#                   [1.0, 0.0, 2.0],
#                   [0.0, 0.0, 2.0],
#                   [2.0, 1.0, 2.0],
#                   [0.0, 1.0, 0.0],
#                   [1.0, 1.0, 1.0],
#                   [1.0, 2.0, 1.0],
#                   [0.0, 1.0, 1.0],
#                   [0.0, 2.0, 1.0]]

#boxes_dimensions = [[1.0, 1.0, 3.0],
#                    [1.0, 3.0, 1.0],
#                    [1.0, 1.0, 3.0],
#                    [1.0, 1.0, 1.0],
#                    [1.0, 1.0, 1.0],
#                    [1.0, 1.0, 1.0],
#                    [1.0, 1.0, 1.0],
#                    [1.0, 1.0, 1.0],
#                    [1.0, 1.0, 1.0],
#                    [1.0, 2.0, 1.0],
#                    [1.0, 1.0, 2.0],
#                    [1.0, 1.0, 2.0],
#                    [1.0, 1.0, 2.0],
#                    [1.0, 1.0, 2.0],
#                    [1.0, 1.0, 2.0]]
#                    
#                         
#                    
#boxes_positions = [[0.0, 2.0, 0.0],
#                   [2.0, 0.0, 0.0],
#                   [0.0, 0.0, 0.0],
#                   [0.0, 1.0, 0.0],
#                   [1.0, 0.0, 0.0],
#                   [2.0, 0.0, 2.0],
#                   [1.0, 0.0, 1.0],
#                   [1.0, 0.0, 2.0],
#                   [2.0, 0.0, 1.0],
#                   [1.0, 1.0, 0.0],
#                   [0.0, 1.0, 1.0],
#                   [1.0, 1.0, 1.0],
#                   [1.0, 2.0, 1.0],
#                   [2.0, 2.0, 1.0],
#                   [2.0, 1.0, 1.0]]    

boxes_dimensions = [[1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0],
                    [1.0, 2.0, 5.0],
                    [5.0, 1.0, 2.0],
                    [1.0, 2.0, 5.0],
                    [2.0, 5.0, 1.0],
                    [2.0, 5.0, 1.0],
                    [5.0, 1.0, 2.0],
                    [2.0, 4.0, 2.0],
                    [4.0, 2.0, 2.0],
                    [2.0, 2.0, 4.0],
                    [4.0, 2.0, 2.0],
                    [2.0, 4.0, 2.0],
                    [2.0, 2.0, 4.0]]
                                 

boxes_positions = [[5.0, 0.0, 0.0],
                   [1.0, 4.0, 4.0],
                   [0.0, 5.0, 5.0],
                   [2.0, 2.0, 2.0],
                   [4.0, 1.0, 1.0],
                   [5.0, 1.0, 0.0],
                   [1.0, 4.0, 5.0],
                   [0.0, 0.0, 4.0],
                   [0.0, 5.0, 0.0],
                   [4.0, 0.0, 1.0],
                   [0.0, 0.0, 0.0],
                   [4.0, 1.0, 2.0],
                   [0.0, 0.0, 1.0],
                   [1.0, 0.0, 4.0],
                   [3.0, 4.0, 2.0],
                   [0.0, 3.0, 0.0],
                   [3.0, 2.0, 0.0]]
                   
                          

#bpy.ops.mesh.primitive_cube_add(scale=(container_side, container_side, container_side), location=(container_side, container_side, container_side))


for i in range(number_of_boxes):
    box_location = [2*boxes_positions[i][0], 2*boxes_positions[i][1], 2*boxes_positions[i][2]]

    box_location[0] += boxes_dimensions[i][0]
    box_location[1] += boxes_dimensions[i][1]
    box_location[2] += boxes_dimensions[i][2]

    bpy.ops.mesh.primitive_cube_add(scale=boxes_dimensions[i],location=box_location)
    bpy.context.active_object.name = f"item_{i+1}"