""" Abstract Methods
    1. Declared by Python Interface
    2. May Not Have a Useful Implementation
    3. Must be Overriden by Concrete Class
    4. Use the @abc.abstractmethod Decorator
"""

import abc

class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass, load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))
    
    @abc.abstractmethod
    def load_data_source(self, path: str, file_name: str):
        """Load in the data set"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def extract_text(self, full_file_path: str):
        """Extract text from the data set"""
        raise NotImplementedError
    
class PdfParserFormal(FormalParserInterface):
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalparserInterface.extract_text()"""
        pass

class EmlParserFormal(FormalParserInterface):
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in Emlparser.
        Does not override FormalParserInterface.extract_text()"""
        pass

print(issubclass(PdfParserFormal, FormalParserInterface))

print(issubclass(EmlParserFormal, FormalParserInterface))

pdf_parser = PdfParserFormal()
eml_parser = EmlParserFormal()