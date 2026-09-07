import bpy, math, random
from mathutils import Vector
random.seed(24)
for ob in list(bpy.data.objects):
    if ob.name in {'Cube','Camera','Light'}: bpy.data.objects.remove(ob, do_unlink=True)
scene=bpy.context.scene
def mat(name,color,rough=.5,metal=0):
    m=bpy.data.materials.new(name); m.diffuse_color=(*color,1); m.use_nodes=True
    p=m.node_tree.nodes.get('Principled BSDF'); p.inputs['Base Color'].default_value=(*color,1); p.inputs['Roughness'].default_value=rough; p.inputs['Metallic'].default_value=metal
    return m
white=mat('Warm white stucco',(.84,.85,.81),.75)
wall=mat('Blue gray render',(.48,.59,.63),.82)
dark=mat('Anthracite powder coated metal',(.035,.049,.055),.3,.55)
glass=mat('Smoky blue glazing',(.085,.16,.20),.16,.35)
glass.node_tree.nodes.get('Principled BSDF').inputs['Transmission Weight'].default_value=.32
wood=mat('Natural teak',(.25,.13,.052),.55)
concrete=mat('Concrete paving',(.37,.39,.40),.85)
stone=mat('Dark entrance stone',(.075,.085,.09),.4)
grass=mat('Lawn',(.17,.28,.047),.95)
soil=mat('Planting soil',(.11,.072,.033),1)
leafm=[mat('Foliage '+str(i),c,.85) for i,c in enumerate([(.12,.23,.035),(.23,.36,.06),(.07,.18,.028),(.32,.40,.09)])]
rock=mat('Warm landscape rocks',(.29,.20,.13),.92)
rubber=mat('Rubber',(.013,.016,.019),.78)
carpaint=mat('Ivory automotive paint',(.86,.89,.89),.22,.3)
chrome=mat('Brushed aluminum',(.4,.44,.47),.22,.8)
lamp=mat('Warm light diffuser',(1,.79,.43),.25)
lamp.node_tree.nodes.get('Principled BSDF').inputs['Emission Color'].default_value=(1,.75,.36,1)
lamp.node_tree.nodes.get('Principled BSDF').inputs['Emission Strength'].default_value=3
def box(name,loc,size,material,bevel=0):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc); o=bpy.context.object; o.name=name; o.dimensions=size
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    o.data.materials.append(material)
    if bevel:
        m=o.modifiers.new('Soft edges','BEVEL'); m.width=bevel; m.segments=3
        o.modifiers.new('Weighted normals','WEIGHTED_NORMAL')
    return o
def beam(name,a,b,width,material):
    a,b=Vector(a),Vector(b); o=box(name,(a+b)/2,(width,width,(b-a).length),material,.012); o.rotation_euler=(b-a).to_track_quat('Z','Y').to_euler(); return o
def mesh(name,verts,faces,material):
    me=bpy.data.meshes.new(name); me.from_pydata(verts,[],faces); me.update(); o=bpy.data.objects.new(name,me); scene.collection.objects.link(o); o.data.materials.append(material); return o
def roof(name,x1,x2,z1,z2,y1=-.65,y2=6.6):
    v=[(x1,y1,z1),(x2,y1,z2),(x2,y2,z2),(x1,y2,z1)]
    o=mesh(name+' white soffit',v,[(0,1,2,3)],white); m=o.modifiers.new('Roof thickness','SOLIDIFY'); m.thickness=.23
    for a,b in [(v[0],v[1]),(v[1],v[2]),(v[2],v[3]),(v[3],v[0])]: beam(name+' dark fascia',a,b,.22,dark)
    mesh(name+' standing seam top',[(x,y,z+.025) for x,y,z in v],[(0,1,2,3)],dark)
    for i in range(int((x2-x1)/.45)+1):
        x=x1+(x2-x1)*i/max(1,int((x2-x1)/.45)); z=z1+(z2-z1)*(x-x1)/(x2-x1)
        beam(name+' roof seam',(x,y1,z+.04),(x,y2,z+.04),.018,dark)
    mesh(name+' timber front gable',[(x1+.2,.04,6.05),(x2-.2,.04,6.05),(x2-.2,.04,z2-.25),(x1+.2,.04,z1-.25)],[(0,1,2,3)],wood)
box('Lawn plot',(0,2,-.15),(28,25,.25),grass,.12)
box('Main foundation',(2.65,3,.13),(7.3,6.2,.34),concrete,.04)
box('Ground floor',(2.65,3,.32),(7.3,6.2,.17),stone)
box('Upper floor slab',(2.65,3,3.12),(7.3,6.2,.25),white)
box('Back wall',(2.65,6,3.18),(7.3,.22,5.8),wall)
for x in [-.9,6.2]: box('Side wall',(x,3,3.15),(.22,6,5.7),wall)
# Front wall built around the four full-height glazed openings.
for z in [1.73,4.63]:
    for x,w in [(-.47,.85),(2.6,1.4),(5.8,.8)]: box('Front stucco pier',(x,.08,z),(w,.22,2.72),wall)
    box('Window head',(2.65,.08,z+1.15),(7.3,.22,.43),wall)
    box('Window sill wall',(2.65,.08,z-1.3),(7.3,.22,.2),wall)
def window(name,x,z,w=2.05,h=2.22):
    y=-.075
    box(name+' glass',(x,y,z),(w,.038,h),glass)
    for xx in [x-w/2-.045,x+w/2+.045]:
        box(name+' white surround',(xx,y-.015,z),(.13,.15,h+.22),white,.012)
        box(name+' frame',(xx+(.075 if xx<x else -.075),y-.09,z),(.065,.08,h),dark,.006)
    for zz in [z-h/2,z+h/2]:
        box(name+' trim',(x,y-.025,zz),(w+.2,.15,.12),white,.009)
        box(name+' frame',(x,y-.10,zz),(w,.075,.06),dark)
    box(name+' central mullion',(x,y-.11,z),(.055,.08,h),dark)
    for xx in [x-.09,x+.09]: box(name+' handle',(xx,y-.17,z-.08),(.022,.04,.23),chrome,.01)
    box(name+' curtain left',(x-w*.38,.17,z),(.29,.035,h-.06),white)
for x in [.8,4.45]:
    window('Ground sliding doors',x,1.52)
    window('Upper sliding doors',x,4.46)
box('Facade upper horizontal frame',(2.65,-.04,6.03),(7.45,.4,.19),white)
for x in [-.96,6.25]: box('Upper corner trim',(x,-.06,4.57),(.18,.37,2.93),white)
roof('Lower offset roof',-1.45,3.65,6.9,6.9)
roof('High asymmetric roof',2.55,6.85,8.02,6.85)
# Horizontal timber courses underneath the sloping upper roof.
for z in [6.2+i*.15 for i in range(11)]:
    xmax=min(6.65,2.55+(8.02-.25-z)/((8.02-6.85)/4.3))
    if xmax>2.75: box('Timber cladding joint',((2.75+xmax)/2,-.003,z),(xmax-2.75,.012,.012),dark)
# Open double carport.
box('Carport concrete pad',(-3.98,2.08,.10),(6.15,6.65,.22),concrete,.035)
box('Carport flat canopy',(-3.95,2.2,3.16),(6.25,6.85,.35),white,.025)
for x,y in [(-6.94,-1.03),(-.94,-1.03),(-6.94,5.32),(-.94,5.32)]: box('Carport square column',(x,y,1.55),(.34,.4,3.1),white,.025)
box('Carport front portal beam',(-3.94,-1.03,3.02),(6.35,.43,.46),white,.025)
box('Driveway',(-4.05,-5.14,-.005),(6,8.5,.11),concrete,.02)
# Entrance pergola and three broad steps.
for i in range(3): box('Entrance stone step',(1.1,-.42-i*.26,.28-i*.085),(3.8,.65,.14),stone,.025)
for x in [-.75+i*.64 for i in range(7)]: box('Pergola projecting rafter',(x,-.53,3.10),(.09,1.2,.15),dark,.018)
box('Pergola front beam',(1.16,-1.08,3.04),(4,.10,.14),dark,.014)
# Balcony box frame and roofed ground-level porch.
box('Balcony floor',(4.6,-.77,3.12),(4.02,1.68,.28),white,.025)
for x in [2.67,6.52]: box('Porch portal column',(x,-1.49,1.55),(.29,.3,3.1),white,.018)
box('Porch front header',(4.6,-1.49,3),(4.13,.30,.43),white,.02)
box('Porch planting strip',(4.65,-.9,.26),(3.45,.62,.22),grass,.025)
for y in [-1.3,-.96,-.62,-.28,.06]: box('Vertical teak privacy screen',(6.29,y,1.68),(.105,.1,2.7),wood,.012)
for x in [2.77,3.95,5.23,6.43]: beam('Balcony railing post',(x,-1.46,3.28),(x,-1.46,4.2),.055,dark)
for z in [3.35,3.52,3.69,3.86,4.03,4.2]:
    beam('Balcony horizontal rail',(2.77,-1.46,z),(6.43,-1.46,z),.045,dark)
    for x in [2.77,6.43]: beam('Balcony return rail',(x,-1.46,z),(x,-.05,z),.045,dark)
for x in [2.77,6.43]: beam('Balcony rear post',(x,-.05,3.27),(x,-.05,4.2),.055,dark)
for i in range(5): box('Garden walkway',(1.17,-1.8-i*.61,.025),(2.2,.43,.09),white,.025)
for x in [-1.55,-.78,0]: box('Side stepping stone',(x,-3.64,.025),(.58,1.02,.085),concrete,.025)
for x,y in [(-6.95,-1.29),(-.94,-1.28),(2.67,-1.68),(6.52,-1.68)]:
    box('Wall sconce',(x,y,1.47),(.09,.065,.23),dark,.012)
    box('Sconce diffuser',(x,y-.012,1.6),(.075,.065,.055),lamp,.01)
for x,y in [(-7.12,-4),(-1.0,-5.8),(-1,-2.3),(2.73,-2.15)]:
    box('Garden bollard',(x,y,.19),(.09,.09,.4),dark,.015); box('Bollard lens',(x,y,.30),(.1,.1,.09),lamp,.01)
print('House architecture complete',len(scene.objects))
