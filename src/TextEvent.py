
import json
import os
from typing import Optional, List
from regex import regex as re
from src.Exceptions import TextEventError
from src.constants import Constants


class TextEvent ():
    '''
    Datacontainer class for text events
    This class should only hold data for text events.
    All data is accesed and retrieved via getter and setter methods.
    All crud operations is handled by specialized classes. 
    '''
    _nameMaxLength = 20
    _idnumberLength = 4
    _versionLength = 2
    _viewOrderLength = 2
    _bodyTextLength = 1000

    def __init__(self):
        self.text_event = {"0000": #idnumber
                           {
                               Constants.NAME.value : "template",
                               Constants.REL_EVENTS.value : [],
                               Constants.VERSION.value : "00",
                               Constants.V_ORDER.value : "00",
                               Constants.B_TEXT.value: "lorem ipsum...."
                           }}
        
    def _containsLetter(self, iv_string: str) -> bool:
        regexresult = re.search('[a-zA-Z]', iv_string)
        if regexresult == None:
            return True
        else:
            return False

    def _containsIllegalChar(self, iv_string: str) -> bool:
        regexresult = re.search(r'[^\w_. -]', iv_string)
        if regexresult == None:
            return True
        else:
            return False

    def _validateString(self, iv_string: str, iv_stringLength: int):
        if type(iv_string) != str:
            raise TextEventError(errors=Constants.INP_ERR.value,
                                 message=
                                   f"The {iv_string} is of type {type(iv_string)}. Only type string accepted.")
        elif len(iv_string) != iv_stringLength:
            raise TextEventError(errors=Constants.INP_ERR.value,
                                 message=
                                 f"The {iv_string} does not have the correct length of {iv_stringLength}")
        elif self._containsLetter(iv_string):
            raise TextEventError(errors=Constants.INP_ERR.value,
                                 message=
                                 f"The {iv_string} can only contain digits")
        elif self._containsIllegalChar(iv_string):
            raise TextEventError(errors=Constants.INP_ERR.value,
                                 message=
                                 f"The {iv_string} cannot contain special characthers")

    def setName(self, iv_name: str) -> Optional[None]:
        self._validateString(iv_name,self._nameMaxLength)
        self.text_event["0000"][Constants.NAME.value] = iv_name

    def getname(self) -> str:
        return self.text_event["0000"][Constants.NAME.value]

    def setIdnumber(self, iv_idnumber: str) -> Optional[None]:
        self._validateString(iv_idnumber, self._idnumberLength)
        self.text_event = self.text_event.pop("",{iv_idnumber:self.text_event["0000"]})

    def getIdnumber(self) -> str:
        return_list = list(self.text_event.keys())
        return return_list[0]

    def setRelatedTextEvents(self, iv_list: List[str]) -> Optional[None]:
        if len(iv_list) == 0:
            raise TextEventError(
                errors=Constants.INP_ERR.value,
                                 message= "The input can not be empty")#TODO: Check the gameplay logic of this?
        for the_entry in iv_list:
            self._validateString(the_entry, self._idnumberLength)
        self.text_event["0000"][Constants.REL_EVENTS.value] = iv_list

    def getRealtedTextEvents(self) -> list:
        return self.text_event["0000"][Constants.REL_EVENTS.value]

    def setVersion(self, iv_version: str) -> Optional[None]:
        self._validateString(iv_version, self._versionLength)
        self.text_event["0000"][Constants.VERSION.value] = iv_version

    def getVersion(self) -> str:
        return self.text_event["0000"][Constants.VERSION.value]

    def setViewOrder(self, iv_viewOrder: str) -> Optional[None]:
        self._validateString(iv_viewOrder, self._viewOrderLength)
        self.text_event["0000"][Constants.V_ORDER.value] = iv_viewOrder

    def getViewOrder(self) -> str:
        return self.text_event["0000"][Constants.V_ORDER.value]

    def setBodyText(self, iv_bodytext: str) -> Optional[None]:
        if len(iv_bodytext) >= self._bodyTextLength:
            raise TextEventError(errors=Constants.INP_ERR.value,
                                 message= f"The event text can not be longer than {self._bodyTextLength}")
        self.text_event["0000"][Constants.B_TEXT.value] = iv_bodytext

    def getBodyText(self) -> str:
        return self.text_event["0000"][Constants.B_TEXT.value]

    def Save(self):
        CrudHandler = CRUDEvent()
        idnumber = self.getIdnumber()
        if idnumber == "0000":
            CrudHandler.append(self)   
        else: 
            CrudHandler.modify(idnumber, self)



    def get(self):
        
        Crudhandler = CRUDEvent() 
        idnumber = self.getIdnumber()
        text_event = Crudhandler.get(idnumber)
        self.setName(text_event[Constants.NAME.value])
        self.setRelatedTextEvents(text_event[Constants.REL_EVENTS.value])
        self.setVersion(text_event[Constants.VERSION.value])
        self.setViewOrder(text_event[Constants.V_ORDER.value])
        self.setBodyText(text_event[Constants.B_TEXT.value])



    def delete(self):
        Crudhandler = CRUDEvent() 
        idnumber = self.getIdnumber()
        Crudhandler.delete(idnumber)

        


class JSONFileHandling():
    """
    Abstract class for handling JSON I/O operations during CRUD for TextEvents. 
    Is implemented in TextEvent CRUD class which handles business logic
    """

    def __init__(self) -> None:
        raise TextEventError(message="An attempt to instantiate an abstract class was made",
                             errors=Constants.SYS_ERR.value)

    def _read_json_file(self, filepath: str) -> dict:
        """
        Read:
        Attempts to read input filepath as a json file which consist of a dict. 
        Returns empty dict if the filepath is invalid. 
        Raises TextEventError on all other error cases. 
        """
        event_data = {}
        try:
            with open(filepath, "r") as file:
                event_data = json.load(file)
            if not isinstance(event_data, dict):
                raise ValueError(
                    "JSON file must contain a dict to append objects.")
        except FileNotFoundError:
            pass  # a new file should be created during the persist
        except Exception as e:
            raise TextEventError(message=f"An error occurred during json read: {e}",
                                 errors=Constants.SYS_ERR.value)
        return event_data

    def _create_update_json_file(self, filepath: str, dict) -> None:
        """
        Create / Update
        Attemps to create using filepath and dict. 
        Raises TextEventError in all non-ok cases. 
        """
        try:
            with open(filepath, "w") as file:
                json.dump(
                    dict, file, indent=Constants.JSON_INDENT.value, sort_keys=True)
        except Exception as e:
            raise TextEventError(message=f"An error occurred during json update/create: {e}",
                                 errors=Constants.SYS_ERR.value)

    def _delete_json_file(self, filepath: str):
        """
        Delete
        Attemps to delete a given filepath. 
        Raises TextEventError if if is not a recognized file. 
        """
        if os.path.isfile(filepath):
            os.remove(filepath)
        else:
            raise TextEventError(message=f"An attempt failed to delete the file {filepath}",
                                 errors=Constants.SYS_ERR.value)

    def _get_next_number(self, filepath: str) -> str:
        Cache = CurrentNumberCache()
        current_number = Cache.get_current_number()
        if current_number == None:
            all_text_events = self._read_json_file(filepath)
            all_keys = list(all_text_events.keys())
            int_list = list(map(int, all_keys))
            int_list.sort()
            next_number = int_list[-1] + 1
        else:
            next_number = current_number + 1
        Cache.set_next_number(next_number)
        next_number = str(next_number)
        return next_number


class CRUDEvent (JSONFileHandling):
    """
    Handles CRUD operations of Text Events. 
    All methods are dependent on the data structure for TextEvents as
    defined in the init methods of the main class. 
    """

    def __init__(self) -> None:
        self._filepath = os.getcwd() + "/data/eventdata.json"

    def append(self, in_text_event: TextEvent):
        """
        Raises TextEventError on error
        """
        # get correct idnumber.
        idnumb = self._get_next_number(self._filepath)
        in_text_event.setIdnumber(idnumb)
        all_text_events = self._read_json_file(self._filepath)
        all_text_events.update(in_text_event.text_event)

        self._create_update_json_file(self._filepath, all_text_events)

    def modify(self, idnumber:str, in_text_event: TextEvent):
        """
        Modify an existing event
        """
        all_text_events = self._read_json_file(self._filepath)
        # Update value for key in all text events
        all_text_events[idnumber] = in_text_event.text_event[idnumber]

        self._create_update_json_file(self._filepath, all_text_events)

    def delete(self, idnumber:str):
        """
        Delete a Text event permanently
        """
        all_text_events = self._read_json_file(self._filepath)
        all_text_events.pop(idnumber)
        self._create_update_json_file(self._filepath, all_text_events)

    def get(self, idnumber:str):
        """
        Gets / reads an event from file. 
        """
        all_text_events = self._read_json_file(self._filepath)
        return all_text_events[idnumber]


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
        if int == type(number):
            self._current_number = number
        else:
            raise TextEventError(errors=Constants.SYS_ERR.value,
                                 message="Input must be a number")


if __name__ == '__main__':
    print("main")

