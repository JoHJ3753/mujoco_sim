# ex039_camera_definition.py

import time
import mujoco
import mujoco.viewer
import math

L1 = 1.0
L2 = 0.8

xml = f"""
<mujoco>
    <option timestep="0.01"/>

    <worldbody>
        <body name="base" pos="0 0 0">
            <body name="link1" pos="0 0 0">
                <joint name="joint1"
                       type="hinge"
                       axis="0 0 1"
                       limited="true"
                       range="-180 180"/>

                <geom name="link1_geom"
                      type="capsule"
                      fromto="0 0 0  {L1} 0 0"
                      size="0.04"
                      mass="1"/>

                <body name="link2" pos="{L1} 0 0">
                    <joint name="joint2"
                           type="hinge"
                           axis="0 0 1"
                           limited="true"
                           range="-180 180"/>

                    <geom name="link2_geom"
                          type="capsule"
                          fromto="0 0 0  {L2} 0 0"
                          size="0.04"
                          mass="0.8"/>

                    <site name="end_site"
                          pos="{L2} 0 0"
                          size="0.05"/>
                </body>
            </body>
        </body>
    </worldbody>

    <actuator>
        <position name="joint1_servo"
                  joint="joint1"
                  kp="2"
                  ctrlrange="-3.14 3.14"
                  ctrllimited="true"/>

        <position name="joint2_servo"
                  joint="joint2"
                  kp="5"
                  ctrlrange="-3.14 3.14"
                  ctrllimited="true"/>
    </actuator>

    <sensor>
        <framepos name="end_pos"
                  objtype="site"
                  objname="end_site"/>
    </sensor>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

theta1 = math.radians(30)
theta2 = math.radians(45)

data.ctrl[0] = theta1
data.ctrl[1] = theta2

with mujoco.viewer.launch_passive(model, data) as viewer:
    #while viewer.is_running():
    cnt = 0
    while cnt < 500:
        mujoco.mj_step(model, data)
        viewer.sync()
        time.sleep(model.opt.timestep)
        cnt += 1