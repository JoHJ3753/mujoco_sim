# ex031_joint_position_sensor.py

import mujoco
import math

xml = """
<mujoco>
    <option timestep="0.01"/>

    <worldbody>
        <body name="arm" pos="0 0 0">
            <joint name="joint1"
                   type="hinge"
                   axis="0 0 1"
                   limited="true"
                   range="-180 180"/>

            <geom name="link1"
                  type="capsule"
                  fromto="0 0 0  1 0 0"
                  size="0.05"
                  mass="1"/>
        </body>
    </worldbody>

    <actuator>
        <position name="joint1_servo"
                  joint="joint1"
                  kp="20"
                  ctrlrange="-3.14 3.14"
                  ctrllimited="true"/>
    </actuator>

    <sensor>
        <jointpos name="joint1_position_sensor" joint="joint1"/>
    </sensor>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

data.ctrl[0] = math.radians(45)

for i in range(200):
    mujoco.mj_step(model, data)

print("data.qpos:", data.qpos[0])
print("sensordata:", data.sensordata[0])
print("qpos degree:", math.degrees(data.qpos[0]))
print("sensor degree:", math.degrees(data.sensordata[0]))