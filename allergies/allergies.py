class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergyCode = {1: 'eggs',
                            2: 'peanuts',
                            4: 'shellfish',
                            8: 'strawberries',
                            16: 'tomatoes',
                            32: 'chocolate',
                            64: 'pollen',
                            128: 'cats'}

    def lst(self):
        allergyNum = []
        allergyValues = sorted(self.allergyCode.keys())
        while self.score > 0:
            candidate = max([x for x in allergyValues if x <= self.score])
            self.score = self.score - candidate
            allergyNum.append(candidate)
        allergyNum
        allergyList = [self.allergyCode[key] for key in allergyNum]
        return allergyList

    def is_allergic_to(self, allergen):
        return allergen in self.lst()