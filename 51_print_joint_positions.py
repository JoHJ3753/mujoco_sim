# 51_print_joint_positions.py

from pathlib import Path
import mujoco

MENAGERIE_DIR = Path(__file__).parent / "mujoco_menagerie"
PANDA_XML = MENAGERIE_DIR / "franka_emika_panda" / "panda.xml"

model = mujoco.MjModel.from_xml_path(str(PANDA_XML))
data = mujoco.MjData(model)

mujoco.mj_forward(model, data)

print("Joint positions")
print("-" * 60)
print(f"{'joint_id':<10} {'name':<25} {'qpos_index':<12} {'position':<12}")
print("-" * 60)

for joint_id in range(model.njnt):
    joint_name = mujoco.mj_id2name(
        model,
        mujoco.mjtObj.mjOBJ_JOINT,
        joint_id
    )

    qpos_index = model.jnt_qposadr[joint_id]
    position = data.qpos[qpos_index]

    print(f"{joint_id:<10} {joint_name:<25} {qpos_index:>12} {position:>12.6f}")