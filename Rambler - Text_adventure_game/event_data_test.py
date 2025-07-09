import unittest
import SaveEvent as EventData


class EventData_data_test (unittest.TestCase):
    #def __setUp(self):
        #print("__setiing up testcase")
        #EventData_01 = EventData.EventData()

    #def tearDown(self):
        #print("tearing down testcases")
        #del EventData_01 
    
    def test_01_name (self):
        long_name = "this_is_a_long_name_for_an_EventData_and_should_not_be_added"
        EventData_01 = EventData.EventData()
        self.assertRaises(EventData.EventInputError, EventData_01.__setName ,long_name)
        del EventData_01
#    def test_02_forbidden_char (self):
#        forbidden_name = "NUL, : , ?, *, +, and %"
#        EventData_02 = EventData.EventData()
#        EventData_02.__setName(forbidden_name)
#        self.assertTrue(forbidden_name == EventData_02.getName(),"Name contains forbidden characthers")
#        del EventData_02
    def test_03_name_not_space(self):
        emtpy_name = ""
        EventData_03 = EventData.EventData()
        self.assertRaises(EventData.EventInputError, EventData_03.__setName ,emtpy_name)
        del EventData_03
    
    def test_04_idnumber_empty(self):
        empty_idnumber = ""
        EventData_04 = EventData.EventData()
        self.assertRaises(EventData.EventInputError, EventData_04.__setIdnumber ,empty_idnumber)
        del EventData_04

    def test_05_idnumber_length(self):
        long_idnumber = "12345"
        short_idnumber = "123"
        EventData_05 = EventData.EventData()
        self.assertRaises(EventData.EventInputError, EventData_05.__setIdnumber ,long_idnumber)
        self.assertRaises(EventData.EventInputError, EventData_05.__setIdnumber ,short_idnumber)
        del EventData_05

    def test_06_related_EventDatas(self):
        forbidden_list = ["123","abab",1234,"",["1234","5678"]]
        EventData_06 = EventData.EventData()
        self.assertRaises(EventData.EventInputError, EventData_06.__setRelatedList, forbidden_list)
        del EventData_06
    
    def test_07_version(self):
        EventData_07 = EventData.EventData()
        args = [
         "1", #short_version
         12, #int version
         "123", #long_version
         "A1", #letter_version 
        "?*", #forbidden_chars 
         None #empty_version 
           ]
        for arg in args:
            self.assertRaises(EventData.EventInputError, EventData_07.__setVersion, arg)
        del EventData_07

    def test_08_view_order(self):
        EventData_08 = EventData.EventData()
        args = [
         "1", #short
         12, # int 
         "123", #long
         "A1", #letter 
        "?*", #forbidden_chars 
         None #empty
           ]
        for arg in args:
            self.assertRaises(EventData.EventInputError, EventData_08.__setViewOrder, arg)
        del EventData_08

    def test_09_body_text(self):
        EventData_09 = EventData.EventData()
        #text is 1001 char
        long_text = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. 
        Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. 
        Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. 
        Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, 
        venenatis vitae, justo. 
        Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. 
        Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. 
        Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. 
        Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. 
        Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, 
        sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Na"""
        self.assertRaises(EventData.EventInputError, EventData_09.__setBodyText, long_text)
        del EventData_09
if __name__ == '__main__':
    unittest.main()