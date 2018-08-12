from images_page import ImagesPage
from search_page import SearchPage


# @pytest.mark.skip(reason="test")
def test_google_search(driver):
    search_page = SearchPage(driver).open()
    results_page = search_page.search_for("python")
    link_text = results_page.get_result_link_text(1)
    assert "python" in link_text


def test_google_images(driver):
    search_page = SearchPage(driver).open()
    results_page = search_page.search_for("python")
    images_page = results_page.switch_to_images_page()
    images = images_page.get_elements(ImagesPage.image)[:5]
    for image in images:
        assert image.is_displayed()
