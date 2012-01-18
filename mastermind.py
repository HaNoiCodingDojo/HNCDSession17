import unittest

def number_of_colors_in_good_places(secret_seq, proposed_seq):

    count = 0

    for i in range( len( secret_seq ) ):
        if secret_seq[i] == proposed_seq[i]:
            count += 1

    return count

    # return len(filter(lambda x: x[0] == x[1],
    #                   zip(secret_seq, proposed_seq)))

class MasterMindTest(unittest.TestCase):
    def test_secret_sequence_1_proposed_sequence_1_return_1(self):
        self.assertEqual(1, number_of_colors_in_good_places([1], [1]))

    def test_secret_sequence_1_proposed_sequence_2_return_0(self):
        self.assertEqual(0, number_of_colors_in_good_places([1], [2]))

    def test_secret_sequence_1_1_proposed_sequence_1_1_return_2(self):
        self.assertEqual(2, number_of_colors_in_good_places([1, 1],
                                                            [1, 1]))

    def test_secret_sequence_1_2_proposed_sequence_1_1_return_1(self):
        self.assertEqual(1, number_of_colors_in_good_places([1, 2],
                                                            [1, 1]))

    def test_secret_sequence_2_3_proposed_sequence_1_1_return_0(self):
        self.assertEqual(0, number_of_colors_in_good_places([2,3],
                                                            [1,1]))

    def test_secret_sequence_2_1_proposed_sequence_1_1_return_1(self):
        self.assertEqual(1, number_of_colors_in_good_places([2,1],
                                                            [1,1]))

    def test_secret_sequence_1_1_2_proposed_sequence_2_1_1_return_1(self):
        self.assertEqual(1, number_of_colors_in_good_places([1,1,2],
                                                            [2,1,1]))

if __name__ == "__main__":
    unittest.main()
