import bpy
from Arch1eN import Common

BONE_GROUPS = [
    # Name  |   Select  |   Active  |   Normal
    ("Arm", Common.hex_to_rgb(0x5A2A20), Common.hex_to_rgb(0xDFA093), Common.hex_to_rgb(0xD9654E)),
    ("Leg", Common.hex_to_rgb(0x7A2D27), Common.hex_to_rgb(0xFBA29B), Common.hex_to_rgb(0xFB5B51)),
    ("Spine", Common.hex_to_rgb(0x7A3166), Common.hex_to_rgb(0xFBB0E5), Common.hex_to_rgb(0xFA63D0)),
    ("Foot", Common.hex_to_rgb(0x49267A), Common.hex_to_rgb(0xC299FB), Common.hex_to_rgb(0x964FFB)),
    ("Hand", Common.hex_to_rgb(0x22277A), Common.hex_to_rgb(0x9197FB), Common.hex_to_rgb(0x474FFA)),
    ("IKElbow", Common.hex_to_rgb(0x16707A), Common.hex_to_rgb(0x78EEFB), Common.hex_to_rgb(0x2CE7FA)),
    ("IKKnee", Common.hex_to_rgb(0x167A3D), Common.hex_to_rgb(0x78FBAA), Common.hex_to_rgb(0x2EFA7C)),
    ("IKFoot", Common.hex_to_rgb(0x6C7A1A), Common.hex_to_rgb(0xE8FB80), Common.hex_to_rgb(0xDEFB35)),
]

class GroupBones(bpy.types.Operator):
    """Assumes armature is an active object."""
    bl_idname="object.group_bones" # Only 1 '.' character allowed.
    bl_label = "Group Bones"
    
    def execute(self, context):
        print(bpy.context.active_object)
        obj = bpy.context.active_object
        
        # Create bone groups.
        for name, color_select, color_active, color_normal in BONE_GROUPS:
            if name not in obj.pose.bone_groups:
                obj.pose.bone_groups.new(name=name)
            obj.pose.bone_groups[name].color_set = 'CUSTOM'
            obj.pose.bone_groups[name].colors.select = color_select
            obj.pose.bone_groups[name].colors.active = color_active
            obj.pose.bone_groups[name].colors.normal = color_normal
            
        # Assign bones to groups.
        for bone in obj.pose.bones:
            for name, _, _, _ in BONE_GROUPS:
                if name in bone.name:
                    bone.bone_group = obj.pose.bone_groups[name]
        
        return {"FINISHED"}