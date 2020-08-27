def decrement_quality(item): 
    if item.quality > 0:
        item.quality -= 1

def increment_quality(item): 
    if item.quality < 50:
        item.quality += 1

class GildedRose(object):

    SULFURAS = "Sulfuras, Hand of Ragnaros"
    BRIE = "Aged Brie"
    BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            name = item.name
            if name != GildedRose.BRIE and name != GildedRose.BACKSTAGE and name != GildedRose.SULFURAS:
                decrement_quality(item)
            elif item.quality < 50:
                item.quality += 1
                if name == GildedRose.BACKSTAGE:
                    if item.sell_in < 11:
                        increment_quality(item)
                    if item.sell_in < 6:
                        increment_quality(item)
            if name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1
            if item.sell_in < 0:
                if name != GildedRose.BRIE:
                    if name != GildedRose.BACKSTAGE:
                        if name != GildedRose.SULFURAS:
                            decrement_quality(item)
                    else:
                        item.quality = 0
                else:
                    increment_quality(item)