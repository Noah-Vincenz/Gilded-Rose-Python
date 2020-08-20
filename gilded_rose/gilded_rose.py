class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            name = item.name
            if (name != "Aged Brie" and name != "Backstage passes to a TAFKAL80ETC concert" and name != "Sulfuras, Hand of Ragnaros") and (item.quality > 0):
                item.quality -= 1
            elif item.quality < 50:
                item.quality += 1
                if name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality += 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality += 1
            if name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1
            if item.sell_in < 0:
                if name != "Aged Brie":
                    if name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if name != "Sulfuras, Hand of Ragnaros":
                                item.quality -= 1
                    else:
                        item.quality = 0
                elif item.quality < 50:
                    item.quality += 1
