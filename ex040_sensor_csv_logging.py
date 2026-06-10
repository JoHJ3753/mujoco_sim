# ex040_sensor_csv_logging.py

import csv
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
        <position name="joint1_servo"
                  joint="joint1"
                  kp="20"
                  ctrlrange="-3.14 3.14"
                  ctrllimited="true"/>
    </actuator>

    <sensor>
        <jointpos name="joint1_pos_sensor" joint="joint1"/>
        <jointvel name="joint1_vel_sensor" joint="joint1"/>
    </sensor>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

log_file = "sensor_log.csv"

with open(log_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow([
        "time",
        "target_deg",
        "qpos_deg",
        "qvel_deg_s",
        "sensor_pos_deg",
        "sensor_vel_deg_s"
    ])

    for i in range(500):
        target = math.radians(45) * math.sin(2 * math.pi * 0.5 * data.time)
        data.ctrl[0] = target

        mujoco.mj_step(model, data)

        sensor_pos = data.sensordata[0]
        sensor_vel = data.sensordata[1]

        writer.writerow([
            data.time,
            math.degrees(target),
            math.degrees(data.qpos[0]),
            math.degrees(data.qvel[0]),
            math.degrees(sensor_pos),
            math.degrees(sensor_vel)
        ])

print("CSV 저장 완료:", log_file)