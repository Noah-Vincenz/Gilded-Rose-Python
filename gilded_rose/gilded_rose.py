def decrement_quality(item): 
    if item.quality > 0:
        item.quality -= 1

def increment_quality(item): 
    if item.quality < 50:
        item.quality += 1

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            name = item.name
            if name != "Aged Brie" and name != "Backstage passes to a TAFKAL80ETC concert" and name != "Sulfuras, Hand of Ragnaros":
                decrement_quality(item)
            elif item.quality < 50:
                item.quality += 1
                if name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        increment_quality(item)
                    if item.sell_in < 6:
                        increment_quality(item)
            if name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1
            if item.sell_in < 0:
                if name != "Aged Brie":
                    if name != "Backstage passes to a TAFKAL80ETC concert":
                        if name != "Sulfuras, Hand of Ragnaros":
                            decrement_quality(item)
                    else:
                        item.quality = 0
                else:
                    increment_quality(item)