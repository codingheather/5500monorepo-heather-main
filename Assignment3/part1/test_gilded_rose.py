# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_banana_item(self):
        # Arrange
        items_one = [Item("Banana", 2, 49)]
        gilded_rose_one = GildedRose(items_one)

        original_sell_in = gilded_rose_one.get_item_sell_in("Banana")
        original_quality = gilded_rose_one.get_item_quality("Banana")

        # Act
        gilded_rose_one.update_quality() # sell_in == 1

        # Assert
        self.assertEqual("Banana", items_one[0].name)
        # check the item have a SellIn value
        self.assertEqual(1, items_one[0].sell_in)
        # check the item have a Quality value
        self.assertEqual(48, items_one[0].quality)
        new_sell_in_one = gilded_rose_one.get_item_sell_in("Banana")
        new_quality_one = gilded_rose_one.get_item_quality("Banana")

        assert new_sell_in_one < original_sell_in
        assert new_sell_in_one == original_sell_in - 1

        assert new_quality_one > -1
        assert new_quality_one <= 50
        assert new_quality_one < original_quality
        assert new_quality_one == original_quality - 1

        gilded_rose_one.update_quality() # sell_in == 0
        new_quality_two = gilded_rose_one.get_item_quality("Banana")
        assert new_quality_two > -1
        assert new_quality_two <= 50
        assert new_quality_two < new_quality_one
        assert new_quality_two == new_quality_one - 1

        gilded_rose_one.update_quality() 
        new_sell_in_two = gilded_rose_one.get_item_sell_in("Banana")
        new_quality_three = gilded_rose_one.get_item_quality("Banana")
        assert new_sell_in_two == original_sell_in - 3 # sell_in == -1; indicating passed the sell by date
        assert new_quality_three > -1
        assert new_quality_three <= 50
        assert new_quality_three < new_quality_two
        assert new_quality_three == new_quality_two - 2

    def test_aged_brie_item(self):
        items = [Item("Aged Brie", 2, 40)]
        gilded_rose = GildedRose(items)
        original_sell_in = gilded_rose.get_item_sell_in("Aged Brie")
        original_quality = gilded_rose.get_item_quality("Aged Brie")

        gilded_rose.update_quality()

        new_sell_in_one = gilded_rose.get_item_sell_in("Aged Brie")
        new_quality_one = gilded_rose.get_item_quality("Aged Brie")

        assert new_sell_in_one < original_sell_in
        assert new_sell_in_one == original_sell_in - 1

        assert new_quality_one <= 50
        assert new_quality_one > original_quality
        assert new_quality_one == original_quality + 1

        gilded_rose.update_quality()
        gilded_rose.update_quality()

        new_sell_in_two = gilded_rose.get_item_sell_in("Aged Brie")
        new_quality_two = gilded_rose.get_item_quality("Aged Brie")

        assert new_sell_in_two < new_sell_in_one
        assert new_sell_in_two == new_sell_in_one - 2

        assert new_quality_two <= 50
        assert new_quality_two > new_quality_one
        assert new_quality_two == new_quality_one + 3

        # hit 50 already for sure
        for i in range(5):
            gilded_rose.update_quality()

        new_quality_three = gilded_rose.get_item_quality("Aged Brie")
        assert new_quality_three == 50

    def test_sulfuras_item(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 42)]
        gr = GildedRose(items)

        original_quality = gr.get_item_quality("Sulfuras, Hand of Ragnaros")
        original_sell_in = gr.get_item_sell_in("Sulfuras, Hand of Ragnaros")

        gr.update_quality()

        new_quality = gr.get_item_quality("Sulfuras, Hand of Ragnaros")
        new_sell_in = gr.get_item_sell_in("Sulfuras, Hand of Ragnaros")        

        assert new_quality == original_quality
        assert new_sell_in == original_sell_in

        gr.update_quality()

        newer_quality = gr.get_item_quality("Sulfuras, Hand of Ragnaros")
        new_sell_in = gr.get_item_sell_in("Sulfuras, Hand of Ragnaros")        

        assert new_quality == original_quality
        assert new_sell_in == original_sell_in

        assert newer_quality == original_quality

    def test_backstage_passes_item(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 42)]
        gilded_rose = GildedRose(items)

        original_sell_in = gilded_rose.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert")
        original_quality = gilded_rose.get_item_quality("Backstage passes to a TAFKAL80ETC concert")

        gilded_rose.update_quality()

        new_sell_in_one = gilded_rose.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert")
        new_quality_one = gilded_rose.get_item_quality("Backstage passes to a TAFKAL80ETC concert")

        assert new_sell_in_one < original_sell_in
        assert new_sell_in_one == original_sell_in - 1

        assert new_quality_one <= 50
        assert new_quality_one > original_quality
        assert new_quality_one == original_quality + 2

        gilded_rose.update_quality() 
        new_quality_two = gilded_rose.get_item_quality("Backstage passes to a TAFKAL80ETC concert")
        assert new_quality_two <= 50
        assert new_quality_two > new_quality_one
        assert new_quality_two == new_quality_one + 3

        gilded_rose.update_quality() # 4
        gilded_rose.update_quality() # 3
        gilded_rose.update_quality() # 2
        gilded_rose.update_quality() # 1
        gilded_rose.update_quality() # 0

        new_quality_three = gilded_rose.get_item_quality("Backstage passes to a TAFKAL80ETC concert")
        assert new_quality_three == 0

    def test_conjured_item(self):
        # Arrange
        items = [Item("Conjured", 1, 42)]
        gr = GildedRose(items)

        original_sell_in = gr.get_item_sell_in("Conjured")
        original_quality = gr.get_item_quality("Conjured")

        # Act
        gr.update_quality()

        # Assert
        new_sell_in = gr.get_item_sell_in("Conjured") # 0 
        new_quality = gr.get_item_quality("Conjured")

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality < original_quality
        assert new_quality == original_quality - 2 # "Conjured" items degrade in Quality twice as fast as normal items

        gr.update_quality()

        new_quality = gr.get_item_quality("Conjured")

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality < original_quality
        assert new_quality == original_quality - 4


if __name__ == '__main__':
    unittest.main()
