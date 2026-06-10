# ex014_friction_test.py

import mujoco

xml = """
<mujoco>
    <option timestep="0.01" gravity="0 0 -9.81"/>

    <worldbody>
        <geom name="ground" type="plane" size="10 10 0.1" friction="0.1 0.005 0.0001"/>

        <body name="box_body" pos="0 0 0.3">
            <freejoint/>
            <geom name="box_geom" type="box" size="0.2 0.2 0.2" mass="1" friction="0.1 0.005 0.0001"/>
        </body>
    </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

box_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "box_body")

# x방향 초기 속도 부여
data.qvel[0] = 2.0

for i in range(200):
    mujoco.mj_step(model, data)

print("박스 x 위치:", data.xpos[box_id][0])
print("박스 속도 qvel:", data.qvel[:])