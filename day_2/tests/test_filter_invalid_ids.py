import pytest

from day_2.GiftshopProduct import GiftShopProduct


@pytest.mark.parametrize(
    "id_range_list, expected_invalid_ids",
    [
        (["5168-7482"], [11, 22]),
    ]
)
def test_filters_invalid_ids(id_range_list, expected_invalid_ids):
    product = GiftShopProduct()
    invalid_ids= product.filter_invalid_ids(id_range_list)

    assert invalid_ids == expected_invalid_ids