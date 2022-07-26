import unittest
from traveller import Traveller

class TestTraveller(unittest.TestCase):
    def setUp(self):
        self.traveller = Traveller("Simon", "Solo", "UK", "Spain")
        self.traveller2 = Traveller("James", "Solo", "UK", "Spain")
        self.travellers = [self.traveller]

    # @unittest.skip
    def test_traveller_has_name(self):
        self.assertEqual("Simon", self.traveller.name)

    # @unittest.skip
    def test_name_not_equal(self):
        self.assertNotEqual("Tom", self.traveller.name)

    # @unittest.skip
    def test_traveller_type(self):
        self.assertEqual("Solo", self.traveller.type)

    # @unittest.skip
    def test_dest_equal(self):
        self.assertEqual("Spain", self.traveller.destination)

    # @unittest.skip
    def test_dest_not_equal(self):
        self.assertNotEqual("Rawanda", self.traveller.destination)

    # @unittest.skip
    def test_traveller_origin(self):
        self.assertEqual("UK", self.traveller.origin)

    # @unittest.skip
    def test_traveller_not_origin(self):
        self.assertNotEqual("GBR", self.traveller.origin)

    # @unittest.skip
    def test_traveller_has_not_packed(self):
        self.assertFalse(self.traveller.packed)

    # @unittest.skip
    def test_traveller_doesnt_have_passport(self):
        self.assertFalse(self.traveller.passport)
    
    # @unittest.skip
    def test_traveller_suitcase_empty(self):
        self.assertEqual(len(self.traveller.suitcase), 0)

    # @unittest.skip
    def test_traveller_suitcase_has_items(self):
        # add items to suitcase
        # traveller["suitcase"].append("washbag")
        self.traveller.suitcase.append("washbag")
        self.traveller.suitcase.append("shirt")
        self.traveller.suitcase.append("trousers")
        self.assertEqual(len(self.traveller.suitcase), 3)

    # @unittest.skip
    def test_traveller_function_to_change_to_packed_once_3_items_in_suitcase(self):
        self.traveller.do_packing(["washbag", "shirt", "trousers"])
        self.assertEqual(len(self.traveller.suitcase), 3)
        self.assertTrue(self.traveller.packed)

    
    # @unittest.skip
    def test_traveller_packed_can_collect_passport_if_packed(self):
        self.traveller.do_packing(["washbag", "shirt", "trousers"])
        self.traveller.get_passport()
        self.assertTrue(self.traveller.packed)
        self.assertTrue(self.traveller.passport)


    # Let's create a second traveller in the setUp called traveller2

    # @unittest.skip
    def test_can_add_traveller_to_travellers(self):
        self.travellers.append(self.traveller2)
        self.assertEqual(len(self.travellers), 2)


    # @unittest.skip
    def test_travellers_is_greater_than_1_then_change_to_group(self):
        # insert code here
        self.travellers.append(self.traveller2)
        if len(self.travellers) > 1:
            for traveller in self.travellers:
                traveller.grouped()

        self.assertEqual(len(self.travellers), 2) 
        self.assertEqual("Group", self.traveller.type)
        self.assertEqual("Group", self.traveller2.type)

    
    # Let's create a flight counter for each traveller
    # @unittest.skip
    def test_traveller_has_flight_counter(self):
        self.assertEqual(self.traveller.flights, 0)

    # @unittest.skip
    # test that the flight counter can be increated by method lets_fly
    def test_traveller_can_fly(self):
        self.traveller.lets_fly()
        self.assertEqual(1, self.traveller.flights)
