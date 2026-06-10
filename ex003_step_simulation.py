# ex003_step_simulation.py

import mujoco

xml = """
<mujoco>
    <option timestep="0.01"/>
    <worldbody>
    </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

print("초기 시간:", data.time)

mujoco.mj_step(model, data)

print("1스텝 후 시간:", data.time)

for i in range(10):
    mujoco.mj_step(model, data)

print("11스텝 후 시간:", data.time)