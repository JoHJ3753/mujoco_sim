# ex025_position_actuator.py

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
        <position name="pos_servo"
                  joint="joint1"
                  kp="10"
                  ctrlrange="-3.14 3.14"
                  ctrllimited="true"/>
    </actuator>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

target_angle = math.radians(45)
data.ctrl[0] = target_angle

for i in range(200):
    mujoco.mj_step(model, data)
    #print("목표 각도 rad:", target_angle)
    print("목표 각도 deg:", math.degrees(target_angle))
    #print("현재 qpos rad:", data.qpos[0])
    print("현재 qpos deg:", math.degrees(data.qpos[0]))

print("목표 각도 rad:", target_angle)
print("현재 qpos rad:", data.qpos[0])
print("현재 qpos deg:", math.degrees(data.qpos[0]))