import os


class FlowerDictionary:
    def __init__(self):
        pass

    def getlabel(self, imagePath):
        label = os.path.splitext(imagePath.split("_")[-1])[0]
        labeltoint = int(label)
        if 1 <= labeltoint <= 79:           # 1 71 data
            return "Daffodil"
        elif 80 <= labeltoint <= 160:       # 2 50 data
            return "Snowdrop"
        elif 161 <= labeltoint <= 200:      # 3 17 data
            return "Lily Valley"
        elif 201 <= labeltoint <= 320:      # 4 28 data
            return "Bluebell"
        elif 321 <= labeltoint <= 400:      # 5 50 data
            return "Crocus"
        elif 401 <= labeltoint <= 480:      # 6 78 data
            return "Iris"
        elif 481 <= labeltoint <= 560:      # 7 49 data
            return "Tigerlily"
        elif 561 <= labeltoint <= 640:      # 8 41 data
            return "Tulip"
        elif 641 <= labeltoint <= 720:      # 9 65 data
            return "Fritillary"
        elif 721 <= labeltoint <= 800:      # 10 71 data
            return "Sunflower"
        elif 801 <= labeltoint <= 880:      # 11 57 data
            return "Daisy"
        elif 881 <= labeltoint <= 950:      # 12 43 data
            return "Colts\'Foot"
        elif 951 <= labeltoint <= 1120:     # 13 55 data
            return "Dandelion"
        elif 1121 <= labeltoint <= 1200:    # 14 54 data
            return "Buttercup"
        elif 1201 <= labeltoint <= 1280:    # 15 61 data
            return "Windflower"
        elif 1281 <= labeltoint <= 1400:    # 16 56 data
            return "Pansy"
        return label
