def safe_divide(numerator, denominator):
    try: 
        num = float(numerator)
        d_nom = float(denominator)
        if d_nom == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {num / d_nom:.1f}"
    except ValueError:
        print(f"Error: Please enter numeric values only.")