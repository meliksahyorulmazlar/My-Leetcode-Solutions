class Solution:
    def romanToInt(self, s: str) -> int:
        i_count = s.count("I")
        v_count = s.count("V")
        x_count = s.count("X")
        l_count = s.count("L")
        c_count = s.count("C")
        d_count = s.count("D")
        m_count = s.count("M")

        iv_count = s.count("IV")
        i_count -= iv_count
        v_count -= iv_count

        ix_count = s.count("IX")
        i_count -= ix_count
        x_count -= ix_count

        xl_count = s.count("XL")
        x_count -= xl_count
        l_count -= xl_count

        xc_count = s.count("XC")
        x_count -= xc_count
        c_count -= xc_count

        cd_count = s.count("CD")
        c_count -= cd_count
        d_count -= cd_count

        cm_count = s.count("CM")
        c_count -= cm_count
        m_count -= cm_count

        total = 0
        total += (1*i_count)
        total += (5*v_count)
        total += (10*x_count)
        total += (50*l_count)
        total += (100*c_count)
        total += (500*d_count)
        total += (1000*m_count)

        total += (4*iv_count)
        total += (9*ix_count)
        total += (40*xl_count)
        total += (90*xc_count)
        total += (400*cd_count)
        total += (900*cm_count)

        return total