# ex009_slide_joint.py

import mujoco

xml = """
<mujoco>
    <option timestep="0.01"/>

    <worldbody>
        <body name="slider" pos="0 0 0.5">
            <joint name="slide_x" type="slide" axis="1 0 0" limited="true" range="-1 1"/>
            <geom name="slider_geom" type="box" size="0.1 0.1 0.1" mass="1"/>
        </body>
    </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

joint_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, "slide_x")

print("slide_x joint id:", joint_id)
print("qpos:", data.qpos[:])
print("qvel:", data.qvel[:])