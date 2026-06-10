# ex044_forward_kinematics_check.py

import mujoco
import math
import mujoco.viewer
import time

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
                  kp="50"
                  ctrlrange="-3.14 3.14"
                  ctrllimited="true"/>

        <position name="joint2_servo"
                  joint="joint2"
                  kp="50"
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

with mujoco.viewer.launch_passive(model, data) as viewer:
    viewer.sync()
    while viewer.is_running():
        mujoco.mj_step(model, data)
        viewer.sync()
        time.sleep(model.opt.timestep)

theta1 = math.radians(30)
theta2 = math.radians(45)

data.ctrl[0] = theta1
data.ctrl[1] = theta2

for i in range(500):
    mujoco.mj_step(model, data)

q1 = data.qpos[0]
q2 = data.qpos[1]

fk_x = L1 * math.cos(q1) + L2 * math.cos(q1 + q2)
fk_y = L1 * math.sin(q1) + L2 * math.sin(q1 + q2)

mujoco_end = data.sensordata[:]

print("MuJoCo end position:", mujoco_end)
print("FK calculated x:", fk_x)
print("FK calculated y:", fk_y)
print("error x:", mujoco_end[0] - fk_x)
print("error y:", mujoco_end[1] - fk_y)