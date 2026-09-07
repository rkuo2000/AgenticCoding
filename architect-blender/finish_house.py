def uv(name,loc,scale,material,segments=16,rings=8):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments,ring_count=rings,location=loc); o=bpy.context.object; o.name=name; o.scale=scale; o.data.materials.append(material)
    for p in o.data.polygons: p.use_smooth=True
    return o
def cyl(name,a,b,r,material,vertices=12):
    a,b=Vector(a),Vector(b); bpy.ops.mesh.primitive_cylinder_add(vertices=vertices,radius=r,depth=(b-a).length,location=(a+b)/2); o=bpy.context.object; o.name=name; o.rotation_euler=(b-a).to_track_quat('Z','Y').to_euler(); o.data.materials.append(material); return o
# Two stylized architectural entourage cars, facing the driveway.
def car(x,y):
    box('Car lower body',(x,y,.64),(1.75,3.75,.55),carpaint,.23)
    box('Car hood',(x,y-1.2,.92),(1.67,1.19,.19),carpaint,.13)
    verts=[(x+dx,y+dy,z) for dx,dy,z in [(-.76,-.68,.86),(.76,-.68,.86),(.76,1.25,.86),(-.76,1.25,.86),(-.61,-.29,1.48),(.61,-.29,1.48),(.61,.77,1.48),(-.61,.77,1.48)]]
    mesh('Car panoramic glazing',verts,[(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7),(4,5,6,7)],glass)
    box('Car roof',(x,y+.24,1.49),(1.26,1.13,.08),carpaint,.09)
    for i,j in [(0,4),(1,5),(2,6),(3,7)]: beam('Car window pillar',verts[i],verts[j],.07,carpaint)
    for xx in [x-.765,x+.765]: beam('Car B pillar',(xx,y+.3,.91),(x+(.615 if xx>x else -.615),y+.3,1.48),.055,dark)
    for xx in [x-.86,x+.86]:
        for yy in [y-1.15,y+1.15]:
            cyl('Car tire',(xx-.105,yy,.47),(xx+.105,yy,.47),.35,rubber,24)
            outer=xx+(.115 if xx>x else -.115)
            cyl('Alloy wheel',(outer-.01,yy,.47),(outer+.01,yy,.47),.235,chrome,24)
            for t in range(5):
                a=t*math.tau/5; beam('Wheel spoke',(outer,yy,.47),(outer,yy+.20*math.cos(a),.47+.20*math.sin(a)),.04,dark)
    box('Front grille',(x,y-1.88,.64),(.91,.035,.21),dark,.055)
    for xx in [x-.62,x+.62]: box('Headlight',(xx,y-1.87,.85),(.37,.048,.13),lamp,.045)
    box('Lower air intake',(x,y-1.88,.40),(1.26,.035,.10),dark,.035)
    box('Front plate',(x,y-1.914,.55),(.32,.014,.08),white,.009)
    for xx in [x-.95,x+.95]: uv('Wing mirror',(xx,y-.38,1.04),(.13,.17,.075),carpaint)
car(-5.45,1.05); car(-2.88,1.12)
# Rounded landscape island with rocks and slender tropical trees.
bpy.ops.mesh.primitive_cylinder_add(vertices=64,radius=1,depth=.09,location=(5.3,-3.75,.04)); o=bpy.context.object; o.name='Oval garden white edging'; o.scale=(1.47,.91,1); o.data.materials.append(white)
bpy.ops.mesh.primitive_cylinder_add(vertices=64,radius=1,depth=.09,location=(5.3,-3.75,.082)); o=bpy.context.object; o.name='Oval garden soil'; o.scale=(1.37,.81,1); o.data.materials.append(soil)
for i in range(10):
    a=random.uniform(0,math.tau); r=random.uniform(.3,1)
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2,radius=1,location=(5.3+math.cos(a)*r,-3.75+math.sin(a)*r*.56,.20)); o=bpy.context.object; o.name='Landscape boulder'; o.scale=(random.uniform(.2,.43),random.uniform(.2,.35),random.uniform(.18,.34)); o.data.materials.append(rock)
def tropical(x,y,h):
    cyl('Palm trunk',(x,y,.1),(x+.16,y,h),.055,wood)
    for j in range(9):
        a=j*math.tau/9+random.random()*.3; start=Vector((x+.16,y,h)); end=start+Vector((math.cos(a)*.87,math.sin(a)*.87,random.uniform(-.45,.22)))
        cyl('Palm frond rib',start,end,.012,leafm[0],6)
        for k in range(1,8):
            t=k/8; center=start.lerp(end,t); side=Vector((-math.sin(a),math.cos(a),-.25))*(.21*math.sin(t*math.pi))
            for sign in [-1,1]:
                tip=center+side*sign+Vector((math.cos(a),math.sin(a),-.22))*.19
                mesh('Palm leaflet',[tuple(center),tuple(center+Vector((math.cos(a),math.sin(a),0))*.15),tuple(tip)],[(0,1,2)],random.choice(leafm))
for dx,dy,h in [(-.5,.1,2.6),(.5,.1,3.05),(.05,-.2,2.15)]: tropical(5.3+dx,-3.75+dy,h)
def tree(x,y,h):
    cyl('Background tree trunk',(x,y,0),(x,y,h*.8),.12,wood)
    for i in range(20):
        a=random.random()*math.tau; r=random.uniform(.2,1.55); z=random.uniform(h*.55,h)
        pos=(x+math.cos(a)*r,y+math.sin(a)*r,z)
        if i<7: cyl('Tree branch',(x,y,h*.4),pos,.045,wood,8)
        uv('Tree foliage',pos,(random.uniform(.55,1),random.uniform(.6,1.1),random.uniform(.38,.75)),random.choice(leafm),12,6)
for x,y,h in [(-9,6,5.5),(-6.8,9,6),(-2,10,5.7),(8.8,7.2,6),(11,9,5.3)]: tree(x,y,h)
box('Rear boundary wall',(0,10,.68),(27,.18,1.4),white,.025)
# Interior hints visible through the windows.
interior=mat('Interior warm plaster',(.65,.59,.48),.9)
for z in [.44,3.29]:
    box('Interior room partition',(2.7,3,z+1.2),(.13,5.8,2.4),interior)
    box('Interior rear lining',(2.7,5.82,z+1.2),(6.8,.08,2.4),interior)
    box('Lounge sofa',(4.5,2.5,z+.4),(1.9,.82,.65),white,.12)
    box('Sofa back',(4.5,2.82,z+.7),(1.9,.2,.7),white,.08)
    box('Coffee table',(4.5,1.35,z+.3),(1.15,.65,.10),wood,.035)
    for x in [4.05,4.95]: box('Table leg',(x,1.35,z+.15),(.04,.43,.3),dark)
# Procedural microtexture for the lawn and stucco.
for material,scale,strength in [(grass,130,.18),(wall,90,.08),(white,100,.06),(concrete,45,.12),(wood,7,.13)]:
    nt=material.node_tree; p=nt.nodes.get('Principled BSDF'); noise=nt.nodes.new('ShaderNodeTexNoise'); noise.inputs['Scale'].default_value=scale
    bump=nt.nodes.new('ShaderNodeBump'); bump.inputs['Strength'].default_value=strength; bump.inputs['Distance'].default_value=.045
    nt.links.new(noise.outputs['Fac'],bump.inputs['Height']); nt.links.new(bump.outputs['Normal'],p.inputs['Normal'])
    if material==grass:
        ramp=nt.nodes.new('ShaderNodeValToRGB'); ramp.color_ramp.elements[0].color=(.065,.13,.018,1); ramp.color_ramp.elements[1].color=(.25,.37,.07,1); nt.links.new(noise.outputs['Fac'],ramp.inputs[0]); nt.links.new(ramp.outputs[0],p.inputs['Base Color'])
world=bpy.data.worlds.new('Clear blue daylight'); scene.world=world; world.use_nodes=True; world.node_tree.nodes['Background'].inputs[0].default_value=(.44,.64,.85,1); world.node_tree.nodes['Background'].inputs[1].default_value=.45
bpy.ops.object.light_add(type='SUN',location=(-8,-10,12)); sun=bpy.context.object; sun.name='Afternoon sun'; sun.rotation_euler=(math.radians(27),math.radians(-25),math.radians(-28)); sun.data.energy=2.7; sun.data.angle=.09
bpy.ops.object.light_add(type='AREA',location=(1,-8,9)); o=bpy.context.object; o.name='Soft sky fill'; o.data.energy=1000; o.data.shape='DISK'; o.data.size=10; o.rotation_euler=(Vector((0,1,3))-o.location).to_track_quat('-Z','Y').to_euler()
bpy.ops.object.camera_add(location=(.1,-24.5,6.3)); camera=bpy.context.object; camera.name='Reference facade camera'; camera.rotation_euler=(Vector((0,1,3.3))-camera.location).to_track_quat('-Z','Y').to_euler(); camera.data.lens=37; scene.camera=camera
scene.render.engine='CYCLES'; scene.cycles.samples=48; scene.cycles.use_denoising=True
scene.render.resolution_x=1600; scene.render.resolution_y=1000; scene.render.resolution_percentage=100
scene.view_settings.view_transform='AgX'
scene.render.image_settings.file_format='PNG'; scene.render.filepath='/home/rkuo/AgenticCoding/architect-blender/Simple-House-Render.png'
scene['Reference']='Simple-House-Design.webp'; scene['Notes']='Exterior reconstruction from a single reference. Dimensions and unseen elevations are estimated.'
for area in bpy.context.screen.areas:
    if area.type=='VIEW_3D':
        area.spaces.active.region_3d.view_perspective='CAMERA'
bpy.ops.wm.save_as_mainfile(filepath='/home/rkuo/AgenticCoding/architect-blender/Simple-House.blend')
print('Saved scene with',len(scene.objects),'objects')
