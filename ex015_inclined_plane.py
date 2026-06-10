# ex015_inclined_plane.py

import mujoco
import math
import mujoco.viewer
import time

angle_deg = 20
angle_rad = math.radians(angle_deg)

xml = f"""
<mujoco>
    <option timestep="0.01" gravity="0 0 -9.81"/>

    <worldbody>
    <light name="top_light" pos="0 0 4"/>
        <geom name="slope"
              type="box"
              size="3 1 0.05"
              pos="0 0 0"
              euler="0 {angle_deg} 0"
              friction="0.3 0.01 0.001"/>

        <body name="box_body" pos="-1 0 0.6">
            <freejoint/>
            <geom name="box_geom"
                  type="box"
                  size="0.2 0.2 0.2"
                  mass="1"
                  friction="0.3 0.01 0.001"/>
        </body>
    </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

box_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "box_body")



#for i in range(300):
with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)
        viewer.sync()
        time.sleep(model.opt.timestep)
        mujoco.mj_step(model, data)
        #print("박스 위치:", data.xpos[box_id])
        time.sleep(0.01)


print("경사각:", angle_deg)
print("박스 위치:", data.xpos[box_id])