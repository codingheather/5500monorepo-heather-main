# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemWithBehavior(Item):
    def __init__(self, name, sell_in, quality, qualityBehavior):
        super().__init__(name, sell_in, quality)
        self.qualityBehavior = qualityBehavior

    def apply_quality_change(self):
        self.qualityBehavior.apply_quality_change(self)

class QualityBehavior:
    def apply_quality_change(self, item):
        pass

class BasicQualityBehavior(QualityBehavior):
    def apply_quality_change(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1

        item.sell_in = item.sell_in - 1
        
        if item.sell_in < 0:
            if item.quality > 0:
                item.quality = item.quality - 1
        

class AgedBrieQualityBehavior(QualityBehavior):
    def apply_quality_change(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.quality < 50:
                item.quality = item.quality + 1

class SulfurasQualityBehavior(QualityBehavior):
    def apply_quality_change(self, item):
        return

class BackStagePassesQualityBehavior(QualityBehavior):
    def apply_quality_change(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.sell_in < 11:
                if item.quality < 50:
                    item.quality = item.quality + 1
            if item.sell_in < 6:
                if item.quality < 50:
                    item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = 0


class ConjuredQualityBehavior(QualityBehavior):
    def apply_quality_change(self, item):
        if item.quality > 0:
            item.quality = item.quality - min(2, item.quality)
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.quality > 0:
                item.quality = item.quality - min(2, item.quality)


class GildedRose(object):

    def __init__(self, items: list[ItemWithBehavior]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
        # can add more class attributes

    def update_quality(self):
        for item in self.items:
            item.apply_quality_change()

    def get_item_sell_in(self, name):
        for item in self.items:
            if item.name == name:
                return item.sell_in
    
    def get_item_quality(self, name):
        for item in self.items:
            if item.name == name:
                return item.quality