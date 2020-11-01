import pytest
from battleships import *

def test_is_sunk1():
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s) == True
    #add at least four more tests for is_sunk by the project submission deadline

def test_ship_type1():
    s = (6, 7, True, 3, {(6,7), (7,7), (8,7)})
    assert ship_type1(s) == "cruiser"
    #provide at least five tests in total for open_sea by the project submission deadline

def test_is_open_sea1():
    s1 = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    s2 = (6, 7, True, 6, {(6,7), (7,7), (8,7)})
    fleet = [s1,s2]
    rcf = (4,5,fleet)
    assert is_open_sea1(rcf) == True
    #provide at least five tests in total for open_sea by the project submission deadline

def test_ok_to_place_ship_at1():
    s1 = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    s2 = (6, 7, True, 3, {(6,7), (7,7), (8,7)})
    fleet = [s1,s2]
    sf = (4,5, True,4,fleet)
    assert test_ok_to_place_ship_at1(sf) == True
    #provide at least five tests in total for ok_to_place_ship_at by the project submission deadline

def test_place_ship_at1():
    #add at least one test for place_ship_at by the deadline of session 7 assignment
    #provide at least five tests in total for place_ship_at by the project submission deadline

def test_check_if_hits1():
    #add at least one test for check_if_hits by the deadline of session 7 assignment
    #provide at least five tests in total for check_if_hits by the project submission deadline

def test_hit1():
    #add at least one test for hit by the deadline of session 7 assignment
    #provide at least five tests in total for hit by the project submission deadline

def test_are_unsunk_ships_left1():
    #add at least one test for are_unsunk_ships_left by the deadline of session 7 assignment
    #provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
    
