import pytest

from day_2.IdHandler import IDHandler


@pytest.mark.parametrize(
    "id_range_list, expected_sum",
    [
        (["10-23"], 33),
        (["1000-1500"], 6060),
        (["89451761-89562523"], 984598450)
    ]
)
def test_filters_invalid_ids(id_range_list, expected_sum):
    product = IDHandler()
    invalid_id_sum= product.sum_invalid_ids(id_range_list)

    assert invalid_id_sum == expected_sum