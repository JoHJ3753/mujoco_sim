# ex018_bouncing_ball.py

import mujoco

xml = """
<mujoco>
    <option timestep="0.005" gravity="0 0 -9.81"/>

    <worldbody>
        <geom name="ground"
              type="plane"
              size="5 5 0.1"
              solref="0.01 1"
              solimp="0.9 0.95 0.001"/>

        <body name="ball_body" pos="0 0 2">
            <freejoint/>
            <geom name="ball_geom"
                  type="sphere"
                  size="0.2"
                  mass="1"
                  solref="0.01 1"
                  solimp="0.9 0.95 0.001"/>
        </body>
    </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

ball_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "ball_body")

for i in range(400):
    mujoco.mj_step(model, data)

    if i % 20 == 0:
        print(f"time={data.time:.2f}, ball_z={data.xpos[ball_id][2]:.4f}")