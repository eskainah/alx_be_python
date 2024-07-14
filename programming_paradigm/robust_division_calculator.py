def safe_divide(numerator, denominator):
    try: 
        num = float(numerator)
        d_nom = float(denominator)
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        return f"The quotient is: {num/d_nom:.1f}"
    except ValueError:
        print(f"Error: Please enter numeric values only.")