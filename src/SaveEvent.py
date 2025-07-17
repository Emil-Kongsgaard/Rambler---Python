import json
from typing import Optional, List
from pathvalidate import sanitize_filepath
from regex import regex as re
import os as os


class EventInputError(Exception):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)



class EventData ():
    '''Datacontainer class for events
    This class should only hold data for events.
    All data is accesed and retrieved via getter and setter methods.
    All crud operations is handled by specialized classes like Event_save, etc. 
    '''
    __nameMaxLength = 20
    __idnumberLength = 4
    __versionLength = 2
    __viewOrderLength = 2
    __bodyTextLength = 1000

    def __init__(self):
        self.__name: str = "template"
        self.__idnumber: str = "0000"
        self.__related_events: List[str] = []
        self.__version: str = "00"
        self.__view_order: str = "00"
        self.__body_text: str = "lorem ipsum...."

    def __containsLetter(self, iv_string: str) -> bool:
        regexresult = re.search('[a-zA-Z]', iv_string)
        if regexresult == None:
            return True
        else:
            return False

    def __containsIllegalChar(self, iv_string: str) -> bool:
        regexresult = re.search(r'[^\w_. -]', iv_string)
        if regexresult == None:
            return True
        else:
            return False

    def __validateString(self, iv_string: str, iv_stringLength: int):
        if type(iv_string) != str:
            raise EventInputError("Input error",
                                  f"The {iv_string} is of type {type(iv_string)}. Only type string accepted.")
        elif len(iv_string) != iv_stringLength:
            raise EventInputError("Input error",
                                  f"The {iv_string} does not have the correct length of {iv_stringLength}")
        elif self.__containsLetter(iv_string) == True:
            raise EventInputError("Input error",
                                  f"The {iv_string} can only contain digits")
        elif self.__containsIllegalChar(iv_string) == True:
            raise EventInputError("Input error",
                                  f"The {iv_string} can not contain special characthers")

    def __setName(self, iv_name: str) -> Optional[None]:
        if len(iv_name) > self.__nameMaxLength:
            raise EventInputError(
                "this is an exception class", "The name is too long")
        self.__name = sanitize_filepath(iv_name)

    def __setIdnumber(self, iv_idnumber: str) -> Optional[None]:
        try:
            self.__validateString(iv_idnumber, self.__idnumberLength)
        except EventInputError as e:
            raise e
        self.__idnumber = iv_idnumber

    def __setRelatedList(self, iv_list: List[str]) -> Optional[None]:
        if len(iv_list) == 0:
            raise EventInputError(
                "this is an expecetion class", "The input can not be empty")
        for the_entry in iv_list:
            try:
                self.__validateString(the_entry, self.__idnumberLength)
            except EventInputError as e:
                raise e
        self.__related_events = iv_list

    def __setVersion(self, iv_version: str) -> Optional[None]:
        try:
            self.__validateString(iv_version, self.__versionLength)
        except EventInputError as e:
            raise e
        self.__version = iv_version

    def __setViewOrder(self, iv_viewOrder: str) -> Optional[None]:
        try:
            self.__validateString(iv_viewOrder, self.__viewOrderLength)
        except EventInputError as e:
            raise e
        self.__view_order = iv_viewOrder

    def __setBodyText(self, iv_bodytext: str) -> Optional[None]:
        if len(iv_bodytext) >= self.__bodyTextLength:
            raise EventInputError(
                "Input error", f"The event text can not be longer than {self.__bodyTextLength}")
        self.__body_text = iv_bodytext

    def setEvent(self, iv_event_dict: dict):
        try:
            self.__setName(iv_event_dict["Name"])
            self.__setRelatedList(iv_event_dict["RelatedEvents"])
            self.__setVersion(iv_event_dict["Version"])
            self.__setViewOrder(iv_event_dict["ViewOrder"])
            self.__setBodyText(iv_event_dict["BodyText"])
        except EventInputError as e:
            raise e

    def getEvent(self):
        template_dict = {"Name": self.__name,
                         "IDnumber": self.__idnumber,
                         "RelatedEvents": self.__related_events,
                         "Version": self.__version,
                         "ViewOrder": self.__view_order,
                         "BodyText": self.__body_text}
        return template_dict


class PersistEvent ():
    """Class for handling the persistance of events. 
    The class only has one public execute method, which accepts an event class as input.
    All data validations happens in SaveEvent class. This class handles persistence and assumes static data.
    On error raises an exception with input data.
    """

    def __init__(self) -> None:
        self.__filepath = os.getcwd() + "/data/eventdata.json"

    def execute(self, in_EventData: EventData):
        event_data = in_EventData.getEvent()
        try:
        # Step 1: Read the existing data
            with open(self.__filepath, "r") as file:
                data:dict = json.load(file)  # Load existing JSON data

        # Ensure the file contains a list
            if not isinstance(data, dict):
                raise ValueError("JSON file must contain a list to append objects.")

        # Step 2: Append the new object
            data.keys()
            #data.update()

        # Step 3: Write the updated data back to the file
            with open(self.__filepath, "w") as file:
                json.dump(data, file, indent=4,sort_keys=True)  # Save with pretty formatting

            print("Object appended successfully!")

        except FileNotFoundError:
        # If the file doesn't exist, create it with the new object
            with open(self.__filepath, "w") as file:
                pass
                #json.dump([new_object], file, indent=4)
            
        except json.JSONDecodeError:
            print("Error: The file does not contain valid JSON.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == '__main__':
    print("main")
    print(os.getcwd())
