"""Módulo para traduzir texto entre inglês e francês usando o MyMemoryTranslator."""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Traduz texto do inglês para o francês usando o MyMemoryTranslator.
    Args:
        english_text (str): O texto em inglês a ser traduzido.
    Returns:
        str: O texto traduzido para o francês.
    """
    translator = MyMemoryTranslator(source='en-GB', target='fr-FR')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """Traduz texto do francês para o inglês usando o MyMemoryTranslator.
    Args:
        french_text (str): O texto em francês a ser traduzido.
    Returns:
        str: O texto traduzido para o inglês.
    """
    translator = MyMemoryTranslator(source='fr-FR', target='en-GB')
    english_text = translator.translate(french_text)
    return english_text
