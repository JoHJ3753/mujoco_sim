# ex029_sine_position_control.py

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
                  kp="30"
                  ctrlrange="-3.14 3.14"
                  ctrllimited="true"/>
    </actuator>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

amplitude = math.radians(45)
frequency = 0.5

for i in range(500):
    target = amplitude * math.sin(2 * math.pi * frequency * data.time)

    data.ctrl[0] = target

    mujoco.mj_step(model, data)

    if i % 50 == 0:
        print(
            f"time={data.time:.2f}, "
            f"target={math.degrees(target):.2f}, "
            f"qpos={math.degrees(data.qpos[0]):.2f}"
        )