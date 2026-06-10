# ex022_ctrl_value_comparison.py

import mujoco

def run_motor(ctrl_value):
    xml = """
    <mujoco>
        <option timestep="0.01" gravity="0 0 -9.81"/>

        <worldbody>
            <body name="pendulum" pos="0 0 1">
                <joint name="hinge_joint"
                       type="hinge"
                       axis="0 1 0"
                       limited="true"
                       range="-90 90"/>

                <geom name="rod"
                      type="capsule"
                      fromto="0 0 0  0 0 -1"
                      size="0.05"
                      mass="1"/>
            </body>
        </worldbody>

        <actuator>
            <motor name="hinge_motor"
                   joint="hinge_joint"
                   gear="1"
                   ctrlrange="-5 5"
                   ctrllimited="true"/>
        </actuator>
    </mujoco>
    """

    model = mujoco.MjModel.from_xml_string(xml)
    data = mujoco.MjData(model)

    data.ctrl[0] = ctrl_value

    for i in range(100):
        mujoco.mj_step(model, data)

    return data.qpos[0], data.qvel[0]


for ctrl in [-5, -2, 0, 2, 5]:
    qpos, qvel = run_motor(ctrl)
    print(f"ctrl={ctrl:>3}, qpos={qpos:.4f}, qvel={qvel:.4f}")