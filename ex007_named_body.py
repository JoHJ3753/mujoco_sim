# ex007_named_body.py

import mujoco

xml = """
<mujoco>
    <option timestep="0.01"/>
    <worldbody>
        <geom name="ground" type="plane" size="5 5 0.1"/>

        <body name="robot_base" pos="0 0 0.5">
            <geom name="base_geom" type="box" size="0.3 0.2 0.1" mass="2"/>
        </body>
    </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)

body_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "robot_base")
geom_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_GEOM, "base_geom")

print("robot_base body id:", body_id)
print("base_geom geom id:", geom_id)