import bpy
from mathutils import Vector
scene=bpy.context.scene
for o in list(scene.objects):
    if o.name.startswith(('Front stucco pier','Window head','Window sill wall')): bpy.data.objects.remove(o,do_unlink=True)
wall=bpy.data.materials.get('Blue gray render.001') or bpy.data.materials.get('Blue gray render')
def panel(name,x1,x2,z1,z2):
    bpy.ops.mesh.primitive_cube_add(size=1,location=((x1+x2)/2,.08,(z1+z2)/2)); o=bpy.context.object; o.name=name; o.dimensions=(x2-x1,.22,z2-z1); bpy.ops.object.transform_apply(location=False,rotation=False,scale=True); o.data.materials.append(wall)
for bottom,top,winbottom,wintop in [(.32,3,.41,2.63),(3.245,6.03,3.35,5.57)]:
    for a,b in [(-1.0,-.225),(1.825,3.425),(5.475,6.31)]: panel('Solid facade pier',a,b,bottom,top)
    for a,b in [(-.225,1.825),(3.425,5.475)]:
        panel('Facade lintel',a,b,wintop,top); panel('Facade sill',a,b,bottom,winbottom)
o=bpy.data.objects.get('Lower offset roof timber front gable')
for v in o.data.vertices:
    if v.co.x>2.75: v.co.x=2.75
scene.camera.location=(.1,-23.5,4.8); scene.camera.rotation_euler=(Vector((0,.5,3.65))-scene.camera.location).to_track_quat('-Z','Y').to_euler(); scene.camera.data.lens=39
scene.render.filepath='/home/rkuo/AgenticCoding/architect-blender/Simple-House-Render.png'
bpy.ops.wm.save_as_mainfile(filepath='/home/rkuo/AgenticCoding/architect-blender/Simple-House.blend')
