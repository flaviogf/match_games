from match_games.pagination import (count_items, count_pages, verify_has_next,
                                    verify_has_previous)


class TestCountItems:
    def test_should_return_a_dict_with_count_equal_to_len_of_items(self):
        assert {'count': 1} == count_items([1])


class TestCountPages():
    def test_should_return_a_dict_with_pages_equal_to_2_when_count_equal_to_20_and_limit_equal_to_10(self):
        assert {'count': 20, 'pages': 2} == count_pages(10)({'count': 20})


class TestVerifyHasPrevious:
    def test_should_return_a_dict_with_has_previous_equal_to_true_when_pages_equal_to_5_and_current_page_is_equal_to_2(self):
        expected = {'pages': 5, 'has_previous': True}

        result = verify_has_previous(2)({'pages': 5})

        assert expected == result


class TestVerifyHasNext:
    def test_should_return_a_dict_with_has_next_equal_to_true_when_pages_equal_to_5_and_current_page_is_equal_to_4(self):
        expected = {'pages': 5, 'has_next': True}

        result = verify_has_next(4)({'pages': 5})

        assert expected == result
