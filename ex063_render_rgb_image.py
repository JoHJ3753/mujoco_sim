# ex063_render_rgb_image.py

import mujoco

xml = """
<mujoco>
    <option timestep="0.01"/>

    <worldbody>
        <light name="top_light" pos="0 0 4"/>

        <camera name="front_camera"
                pos="2 -3 2"
                xyaxes="1 0 0  0 0 1"/>

        <geom name="ground"
              type="plane"
              size="5 5 0.1"
              rgba="0.8 0.8 0.8 1"/>

        <body name="box_body" pos="0 0 0.3">
            <geom name="box_geom"
                  type="box"
                  size="0.3 0.3 0.3"
                  mass="1"
                  rgba="0.2 0.5 1 1"/>
        </body>
    </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

renderer = mujoco.Renderer(model, height=480, width=640)

mujoco.mj_forward(model, data)

renderer.update_scene(data, camera="front_camera")
image = renderer.render()

print("image type:", type(image))
print("image shape:", image.shape)
print("image dtype:", image.dtype)
print("min pixel:", image.min())
print("max pixel:", image.max())