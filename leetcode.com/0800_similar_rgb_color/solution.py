class Solution:
    def similarRGB(self, color: str) -> str:
        a = [
            '0x00', '0x11', '0x22', '0x33', '0x44', '0x55', '0x66', '0x77',
            '0x88', '0x99', '0xaa', '0xbb', '0xcc', '0xdd', '0xee', '0xff',
        ]

        m = float('-inf')
        x, y, z = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)

        for i in a:
            for j in a:
                for k in a:
                    v = - (x - int(i, 16))**2 \
                        - (y - int(j, 16))**2 \
                        - (z - int(k, 16))**2

                    if v > m:
                        m = v
                        r = f'#{i[2:]}{j[2:]}{k[2:]}'

        return r
