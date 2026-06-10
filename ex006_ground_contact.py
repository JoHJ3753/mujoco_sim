# ex006_ground_contact.py

import mujoco

xml = """
<mujoco>
    <option timestep="0.01" gravity="0 0 -9.81"/>

    <worldbody>
        <geom name="ground" type="plane" size="5 5 0.1" pos="0 0 0"/>

        <body name="box_body" pos="0 0 1">
            <freejoint/>
            <geom name="box_geom" type="box" size="0.2 0.2 0.2" mass="1"/>
        </body>
    </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

for i in range(150):
    mujoco.mj_step(model, data)
    print("최종 시간:", data.time)
    print("박스 z 위치:", data.xpos[1][2])
    print("접촉 개수:", data.ncon)

print("최종 시간:", data.time)
print("박스 z 위치:", data.xpos[1][2])
print("접촉 개수:", data.ncon)