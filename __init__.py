import bpy
from Arch1eN import Common
from Arch1eN import Rigging
from Arch1eN import UnrealEngine

bl_info = {
    "name": "ABT",
    "description": "Arch1eNs Blender Tools",
    "blender": (2, 80, 0),
    "category": "Object",
}

class ABT_PT_Panel(bpy.types.Panel):
    """My Object Moving Script"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "ABT_PT_Panel"        # Optional. If ommited, class name will be used.
    bl_label = "Rigging"         # Display name in the interface.
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "ABT"

    def draw(self, context):        # execute() is called when running the operator.
        layout = self.layout
        
        row = layout.row()
        
        if bpy.context.active_object is not None:
            if bpy.context.active_object.type == "ARMATURE":
                row.operator("object.GroupBones", text="Group Bones")
            else:   
                row.label(text="Please select armature.")

    # Lets Blender know the operator finished successfully.

def register():
    bpy.utils.register_class(ABT_PT_Panel)
    bpy.utils.register_class(Rigging.GroupBones)
    bpy.utils.register_class(UnrealEngine.ABT_PT_UnrealEngine_Panel)
    bpy.utils.register_class(UnrealEngine.SetupSceneForUnrealEngine)
    
def unregister():
    bpy.utils.unregister_class(ABT_PT_Panel)
    bpy.utils.unregister_class(Rigging.GroupBones)
    bpy.utils.unregister_class(UnrealEngine.ABT_PT_UnrealEngine_Panel)
    bpy.utils.unregister_class(UnrealEngine.SetupSceneForUnrealEngine)  

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()