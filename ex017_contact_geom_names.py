# ex017_contact_geom_names.py

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

for i in range(200):
    mujoco.mj_step(model, data)

    for c in range(data.ncon):
        contact = data.contact[c]

        geom1_id = contact.geom1
        geom2_id = contact.geom2

        geom1_name = mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_GEOM, geom1_id)
        geom2_name = mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_GEOM, geom2_id)

        print(f"time={data.time:.2f}, contact: {geom1_name} <-> {geom2_name}")