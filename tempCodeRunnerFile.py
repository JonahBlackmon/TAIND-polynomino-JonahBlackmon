    length, width = piece.piece.shape
            ex = x+width
            ey = y + length
            self.base[y:ey, x:ex] -= piece.piece