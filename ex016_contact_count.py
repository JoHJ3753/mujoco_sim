# ex016_contact_count.py

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

for i in range(200):
    mujoco.mj_step(model, data)

    #if data.ncon > 0:
    print(f"step={i}, time={data.time:.2f}, z={data.xpos[box_id][2]:.4f}, contacts={data.ncon}")