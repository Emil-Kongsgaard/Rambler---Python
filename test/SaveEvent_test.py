import unittest
import SaveEvent

class EventData_test (unittest.TestCase):
        def setUp(self):
            self.Event = SaveEvent.EventData()
            self.eventdata = self.Event.getEvent()

        def tearDown(self):
            del self.Event
            del self.eventdata

        def test_01_name(self):
            args = ["this_is_a_long_name_for_an_EventData_and_should_not_be_added",
                    "",
                    ]
            for arg in args:
                self.eventdata["Name"] = arg
                self.assertRaises(SaveEvent.EventInputError,
                                self.Event.setEvent, self.eventdata)

       #def test_02_idnumber(self):
#            args = ["",
#                    "12345",
#                    "123",
#                    "?!**"
#                    ]
#            for arg in args:
#                self.eventdata["IDnumber"] = arg
#                self.assertRaises(SaveEvent.EventInputError,
#                            self.Event.setEvent, self.eventdata)

        def test_03_related_EventDatas(self):
            args = ["123", 
                    "abab", 
                    1234, 
                    "",
                    ["1234", "5678"]
                   ]
            self.eventdata["RelatedEvents"] = args
            self.assertRaises(SaveEvent.EventInputError,
                            self.Event.setEvent, self.eventdata)

        def test_04_version(self):
            args = ["1",  # short_version
                     12,  # int version
                    "123",  # long_version
                    "A1",  # letter_version
                    "?*",  # forbidden_chars
                    None  # empty_version
                ]
            for arg in args:
                self.eventdata["Version"] = arg
                self.assertRaises(SaveEvent.EventInputError,
                                self.Event.setEvent, self.eventdata)

        def test_05_view_order(self):
            args = [
                "1",  # short
                12,  # int
                "123",  # long
                "A1",  # letter
                "?*",  # forbidden_chars
                None  # empty
            ]
            for arg in args:
                self.eventdata["ViewOrder"] = arg
                self.assertRaises(SaveEvent.EventInputError,
                            self.Event.setEvent, self.eventdata)

        def test_09_body_text(self):
            # text is 1001 char
            long_text = """Lorem ipsum dolor sit amet, consectetuer adipiscing
            elit. Aenean commodo ligula eget dolor. 
            Aenean massa. Cum sociis natoque penatibus et magnis dis parturien
            montes, nascetur ridiculus mus. 
            Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
            Nulla consequat massa quis enim. 
            Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. 
            In enim justo, rhoncus ut, imperdiet a, 
            venenatis vitae, justo. 
            Nullam dictum felis eu pede mollis pretium. Integer tincidunt. 
            Cras dapibus. Vivamus elementum semper nisi. 
            Aenean vulputate eleifend tellus. 
            Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. 
            Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. 
            Phasellus viverra nulla ut metus varius laoreet. 
            Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. 
            Curabitur ullamcorper ultricies nisi. 
            Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, 
            sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Na"""
            
            self.eventdata["Bodytext"] = long_text
            self.assertRaises(SaveEvent.EventInputError,
                              self.Event.setEvent, self.eventdata)                       

class PersistData_test(unittest.TestCase):
    def setUp(self):
        self.Event = SaveEvent.EventData()
        self.eventdata = self.Event.getEvent()
        #setvalues
        self.eventdata["Name"] = "TestEvent"
        self.eventdata["RelatedEvents"] = ["0002","0003"]
        self.eventdata["Version"] = "01"
        self.eventdata["ViewOrder"] = "01"
        self.eventdata["BodyText"] = "Lorem ipsum....."

        self.Event.setEvent(self.eventdata)

    def tearDown(self):
        del self.eventdata
        del self.Event
        #+ remove .txt file from /data

    def test_01_save_first (self):
        pass

    def test_02_save_on_newline(self):
        pass
    def test_03_save_in_the_middle(self):
        pass
    def test_04_save_existing(self):
        pass
    def test_05_save_corrupted(self):
        pass



#    def test_01_create_dir(self):
#        #Test that class can create a new /data if nothing exist.
#        pass




if __name__ == '__main__':
    unittest.main()
