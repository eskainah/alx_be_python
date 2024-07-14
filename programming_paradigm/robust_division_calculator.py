def safe_divide(numerator, denominator):
    try: 
        num = float(numerator)
        d_nom = float(denominator)
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            quotient = num / d_nom
        return f"The quotient is: {quotient:.1f}"
    except ValueError:
        print(f"Error: Please enter numeric values only.")