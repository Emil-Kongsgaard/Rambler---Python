import unittest
import json
import os
from unittest import mock
from unittest.mock import MagicMock
from src.Exceptions import TextEventError
from src.TextEvent import CurrentNumberCache, JSONFileHandling,TextEvent

class test_CurrentNumberCache(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = CurrentNumberCache()

    def tearDown(self) -> None:
        del self.instance
        
    def test_01_new_instance(self):
        instance_2 = CurrentNumberCache()
        self.assertEqual(self.instance,instance_2,"The singleton pattern does not work")
    
    def test_02_get_number(self):
        number = self.instance.get_current_number()
        self.assertIsNone(number,"Get_current_number does not return None as initial value")
    
    def test_03_get_number(self):
        self.instance._current_number = 3
        number = self.instance.get_current_number()
        self.assertEqual(number,3,"get_current_number does not return the correct number.")

    def test_04_set_number(self):
        self.instance.set_next_number(3)
        self.assertEqual(self.instance._current_number,3,"set_current_number does not save number correct")
    
    def test_05_set_number(self):
        number = "not a number"
        with self.assertRaises(Exception):
            self.instance.set_next_number(number) # pyright: ignore[reportArgumentType]

    def test_06_get_number(self):
        self.instance.set_next_number(3)
        instance_3 = CurrentNumberCache()
        self.assertEqual(instance_3.get_current_number(),3,"the correct number is not returned when a new instance is called")

class test_JSONFileHandling(unittest.TestCase):

    def setUp(self) -> None:
        patcher = mock.patch('src.TextEvent.JSONFileHandling.__init__', return_value=None)
        self.addCleanup(patcher.stop)
        self.mock_init = patcher.start()

        self.instance = JSONFileHandling()
        
    def tearDown(self) -> None:
        return None
    @unittest.expectedFailure #The class is patched in setup - so this should fail
    def test_01_no_instance(self):
        with self.assertRaises(TextEventError):
            obj = JSONFileHandling()
    
    def test_02_read_file(self):
        dict = self.instance._read_json_file("not a filepath")
        self.assertEqual(dict,{},"Read_file does not return empty dict when file is not found")

    def test_03_read_file(self):
        filepath = os.getcwd() + "/data/testdata.txt"
        with open(filepath, "w") as file:
            file.write("this file should not exist outside of testing")
        with self.assertRaises(TextEventError):
            self.instance._read_json_file(filepath)
        os.remove(filepath)

    def test_04_read_file(self):
        filepath = os.getcwd() + "/data/testdata.json"
        test_list = ["this","is","not","a","dict"]
        with open(filepath,"w") as file:
            json.dump(test_list,file,indent=4)
        with self.assertRaises((ValueError,TextEventError)):
            self.instance._read_json_file(filepath)
        os.remove(filepath)
    
    def test_05_create_file(self):
        with self.assertRaises(TextEventError):
            self.instance._create_update_json_file("not a file path",dict)

    def test_06_create_file(self):
        my_dict = {"this should not":"exist outside of testing"}
        filepath = os.getcwd() + "/data/testdata.json"
        self.instance._create_update_json_file(filepath,my_dict)
        if not os.path.isfile(filepath) :
            self.fail("_create_update_json_file did not create a file")
        os.remove(filepath)       
    

    @mock.patch('src.TextEvent.CurrentNumberCache')
    def test_07_get_next_number_from_file(self, mock_cache_cls):
        # Arrange
        mock_cache = MagicMock()
        mock_cache.get_current_number.return_value = None
        mock_cache_cls.return_value = mock_cache

        # Mock the method under test to have access to the actual function
        self.instance._read_json_file = MagicMock(return_value={"1": "event1", "2": "event2", "5": "event5"})

        # Act
        result = self.instance._get_next_number("dummy.json")

        # Assert
        self.assertEqual(result, "6")  # highest key 5 + 1
        mock_cache.set_next_number.assert_called_once_with(6)

    @mock.patch('src.TextEvent.CurrentNumberCache')
    def test_get_next_number_from_cache(self, mock_cache_cls):
        # Arrange
        mock_cache = MagicMock()
        mock_cache.get_current_number.return_value = 10
        mock_cache_cls.return_value = mock_cache

        self.instance._read_json_file = MagicMock()  # should not be called

        # Act
        result = self.instance._get_next_number("dummy.json")

        # Assert
        self.assertEqual(result, "11")
        mock_cache.set_next_number.assert_called_once_with(11)
        self.instance._read_json_file.assert_not_called()

    
# CRUDEvent

if __name__ == '__main__':
    unittest.main()
