import pytest

from coding_interview.arrays_and_strings.url_ify import count_spaces, url_ify


@pytest.mark.parametrize("sentence,length,output", [
    ('the sky is blue       ', 15, 'the%20sky%20is%20blue '),
    ('YES NO   ', 6, 'YES%20NO ')
])
def test_url_ify(sentence, length, output):
    assert url_ify(sentence=sentence, length=length) == output


@pytest.mark.parametrize("sentence,length,output", [
    (list('the sky is blue       '), 15, 3),
    (list('YES NO   '), 6, 1)
])
def test_count_spaces(sentence, length, output):
    assert count_spaces(sentence=sentence, length=length) == output
