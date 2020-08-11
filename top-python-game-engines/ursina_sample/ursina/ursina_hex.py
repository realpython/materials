from ursina import *
from copy import copy


class MinecraftClone(Entity):

    def __init__(self):
        super().__init__()
        c = Cylinder(6, height=1, start=-.5)

        verts = c.vertices
        tris = c.triangles
        vertices = list()
        triangles = list()
        colors = list()

        # for z in range(16):
        #     # for x in range(4):
        #     # triangles += [(t[0]+(i*len(triangles)), t[1]+(i*len(triangles)), t[2]+(i*len(triangles))) for t in tris]
        #     vertices += [Vec3(v) + Vec3(i,0,i) for v in verts]
        #     colors += (color.random_color(),) * len(verts)


        i = 0
        size = 16
        # verts = list()
        for z in range(size):
            for x in range(size):
                for y in range(1):
                    x_pos = x * .8660025
                    if z%2 == 0:
                        x_pos += .5*.8660025

                    # extra_height = 0
                    # if random.random() < .2:
                    #     extra_height = random.uniform(1, 3) * .2

                    # vertices += [Vec3(v) + Vec3(x_pos,0,z*.75) + Vec3(0,extra_height,0) for v in verts]
                    # col = lerp(color.lime, color.random_color(), .2)
                    # colors += (lerp(color.yellow, color.random_color(), .2).tint(-.2), ) * len(verts)
                    #
                    # i += 1
                    voxel = Entity(
                        parent = self,
                        name = 'voxel',
                        model = copy(c),
                        origin_y = -.5,
                        double_sided = True,
                        color = lerp(lerp(color.brown, color.dark_gray, .5), color.random_color(), .1),
                        index = (x,y,z),
                        position=(x*.8660025,y,z*.75)
                        )
                    voxel.collider = MeshCollider(voxel, mesh=c, center=-voxel.origin)
                    top = Entity(parent=voxel, model=copy(c), y=1.01, scale_y=.01)
                    top.color = lerp(color.lime, color.random_color(), .2)

                    if z%2 == 0:
                        voxel.x += .5*.8660025

                    if random.random() < .2:
                        voxel.scale_y += random.uniform(1, 3) * .2


        m = Mesh(vertices, colors=colors)
        # Entity(model=m, scale=2, collider='mesh')
        sky = Sky()
        Entity(model='quad', scale=99999, color=color.azure.tint(-.1), rotation_x=90)
        player = FirstPersonController()


class Magician(Entity):
    def update(self):
        # print(mo)
        if mouse.left and mouse.hovered_entity:
            mouse.hovered_entity.scale_y += 1.5 * time.dt
        if mouse.right and mouse.hovered_entity:
            mouse.hovered_entity.scale_y -= 1.5 * time.dt
Magician()

class FirstPersonController(Entity):

    def __init__(self):
        super().__init__()
        self.speed = 3

        self.i = 0
        self.update_interval = 30

        self.cursor = Entity(
            parent = camera.ui,
            model = 'quad',
            color = color.pink,
            scale = .008,
            rotation_z = 45
            )

        self.graphics = Entity(
            name = 'player_graphics',
            parent = self,
            model = 'cube',
            origin = (0, -.5, 0),
            scale = (1, 1.8, 1),
            )

        self.arrow = Entity(
            parent = self.graphics,
            model = 'cube',
            color = color.blue,
            position = (0, .5, .5),
            scale = (.1, .1, .5)
            )

        camera.parent = self
        self.position = (0, 1, 1)
        camera.rotation = (0,0,0)
        camera.position = (0,1.5,0)
        camera.fov = 90
        mouse.locked = True


    def update(self):
        if self.i < self.update_interval:
            self.i += 1
            return

        self.direction = (
            self.forward * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a'])
            )

        if not raycast(self.world_position + self.up, self.direction, .5).hit:
            self.position += self.direction * self.speed * time.dt

        self.rotation_y += mouse.velocity[0] * 40
        camera.rotation_x -= mouse.velocity[1] * 40
        camera.rotation_x = clamp(camera.rotation_x, -90, 90)

        self.y += held_keys['e']
        self.y -= held_keys['q']


if __name__ == '__main__':
    app = Ursina()
    # window.size = (450, (450/window.aspect_ratio))
    # window.center_on_screen()
    MinecraftClone()
    # vr = VideoRecorder(name='minecraft_clone', duration=6)
    # invoke(setattr, vr, 'recording', True, delay=2)
    app.run()