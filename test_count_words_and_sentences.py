import pytest
import os
from main import count_words_and_sentences

@pytest.fixture
def file_1(tmp_path):
    file_path = tmp_path / 'test_file_1.txt'
    file_path.write_text("Файл з одним реченням.")
    return file_path

@pytest.fixture
def file_2(tmp_path):
    file_path = tmp_path / 'test_file_2.txt'
    file_path.write_text("Два!     Речення.")
    return file_path

@pytest.fixture
def file_3(tmp_path):
    file_path = tmp_path / 'test_file_3.txt'
    file_path.write_text("Два! Речення")
    return file_path

@pytest.fixture
def file_4(tmp_path):
    file_path = tmp_path / 'test_file_4.txt'
    file_path.write_text("БезНіякихЗнаківРечення")
    return file_path

@pytest.fixture
def file_5(tmp_path):
    file_path = tmp_path / 'test_file_5.txt'
    file_path.write_text("Тут! Дуже, багато: розділових... Знакііііів,,,,,,,, чи не так?")
    return file_path

@pytest.mark.parametrize("file_fixture, expected_word_count, expected_sentence_count", [
    ('file_1', 4, 1),
    ('file_2', 2, 2),
    ('file_3', 2, 2),
    ('file_4', 1, 1),
    ('file_5', 8, 3),])
def test_count_words_and_sentences(request, file_fixture, expected_word_count, expected_sentence_count):
    file_path = getattr(request, 'getfixturevalue')(file_fixture)
    
    word_count, sentence_count = count_words_and_sentences(file_path)
    
    assert word_count == expected_word_count
    assert sentence_count == expected_sentence_count
