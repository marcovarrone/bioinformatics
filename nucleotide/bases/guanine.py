from nucleotide.bases.type.purine import Purine


class Guanine(Purine):
    def __init__(self):
        super(Guanine, self).__init__("G")

    def __str__(self):
        return self.symbol