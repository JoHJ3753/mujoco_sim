# ex013_mass_comparison.py

import mujoco

xml = """
<mujoco>
    <option timestep="0.01" gravity="0 0 -9.81"/>

    <worldbody>
        <geom name="ground" type="plane" size="5 5 0.1"/>

        <body name="light_box" pos="-0.5 0 2">
            <freejoint/>
            <geom name="light_geom" type="box" size="0.2 0.2 0.2" mass="0.5"/>
        </body>

        <body name="heavy_box" pos="0.5 0 2">
            <freejoint/>
            <geom name="heavy_geom" type="box" size="0.2 0.2 0.2" mass="10"/>
        </body>
    </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

light_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "light_box")
heavy_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "heavy_box")

for i in range(30):
    mujoco.mj_step(model, data)

print("light_box z:", data.xpos[light_id][2])
print("heavy_box z:", data.xpos[heavy_id][2])