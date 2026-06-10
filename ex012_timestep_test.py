# ex012_timestep_test.py

import mujoco

def run_simulation(timestep):
    xml = f"""
    <mujoco>
        <option timestep="{timestep}" gravity="0 0 -9.81"/>

        <worldbody>
            <geom name="ground" type="plane" size="5 5 0.1"/>

            <body name="box_body" pos="0 0 2">
                <freejoint/>
                <geom name="box_geom" type="box" size="0.2 0.2 0.2" mass="1"/>
            </body>
        </worldbody>
    </mujoco>
    """

    model = mujoco.MjModel.from_xml_string(xml)
    data = mujoco.MjData(model)

    box_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "box_body")

    for i in range(100):
        mujoco.mj_step(model, data)

    return data.time, data.xpos[box_id][2]


for timestep in [0.001, 0.005, 0.01, 0.02]:
    sim_time, box_z = run_simulation(timestep)
    print(f"timestep={timestep}, time={sim_time:.3f}, box_z={box_z:.4f}")