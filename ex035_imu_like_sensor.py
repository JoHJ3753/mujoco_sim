# ex035_imu_like_sensor.py

import mujoco

xml = """
<mujoco>
    <option timestep="0.01" gravity="0 0 -9.81"/>

    <worldbody>
        <body name="imu_body" pos="0 0 1">
            <freejoint/>

            <geom name="imu_box"
                  type="box"
                  size="0.2 0.1 0.05"
                  mass="1"/>

            <site name="imu_site"
                  pos="0 0 0"
                  size="0.03"
                  rgba="0 1 0 1"/>
        </body>
    </worldbody>

    <sensor>
        <accelerometer name="imu_acc" site="imu_site"/>
        <gyro name="imu_gyro" site="imu_site"/>
    </sensor>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

for i in range(10):
    mujoco.mj_step(model, data)

print("sensordata 전체:", data.sensordata[:])

acc = data.sensordata[0:3]
gyro = data.sensordata[3:6]

print("accelerometer:", acc)
print("gyro:", gyro)