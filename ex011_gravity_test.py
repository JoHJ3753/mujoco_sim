# ex011_gravity_test.py

import mujoco

xml = """
<mujoco>
    <option timestep="0.01" gravity="0 0 -9.81"/>

    <worldbody>
        <geom name="ground" type="plane" size="5 5 0.1"/>

        <body name="box_body" pos="0 0 2">
            <freejoint/>
            <geom name="box_geom" type="box" size="0.2 0.2 0.2" mass="1"/>
        </body>
    </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

box_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "box_body")

for i in range(100):
    mujoco.mj_step(model, data)

print("시뮬레이션 시간:", data.time)
print("박스 z 위치:", data.xpos[box_id][2])