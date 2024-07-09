from commonElements.elements import elements

class iframes(elements):
    def __init__(self, driver):
        self.driver = driver
    
    def switchToIframe(self, locator):
        iframe = self.getElement(locator)
        self.driver.switch_to.frame(iframe)
    
    def switchToDefaultContent(self):
        self.driver.switch_to.default_content()
    
    def validateIframeContentText(self, iframeLocator, contentLocator, expectedContent):
        self.switchToIframe(iframeLocator)
        content = self.getElement(contentLocator).text
        self.switchToDefaultContent()
        assert content == expectedContent, f"Iframe content should be {expectedContent}, but instead is {content}."
        print(f"Iframe content validated successfully: '{expectedContent}'")
