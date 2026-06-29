import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


class TestCapitalize:
    def test_positive_lowercase(self, utils):
        """Позитивный тест: обычная строка в нижнем регистре"""
        assert utils.capitalize("skypro") == "Skypro"

    def test_positive_mixed_case(self, utils):
        """Позитивный тест: строка с уже заглавной буквой"""
        assert utils.capitalize("Skypro") == "Skypro"

    def test_positive_single_letter(self, utils):
        """Позитивный тест: одна буква"""
        assert utils.capitalize("a") == "A"

    def test_negative_empty_string(self, utils):
        """Негативный тест: пустая строка"""
        assert utils.capitalize(" ") == " "

    def test_negative_with_numbers(self, utils):
        """Позитивный тест: строка с цифрами"""
        assert utils.capitalize("123abc") == "123abc"


class TestTrim:
    def test_positive_spaces_at_start(self, utils):
        """Позитивный тест: пробелы только в начале"""
        assert utils.trim("   skypro") == "skypro"

    def test_positive_no_spaces(self, utils):
        """Позитивный тест: строка без пробелов"""
        assert utils.trim("skypro") == "skypro"

    def test_positive_multiple_spaces(self, utils):
        """Позитивный тест: несколько пробелов подряд"""
        assert utils.trim("    skypro") == "skypro"

    def test_negative_spaces_at_end(self, utils):
        """Негативный тест: пробелы в конце"""
        assert utils.trim("skypro   ") == "skypro   "

    def test_negative_empty_string(self, utils):
        """Негативный тест: пустая строка"""
        assert utils.trim("") == ""

    def test_negative_only_spaces(self, utils):
        """Негативный тест: строка состоит только из пробелов"""
        assert utils.trim("    ") == ""


class TestContains:
    def test_positive_symbol_exists(self, utils):
        """Позитивный тест: символ есть в строке"""
        assert utils.contains("SkyPro", "S")

    def test_positive_symbol_exists_lowercase(self, utils):
        """Позитивный тест: символ есть в строке"""
        assert utils.contains("SkyPro", "o")

    def test_negative_symbol_not_exists(self, utils):
        """Негативный тест: символа нет в строке"""
        assert utils.contains("SkyPro", "U") is False

    def test_negative_empty_string_search(self, utils):
        """Негативный тест: поиск в пустой строке"""
        assert utils.contains(" ", "a") is False

    def test_negative_empty_symbol(self, utils):
        """Негативный тест:поиск пустой строки как символа (поведение index)"""
        assert utils.contains("SkyPro", "")

    def test_negative_long_substring(self, utils):
        """Негативный тест"""
        assert utils.contains("SkyPro", "ky")
