#!/usr/bin/env python3

class Diamond:
    def getDiamond(self, vradius):
        linesToPrint = []
        stars = 1
        padding = vradius - stars

        for n in range(1, vradius * 2):
            line = " " * padding + "*" * stars
            linesToPrint.append(line)

            if n < vradius:
                padding -= 1
                stars += 2
            else:
                padding += 1
                stars -= 2

        return linesToPrint