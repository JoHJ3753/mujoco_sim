# ex026_kp_comparison.py

import mujoco
import math

def run_position_control(kp_value):
    xml = f"""
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
                      kp="{kp_value}"
                      ctrlrange="-3.14 3.14"
                      ctrllimited="true"/>
        </actuator>
    </mujoco>
    """

    model = mujoco.MjModel.from_xml_string(xml)
    data = mujoco.MjData(model)

    data.ctrl[0] = math.radians(90)

    for i in range(200):
        mujoco.mj_step(model, data)

    return math.degrees(data.qpos[0]), math.degrees(data.qvel[0])


for kp in [1, 5, 10, 15, 50, 100]:
    qpos_deg, qvel_deg = run_position_control(kp)
    print(f"kp={kp:>3}, qpos={qpos_deg:>8.3f} deg, qvel={qvel_deg:>8.3f} deg/s")