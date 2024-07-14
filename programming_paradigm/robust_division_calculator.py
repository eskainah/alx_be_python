def safe_divide(numerator, denominator):
    try: 
        num = float(numerator)
        d_nom = float(denominator)
        if denominator == 0:
            raise ZeroDivisionError("You cannot divide by 0")
        return f"The quotient is: {num/d_nom:.1f}"
    except ValueError:
        print(f"The {denominator} is invalid")