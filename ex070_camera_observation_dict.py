# ex070_camera_observation_dict.py

import mujoco
import numpy as np

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

renderer = mujoco.Renderer(model, height=120, width=160)

mujoco.mj_forward(model, data)

renderer.disable_depth_rendering()
renderer.update_scene(data, camera="front_camera")
rgb = renderer.render()

rgb_float = rgb.astype(np.float32) / 255.0

observation = {
    "qpos": data.qpos.copy(),
    "qvel": data.qvel.copy(),
    "rgb": rgb_float
}

print("qpos shape:", observation["qpos"].shape)
print("qvel shape:", observation["qvel"].shape)
print("rgb shape:", observation["rgb"].shape)
print("rgb min:", observation["rgb"].min())
print("rgb max:", observation["rgb"].max())