# ex008_hinge_joint.py

import mujoco

xml = """
<mujoco>
    <option timestep="0.01"/>

    <worldbody>
        <body name="link1" pos="0 0 0">
            <joint name="joint1" type="hinge" axis="0 0 1" limited="true" range="-90 90"/>
            <geom name="link1_geom" type="capsule" fromto="0 0 0  1 0 0" size="0.05" mass="1"/>
        </body>
    </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

joint_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, "joint1")

print("joint1 id:", joint_id)
print("nq:", model.nq)
print("nv:", model.nv)
print("초기 qpos:", data.qpos[:])