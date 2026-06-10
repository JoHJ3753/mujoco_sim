# ex005_free_falling_box.py

import mujoco

xml = """
<mujoco>
    <option timestep="0.01" gravity="0 0 -9.81"/>

    <worldbody>
        <body name="box_body" pos="0 0 1">
            <freejoint/>
            <geom name="box_geom" type="box" size="0.2 0.2 0.2" mass="1"/>
        </body>
    </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

for i in range(100):
    mujoco.mj_step(model, data)
    print(f"time={data.time:.2f}, z={data.xpos[1][2]:.4f}")