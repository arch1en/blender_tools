import bpy
import inspect

class ABT_PT_UnrealEngine_Panel(bpy.types.Panel):
    """My Object Moving Script"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "ABT_PT_UnrealEngine_Panel"        # Optional. If ommited, class name will be used.
    bl_label = "Unreal Engine"         # Display name in the interface.
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "ABT"

    def draw(self, context):        # execute() is called when running the operator.
        layout = self.layout
        
        row = layout.row()
        
        row.operator("object.setup_scene_for_unreal_engine", text="Setup Scene")

class SetupSceneForUnrealEngine(bpy.types.Operator):
    """Assumes armature is an active object."""
    bl_idname="object.setup_scene_for_unreal_engine" # Only 1 '.' character allowed.
    bl_label = "Setup Scene"
    
    def execute(self, context):
        print(bpy.context.scene.unit_settings.scale_length)
        bpy.context.scene.unit_settings.scale_length = 0.01
        return {"FINISHED"}