# ex068_render_depth_image.py

import mujoco
import numpy as np
from PIL import Image

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

        <body name="near_box" pos="-0.4 0 0.3">
            <geom name="near_geom"
                  type="box"
                  size="0.2 0.2 0.2"
                  mass="1"
                  rgba="1 0.2 0.2 1"/>
        </body>

        <body name="far_box" pos="0.8 0.8 0.3">
            <geom name="far_geom"
                  type="box"
                  size="0.2 0.2 0.2"
                  mass="1"
                  rgba="0.2 0.2 1 1"/>
        </body>
    </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

renderer = mujoco.Renderer(model, height=480, width=640)

mujoco.mj_forward(model, data)

renderer.enable_depth_rendering()
renderer.update_scene(data, camera="front_camera")

depth = renderer.render()

print("depth type:", type(depth))
print("depth shape:", depth.shape)
print("depth dtype:", depth.dtype)
print("depth min:", np.min(depth))
print("depth max:", np.max(depth))

depth_normalized = depth.copy()
depth_normalized = depth_normalized - np.min(depth_normalized)
depth_normalized = depth_normalized / (np.max(depth_normalized) + 1e-8)
depth_uint8 = (depth_normalized * 255).astype(np.uint8)

Image.fromarray(depth_uint8).save("depth_image.png")

print("saved: depth_image.png")