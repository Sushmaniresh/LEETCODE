class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # handle zero numerator
        if numerator == 0:
            return "0"
        
        # sign
        negative = (numerator < 0) ^ (denominator < 0)
        
        # work with absolute values (Python handles big ints)
        num = abs(numerator)
        den = abs(denominator)
        
        # integer part
        integer_part = num // den
        rem = num % den
        
        result = "-" + str(integer_part) if negative else str(integer_part)
        
        # if no fractional part
        if rem == 0:
            return result
        
        # fractional part
        result += "."
        frac_digits = []
        seen = {}  # remainder -> index in frac_digits
        
        while rem != 0:
            # if this remainder was seen before, repetition starts at seen[rem]
            if rem in seen:
                idx = seen[rem]
                # insert '(' at idx, and ')' at end
                non_repeating = "".join(frac_digits[:idx])
                repeating = "".join(frac_digits[idx:])
                result += non_repeating + "(" + repeating + ")"
                return result
            
            # mark where this remainder appears in the fraction string
            seen[rem] = len(frac_digits)
            
            rem *= 10
            digit = rem // den
            frac_digits.append(str(digit))
            rem = rem % den
        
        # terminated (no repetition)
        result += "".join(frac_digits)
        return result

   

        
        