
import json
import os
#from regex import regex as re
from src.Exceptions import TextEventError
from src.constants import Constants as C


# here is sample text event
{"0000":  # idnumber
 {
     C.NAME.value: "template",
     C.REL_EVENTS.value: [],
     C.VERSION.value: "00",
     C.V_ORDER.value: "00",
     C.B_TEXT.value: "lorem ipsum....",
     C.POS_TITLE.value: 'Positive_option_title',
     C.POS_FUNCS.value: 'Postive_functions',
     C.POS_BUT_ST.value: 'Postive_button_state',
     C.NEG_TITLE.value: 'Negative_option_title',
     C.NEG_FUNCS.value: 'Negative_functions',
     C.NEG_BUT_ST.value: 'Negative_button_state'
 }} # pyright: ignore[reportUnusedExpression]

class JSONFileHandling():
    """
    Class for handling JSON crud operations for text events. 
    """
    
    def __init__(self) -> None:
        self._filepath = C.JSON_FILEPATH.value

    def _from_json(self) -> dict:
        """
        Read:
        Attempts to read input filepath as a json file which consist of a dict. 
        Returns empty dict if the filepath is invalid. 
        Raises TextEventError on all other error cases. 
        """
        event_data = {}
        if not os.path.isfile(self._filepath):
            return event_data
        try:
            with open(self._filepath, "r") as file:
                event_data = json.load(file)
            if not isinstance(event_data, dict):
                raise ValueError(
                    "JSON file must contain a dict to append objects.")
        except FileNotFoundError:
            pass  # a new file should be created during the persist
        except Exception as e:
            raise TextEventError(message=f"An error occurred during json read: {e}",
                                 errors=C.SYS_ERR.value)
        return event_data

    def _to_json(self, textevent_data:dict) -> None:
        """
        Create / Update
        Attemps to create using filepath and dict. 
        Raises TextEventError in all non-ok cases. 
        """

        try:
            with open(self._filepath, "w") as file:
                json.dump(
                    textevent_data, file, indent=C.JSON_INDENT.value, sort_keys=True)
        except Exception as e:
            raise TextEventError(message=f"An error occurred during json update/create: {e}",
                                 errors=C.SYS_ERR.value)

    def _delete_json(self):
        """
        Delete
        Attemps to delete a given filepath. 
        Raises TextEventError if if is not a recognized file. 
        """
        if os.path.isfile(self._filepath):
            os.remove(self._filepath)
        else:
            raise TextEventError(message=f"An attempt failed to delete the file {self._filepath}",
                                 errors=C.SYS_ERR.value)

    def _get_next_number(self) -> str:
        """
        Internal method to determine the next available numeric key for text events.
        """
        Cache = CurrentNumberCache()
        current_number = Cache.get_current_number()
        # If there is no cached number, inspect file to determine highest numeric key.
        if current_number is None:
            all_text_events = self._from_json()
            all_keys = list(all_text_events.keys())
            # Keep only numeric keys (defensive) and convert to ints
            numeric_keys = [int(k) for k in all_keys if isinstance(k, str) and k.isdigit()]
            if not numeric_keys:
                next_number = 0
            else:
                numeric_keys.sort()
                next_number = numeric_keys[-1] + 1
        else:
            next_number = current_number + 1

        # Cache the integer value for subsequent calls
        Cache.set_next_number(next_number)

        # Return zero-padded string id (4 digits to match existing format e.g. "0000")
        next_number_str = str(next_number).zfill(4)
        return next_number_str
    
    def save_multiple(self, list_of_dicts: list[dict]) -> None:
        """
        Method will ignore the IDnumbers of the input events. 
        Idnumbers will be correctly determined during save. 
        Raises TextEventError on error.
        Output is None on success.
        """
        all_text_events = self._from_json()
        for event in list_of_dicts:
            next_number = self._get_next_number()
            all_text_events[next_number] = event
        self._to_json(all_text_events)
        return None

    def update_multiple(self, text_events:dict) -> None:
        """
        Method will update existing events based on their IDnumbers.
        Raises TextEventError on error.
        Output is None on success.
        """
        all_text_events = self._from_json()
        for idnumber, event in text_events.items():
            if idnumber in all_text_events:
                all_text_events[idnumber] = event
            else:
                raise TextEventError(errors=C.SYS_ERR.value,
                                     message=f"Text event with IDnumber {idnumber} does not exist for update.")

class CurrentNumberCache:
    _instance = None
    _current_number = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CurrentNumberCache, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def get_current_number(self):
        if self._current_number == None:
            return None
        else:
            return self._current_number

    def set_next_number(self, number: int):
        # accept ints only
        if isinstance(number, int):
            self._current_number = number
        else:
            raise TextEventError(errors=C.SYS_ERR.value,
                                 message="Input must be a number")



class TextEvent(JSONFileHandling):
    def __init__(self) -> None:
        super().__init__()

    def get(self,idnumber:str | None = None) -> dict:
        """
        Method to get text events. 
        If idnumber is provided, will return single text event dict.
        Raises TextEventError on error.
        Output is dict of text events or single text event dict.
        """
        if idnumber is not None:
            all_events = self._from_json()
            if idnumber in all_events:
                return all_events[idnumber]
            else:
                raise TextEventError(errors=C.SYS_ERR.value,
                                     message=f"Text event with IDnumber {idnumber} does not exist.")
        return self._from_json()

    # implement saveing text events to json file later. 
    # reuse implementation from TextEvent.py
    def save(self,*args) -> None:
        """
        Method will check if parameters are list of dicts or list of events
        Will perform validations on the text events before saving.
        pass valid textevents on to appropriate internal method.
        Raises TextEventError on error.
        Output is None on success.
        """
        if len(args) == 1 and isinstance(args[0], list):
            list_of_events = args[0]
            if all(isinstance(event, dict) for event in list_of_events):
                return self.save_multiple(list_of_events)
            else:
                raise TextEventError(errors=C.SYS_ERR.value,
                                     message="All items in the list must be dicts representing text events.")
        elif len(args) == 1 and isinstance(args[0], dict):
            text_events_dict = args[0]
            return self.update_multiple(text_events_dict)
        else:
            raise TextEventError(errors=C.SYS_ERR.value,
                                 message="Invalid arguments provided to save method.")


if __name__ == '__main__':
    print("main")
    textevent = TextEvent()
    listevents = textevent.get()
    print(listevents)


