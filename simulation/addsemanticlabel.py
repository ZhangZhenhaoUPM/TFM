import omni.replicator.core as rep
import omni.usd
from isaacsim.core.utils.semantics import add_update_semantics

stage = omni.usd.get_context().get_stage()

# 遍历并打标签（用 core API）
for prim in stage.Traverse():
    name = prim.GetName().lower()
    prim_type = prim.GetTypeName()

    if "table" in name and prim_type == "Mesh":
        add_update_semantics(prim, "table")
    elif "floor_bottom" in name and prim_type == "Mesh":
        add_update_semantics(prim, "floor")
    elif "window" in name and prim_type == "Mesh":
        add_update_semantics(prim, "window")
    elif "wall" in name and prim_type == "Mesh":
        add_update_semantics(prim, "wall")



