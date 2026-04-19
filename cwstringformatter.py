import pyperclip

def format_kenwood_cw(text):
    # Requirements check: Remove newlines and ensure it's a clean string
    text = text.replace('\n', ' ').replace('\r', '')
    
    # Chunking into 24-character segments
    chunk_size = 24
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    
    formatted_segments = []
    
    for i, chunk in enumerate(chunks):
        # Requirement 2: Pad the last chunk with spaces if it's under 24 chars
        if len(chunk) < chunk_size:
            chunk = chunk.ljust(chunk_size)
            
        # Requirement 3: Prepend RI;KY to the first, and KY to the rest
        # Note: 'RI;' is the radio information/interrupt command often used 
        # to clear or initialize the buffer sequence.
        if i == 0:
            formatted_segments.append(f"RI:KY {chunk};")
        else:
            formatted_segments.append(f"KY {chunk};")
            
    # Combine all segments into one string for the clipboard
    return "".join(formatted_segments)

def main():
    print("--- Kenwood TS-590SG CW Buffer Formatter ---")
    print("Paste your text below and press Enter (or just press Enter to use current Clipboard):")
    
    user_input = input("> ").strip()
    
    # Requirement 1: Support pasting from Windows Clipboard if input is empty
    if not user_input:
        user_input = pyperclip.paste()
        print(f"Using text from clipboard: {user_input[:50]}...")

    if not user_input:
        print("No text found in input or clipboard. Exiting.")
        return

    result = format_kenwood_cw(user_input)
    
    # Requirement 4: Display and paste to clipboard
    print("\nFormatted String:")
    print("-" * 30)
    print(result)
    print("-" * 30)
    
    pyperclip.copy(result)
    print("\nSuccess! The formatted string is now on your Windows clipboard.")

if __name__ == "__main__":
    main()