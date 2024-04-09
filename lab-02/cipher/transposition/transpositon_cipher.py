class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ""
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        num_rows = (len(text) + key - 1) // key
        num_cols = (len(text) + num_rows - 1) // num_rows
        
        num_short_cols = (num_rows * num_cols) - len(text)
        decrypted_text = [''] * num_rows

        row = col = 0
        for symbol in text:
            decrypted_text[row] += symbol
            row += 1
            if (row == num_rows) or (row == num_rows - 1 and col >= num_cols - num_short_cols):
                row = 0
                col += 1
        
        # Reconstruct the text by reading characters from columns
        reconstructed_text = ""
        for row in range(num_rows):
            for col in range(num_cols):
                if col < len(decrypted_text[row]):
                    reconstructed_text += decrypted_text[row][col]
        
        return reconstructed_text
    
    