"""Here lies my attempt to not pass the bot arg in PersistentCustomID"""


# from typing import Optional, Union, List
# from interactions.client.context import CommandContext, ComponentContext, MISSING, ActionRow, Message

# from .parse import PersistentCustomID

# def hooked_str(obj):
#     class HookedStr(str):
#         def __init__(self, arg):
#             self._persistence = obj
#             super().__init__()
#     return HookedStr

# og_command_send = CommandContext.send
# og_component_send = ComponentContext.send

# def fix_component(cipher, component):
#     if isinstance(component.custom_id, PersistentCustomID):
#         component.custom_id = component.custom_id.encrypt(cipher)
#     return component

# def fix_action_row(cipher, action_row):
#     for i, component in enumerate(action_row.components):
#         if hasattr(component, "custom_id"):
#             component = fix_component(cipher, component)
#             action_row.components[i] = component
#     return action_row

# def fix_components(ctx, components):
#     cipher = ctx.member._client.token._persistence._cipher
#     if hasattr(components, "custom_id"):
#         return fix_component(cipher, components)
#     if isinstance(components, ActionRow):
#         return fix_action_row(cipher, components)
#     # if its a list of...
#     if isinstance(components, list):
#         if len(components) > 0:
#             for i, component in enumerate(components):
#                 if hasattr(components, "custom_id"):
#                     components[i] = fix_component(cipher, components)
#                 if isinstance(components, ActionRow):
#                     components[i] = fix_action_row(cipher, components)

# async def hooked_command_send(self: CommandContext, content: Optional[str] = MISSING, **kwargs) -> Message:
#     if kwargs.get("components"):
#         print("it had components")
#         kwargs["components"] = fix_components(self, kwargs["components"])

#     return await og_command_send(self, content, **kwargs)


# async def hooked_component_send(self: ComponentContext, content: Optional[str] = MISSING, **kwargs) -> Message:
#     if kwargs.get("components"):
#         kwargs["components"] = fix_components(self, kwargs["components"])
#     return await og_command_send(self, content, **kwargs)
