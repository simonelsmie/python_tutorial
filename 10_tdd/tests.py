from audioop import add
import unittest
from traveller import Traveller

class TestTraveller(unittest.TestCase):
    def setUp(self):
        self.traveller = Traveller("Simon", "Solo", "UK", "Spain")
        self.travellers = [self.traveller]

    @unittest.skip
    def test_traveller_has_name(self):
        self.assertEqual("Simon", self.traveller.name)

    @unittest.skip
    def test_name_not_equal(self):
        self.assertNotEqual("Tom", self.traveller.name)

    @unittest.skip
    def test_traveller_type(self):
        self.assertEqual("Solo", self.traveller.type)

    @unittest.skip
    def test_dest_equal(self):
        pass

    @unittest.skip
    def test_dest_not_equal(self):
        pass

    @unittest.skip
    def test_traveller_origin(self):
        pass

    @unittest.skip
    def test_traveller_not_origin(self):
        pass

    @unittest.skip
    def test_traveller_has_not_packed(self):
        self.assertFalse(self.traveller.packed)

    @unittest.skip
    def test_traveller_doesnt_have_passport(self):
        pass
    
    @unittest.skip
    def test_traveller_suitcase_empty(self):
        pass

    @unittest.skip
    def test_traveller_suitcase_has_items(self):
        # add items to suitcase
        self.assertEqual(len(self.traveller.suitcase), 3)

    @unittest.skip
    def test_traveller_function_to_change_to_packed_one_3_items_in_suitcase(self):
        self.traveller.do_packing(["washbag", "shirt", "trousers"])
        self.assertEqual(len(self.traveller.suitcase), 3)
        self.assertTrue(self.traveller.packed)

    
    @unittest.skip
    def test_traveller_packed_can_collect_passport_if_packed(self):
        self.traveller.do_packing(["washbag", "shirt", "trousers"])
        self.traveller.get_passport()
        self.assertTrue(self.traveller.packed)
        self.assertTrue(self.traveller.passport)


    # Let's create a second traveller in the setUp called traveller2

    @unittest.skip
    def test_can_add_traveller_to_travellers(self):
        pass


    @unittest.skip
    def test_travellers_is_greater_than_1_then_change_to_group(self):
        # insert code here
        self.assertEqual(len(self.travellers), 1) 
        self.assertEqual("Group", self.traveller.type)
        self.assertEqual("Group", self.traveller2)

    
    # Let's create a flight counter for each traveller
    @unittest.skip
    def test_traveller_has_flight_counter(self):
        pass

    @unittest.skip
    # test that the flight counter can be increated by method lets_fly
    def test_traveller_can_fly(self):
        self.traveller.lets_fly()
        self.assertEqual(1, self.traveller.flights)
