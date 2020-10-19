from ui.pages.base_page import BasePage


class CreateSegmentPage(BasePage):

    def create_segment(self, name, segment_xpath):
        """Создаем новый или первый сегмент"""
        self.click(self.main_page_locators.CAMPAIGNS)
        self.wait()
        self.find(self.create_segment_locators.ALL_SEGMENTS).click()
        self.wait()
        try:
            self.click(self.create_segment_locators.CREATE_NEW_SEGMENT)
        except:
            self.click(self.create_segment_locators.CREATE_FIRST_SEGMENT)
        self.click(self.create_segment_locators.APP_AND_GAMES)
        self.click(self.create_segment_locators.PLAYED_AND_PAID)
        self.click(self.create_segment_locators.PAID_ON_PLATFORM)
        self.click(self.create_segment_locators.ADD_SEGMENT)
        self.click(self.create_segment_locators.NEW_SEGMENT_NAME)
        self.field_entry(self.create_segment_locators.NEW_SEGMENT_NAME, name)
        self.click(self.create_segment_locators.CREATE_NEW_SEGMENT)
        self.wait()
        return self.find(segment_xpath)

    def delete_segment(self, delete_segment_cross_xpath):
        """Удаляем сегмент"""
        self.click(self.create_segment_locators.ALL_SEGMENTS)
        self.click(delete_segment_cross_xpath)
        self.click(self.create_segment_locators.DELETE_SEGMENT)
        self.find(self.create_segment_locators.ALL_SEGMENTS).click()
        return self.find(delete_segment_cross_xpath)
