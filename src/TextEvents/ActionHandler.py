from Screens.Utils import Screen
from src.constants import Constants as C
from src.Exceptions import TextEventError

class ActionHandler:
    """Handler that executes a textevent action string.

    Public contract:
      - constructor takes no parameters
      - one public method: Handle(action: str) -> None
    Behavior:
      - resolves `action` (string) via predefined actions
    """
    def __init__(self) -> None:
        # intentionally no parameters and no public helpers
        return None
    def Handle(self, action: str, Context:Screen) -> None:
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
                Context.notifyLoadScreenRequested(param[0])
                pass

            case _:
                raise TextEventError(errors=C.SYS_ERR.value,   
                                     message=f"Unrecognized action code: {action_code}")
            
        return None