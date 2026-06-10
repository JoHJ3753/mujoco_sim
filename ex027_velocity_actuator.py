# ex027_velocity_actuator.py

import mujoco
import math

xml = """
<mujoco>
    <option timestep="0.01" integrator="implicitfast"/>

    <worldbody>
        <body name="wheel" pos="0 0 0">
            <joint name="wheel_joint"
                   type="hinge"
                   axis="0 0 1"/>

            <geom name="wheel_geom"
                  type="cylinder"
                  size="0.3 0.05"
                  mass="1"/>
        </body>
    </worldbody>

    <actuator>
        <velocity name="wheel_velocity_servo"
                  joint="wheel_joint"
                  kv="100"
                  ctrlrange="-10 10"
                  ctrllimited="true"/>
    </actuator>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

data.ctrl[0] = 3.0

for i in range(5):
    mujoco.mj_step(model, data)

print("목표 속도:", data.ctrl[0])
print("현재 qvel rad/s:", data.qvel[0])
print("현재 qvel deg/s:", math.degrees(data.qvel[0]))