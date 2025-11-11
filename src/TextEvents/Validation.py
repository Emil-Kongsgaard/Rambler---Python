import re
from src.Exceptions import TextEventError
from src.constants import Constants as C


# here is sample text event
{"0000":  # idnumber
 {
     C.NAME.value: "template",
     C.REL_EVENT.value: [],
     C.VERSION.value: "00",
     C.B_TEXT.value: "lorem ipsum....",
     C.POS_TITLE.value: 'Positive_option_title',
     C.POS_FUNCS.value: {   "1":   lambda: print("somefunction"),
                            "2":   lambda: print("somethingelse")
                        },
     C.POS_BUT_ST.value: 'Postive_button_state',
     C.NEG_TITLE.value: 'Negative_option_title',
     C.NEG_FUNCS.value: {   "1":   lambda: print("somefunction"),
                            "2":   lambda: print("somethingelse")
                        },
     C.NEG_BUT_ST.value: 'Negative_button_state'
 }} # pyright: ignore[reportUnusedExpression]

class Validator ():
    """
    Class for validation of text event data   
    """
    def __init__(self) -> None:
        pass

    def validate(self, text_event:dict) -> None:
        """
        Validates input text event dict.
        Raises TextEventError on error.
        """
        for idnumber, event in text_event.items():
            self._validateString(idnumber, C.IDNUMBERLENGTH.value, "idnumber")
            self._validateString(event[C.NAME.value], C.NAMELENGTH.value, "name")
            self._validateRelatedEvents(event[C.REL_EVENT.value])
            self._validateString(event[C.VERSION.value], C.VERSIONLENGTH.value, "version")
            self._validateString(event[C.B_TEXT.value], C.BODYTEXTLENGTH.value, "body_text")
            self._validateFunctions(event[C.POS_FUNCS.value])
            self._validateButtonState(event[C.POS_BUT_ST.value])

   
    def _containsLetter(self, iv_string: str) -> bool:
        regexresult = re.search('[a-zA-Z]', iv_string)
        if regexresult == None:
            return False
        else:
            return True

    def _containsIllegalChar(self, iv_string: str) -> bool:
        regexresult = re.search(r'[^\w_. -]', iv_string)
        if regexresult == None:
            return False
        else:
            return True

    def _validateString(self, iv_string: str, iv_stringLength: int, field_name: str = "value"):
        if not isinstance(iv_string, str):
            raise TextEventError(errors=C.INP_ERR.value,
                                 message=f"The field '{field_name}' is of type {type(iv_string).__name__}. Only type string accepted.")
        if len(iv_string) != iv_stringLength:
            raise TextEventError(errors=C.INP_ERR.value,
                                 message=f"The field '{field_name}' does not have the correct length of {iv_stringLength}")
        # For ID-like fields: require digits only
        if not iv_string.isdigit():
            raise TextEventError(errors=C.INP_ERR.value,
                                 message=f"The field '{field_name}' can only contain digits.")

    def _validateFunctions(self, functions: dict) -> None:
        pass
        
    
    def _validateButtonState(self, button_state: str) -> None:
        """
        Validates input button state.
        Raises TextEventError on error.
        """
        valid_vals = [C.ENABLED.value, C.DISABLED.value]
        # include optional hidden state if present in constants
        if hasattr(C, "HIDDEN"):
            valid_vals.append(C.HIDDEN.value) # pyright: ignore[reportAttributeAccessIssue]
        if button_state not in valid_vals:
            raise TextEventError(errors=C.INP_ERR.value,
                                 message=f"The button state '{button_state}' is not valid. Only {', '.join(valid_vals)} accepted.")
        
    def _validateRelatedEvents(self, related_events: list) -> None:
        """
        Validates input related events list.
        Raises TextEventError on error.
        """
        if not isinstance(related_events, list):
            raise TextEventError(errors=C.INP_ERR.value,
                                 message=
                                 f"The related events object is of type {type(related_events)}. Only type list accepted.")
        for event in related_events:
            self._validateString(event, C.IDNUMBERLENGTH.value)