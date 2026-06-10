# ex010_simple_viewer.py

import time
import mujoco
import mujoco.viewer

xml = """
<mujoco>
    <option timestep="0.01" gravity="0 0 -9.81"/>

    <worldbody>
        <light name="top_light" pos="0 0 3"/>
        <geom name="ground" type="plane" size="5 5 0.1"/>

        <body name="box_body" pos="0 0 1">
            <freejoint/>
            <geom name="box_geom" type="box" size="0.2 0.2 0.2" mass="1"/>
        </body>
    </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)
        viewer.sync()
        time.sleep(model.opt.timestep)