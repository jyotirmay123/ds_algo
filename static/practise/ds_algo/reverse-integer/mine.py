class Solution:
    def reverse(self, x: int) -> int:
        if x > (2 ** 31) - 1 or x < -(2 ** 31):
            return 0

        x_s = str(x)
        if x_s[0] == '-' or x_s[0] == '+':
            x_tr = x_s[1:]
            signed = x_s[0]
        else:
            x_tr = x_s
            signed = ''

        def print_reverse(xt):
            if len(xt) == 0:
                return xt

            return print_reverse(xt[1:]) + xt[0]

        out = print_reverse(x_tr)

        if len(out) > 1:
            for idx, o in enumerate(out):
                if o is '0':
                    continue
                elif o is not '0':
                    out = out[idx:]
                    break
        final_out = int(signed + out)
        if final_out > (2 ** 31) - 1 or final_out < -(2 ** 31):
            return 0

        return final_out