import pytest

from day_2.GiftshopProduct import GiftShopProduct


@pytest.mark.parametrize(
    "id_range_list, expected_invalid_ids",
    [
        (["2323-5656"], [11, 22]),
    ]
)
def test_filters_invalid_ids(id_range_list, expected_invalid_ids):
    product = GiftShopProduct()
    invalid_ids= product.filter_invalid_ids(id_range_list)
    invalid_id_sum = product.sum_invalid_ids(invalid_ids)

    assert invalid_ids == expected_invalid_ids