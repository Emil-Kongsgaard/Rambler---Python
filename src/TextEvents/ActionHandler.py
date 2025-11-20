from Screens.Utils import Screen
from src.constants import Constants as C
from src.Exceptions import TextEventError


def Handle(action: str, Context:Screen) -> None:
    """
    Resolve and execute an action string.
    Parameters
    - action: str - identifier for a predefined action.
    Raises TextEventError on resolution or execution failure.
    """ 
    if not isinstance(action, str):
        raise TextEventError(errors=C.INP_ERR.value,
                                 message="Action must be a string")
    action = action.strip()
    action_code = action[0:10] 
    param = ""
    params = []
    for char in action[11:20]:
        param += char
        if char == '_':
            params.append(param[:-1])  # exclude underscore
            param = ""

    match action_code:
        case C.ACTION_NEW_SCREEN.value:
            if len(params) == 2:
                Context.notifyLoadScreenRequested(params[0],params[1])
            else:
                Context.notifyLoadScreenRequested(params[0])
            pass
        case C.ACTION_CHANGE_VALUE.value:
                Context.notifyChangeValueRequested(params[0],int(params[1]))

        case _:
            raise TextEventError(errors=C.SYS_ERR.value,   
                                     message=f"Unrecognized action code: {action_code}")
            
    return None