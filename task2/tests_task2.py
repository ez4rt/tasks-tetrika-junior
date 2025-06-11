import unittest
from unittest.mock import patch, Mock, MagicMock
import requests
from collections import defaultdict
from main import fetch_html, parse_page, save_to_csv


class TestFetchHtml(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_html_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b'<html>...</html>'
        mock_get.return_value = mock_response

        result = fetch_html('https://example.com')
        self.assertEqual(result, b'<html>...</html>')

    @patch('requests.get')
    def test_fetch_html_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException('Network error')
        result = fetch_html('https://example.com')
        self.assertIsNone(result)


class TestParsePage(unittest.TestCase):
    def setUp(self):
        self.html_content = """
        <div class="mw-category-group">
            <ul>
                <li><a title="Акула" href="/wiki/Акула"></a></li>
                <li><a title="Категория:Млекопитающие" href="/wiki/Млекопитающие"></a></li>
                <li><a title="Белка" href="/wiki/Белка"></a></li>
            </ul>
        </div>
        <a href="/wiki/Следующая_страница">Следующая страница</a>
        """

    def test_parse_page_success(self):
        animal_count = defaultdict(int)
        next_url = parse_page(self.html_content, animal_count)

        self.assertEqual(animal_count['А'], 1)
        self.assertEqual(animal_count['Б'], 1)
        self.assertEqual(next_url, 'https://ru.m.wikipedia.org/wiki/Следующая_страница')

    def test_parse_page_no_next(self):
        html_content = self.html_content.replace('Следующая страница', '')
        animal_count = defaultdict(int)
        next_url = parse_page(html_content, animal_count)

        self.assertIsNone(next_url)

    def test_parse_page_empty(self):
        animal_count = defaultdict(int)
        next_url = parse_page('', animal_count)

        self.assertIsNone(next_url)
        self.assertEqual(len(animal_count), 0)


class TestSaveToCsv(unittest.TestCase):
    def test_save_to_csv(self):
        data = {'А': 10, 'Б': 5, 'В': 2}

        mock_file = MagicMock()
        mock_file.__enter__.return_value = mock_file

        with patch('builtins.open', return_value=mock_file) as mock_open:
            save_to_csv(data)

        mock_open.assert_called_once_with('beasts.csv', mode='w', newline='')


if __name__ == '__main__':
    unittest.main()
