from typing import Optional

from presidio_anonymizer.operators.operator import Operator


class Initial(Operator):
    """Initial operator that converts names to initials while preserving leading characters."""

    def operator_name(self) -> str:
        return "initial"

    def operate(self, text: str, params: Optional[dict] = None) -> str:
        
        if not text:
            return ""
        
        # Split into words (this automatically handles extra whitespace)
        words = text.split()
        initials = []
        
        for word in words:
            if word:  # Skip empty strings
                # Find the first alphanumeric character position
                first_alnum_pos = -1
                for i, char in enumerate(word):
                    if char.isalnum():
                        first_alnum_pos = i
                        break
                
                if first_alnum_pos >= 0:
                    # Preserve everything before the first alphanumeric character
                    prefix = word[:first_alnum_pos]
                    initial_char = word[first_alnum_pos].upper()
                    initials.append(f"{prefix}{initial_char}.")
                else:
                    # If no alphanumeric character found, use the first character
                    initials.append(f"{word[0]}.")
        
        return " ".join(initials)

    def validate(self, params: Optional[dict] = None) -> None:
        """No special parameters needed for Initial yet, so nothing to validate."""
        return

    def operator_type(self):
        """This is an anonymization operator (not a deanonymizer)."""
        from presidio_anonymizer.operators.operator import OperatorType
        return OperatorType.Anonymize