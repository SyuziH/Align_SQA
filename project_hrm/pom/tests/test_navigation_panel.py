import pytest
from seleniumPython.Align_SQA.project_hrm.pom.pages.navigation_panel import NavigationPanel


@pytest.mark.usefixtures("log_in")
class TestNavigationPanel:

    def test_recruitment_page(self):
        navigation_panel = NavigationPanel(self.driver)
        navigation_panel.wait_for_page_load()
        navigation_panel.go_to("Recruitment")
        assert navigation_panel.find_navigated_page(NavigationPanel.PAGE_IS_VISIBLE_RECRUITMENT)
