# src/preprocessor.py

def basic_clean(text):
    """
    Basic cleaning for initial testing.
    Converts to lowercase and strips extra spaces.
    """
    if not isinstance(text, str):
        return ""

    text = text.lower().strip()
    return text


# Test when running directly
if __name__ == "__main__":
    sample = "Hello USER, CLICK here to win a prize!"
    print("Original:", sample)
    print("Cleaned:", basic_clean(sample))
