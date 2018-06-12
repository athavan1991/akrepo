import unittest

def tupretfirstelement(meeting):
    return meeting[0];

def merge_ranges(meetings):

    # meetings is a list of tuple
    # new empty list to add tuples
    merged_list = [];

    #Step 1: Sort the tuples in the increasing order of the start times
    meetings = sorted(meetings, key=tupretfirstelement);

    currentstarttime = meetings[0][0];
    currentendtime = meetings[0][1];

    #step2: Compare the previous endtime with the current starttime
    #       if greater than or equal to 1, then update the tuple
    #       else update the endtime alone if its greater than current
    for (starttime, endtime) in meetings[1:len(meetings)]:
        if starttime - currentendtime >= 1:
            merged_list.append((currentstarttime, currentendtime));
            currentstarttime = starttime;
        if endtime > currentendtime:
            currentendtime = endtime;
    merged_list.append((currentstarttime, currentendtime));

    return merged_list;


# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main()