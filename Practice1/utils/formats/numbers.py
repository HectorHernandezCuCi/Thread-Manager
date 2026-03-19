def format_number_input(e):
    """Adds thousand separators and filters out non-numeric characters."""
    clean_value = "".join(filter(str.isdigit, e.control.value))
    if clean_value:
        e.control.value = f"{int(clean_value):,}"
    else:
        e.control.value = ""
    e.control.update()

def get_int(control):
    """Converts formatted string (1,000) back to integer (1000)."""
    try:
        # We handle the case where the control might be empty or None
        val = control.value if control.value else "0"
        return int(val.replace(",", ""))
    except (ValueError, AttributeError):
        return 0