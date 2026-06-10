# ex002_minimal_world.py

import mujoco

xml = """
<mujoco>
    <worldbody>
    </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

print("모델 생성 성공")
print("nbody:", model.nbody)
print("ngeom:", model.ngeom)