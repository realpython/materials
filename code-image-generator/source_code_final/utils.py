from playwright.sync_api import sync_playwright


def make_screenshot(target, session_dict=None):
    with sync_playwright() as playwright:
        webkit = playwright.webkit
        browser = webkit.launch()
        browser_context = browser.new_context(device_scale_factor=2)
        if session_dict:
            browser_context.add_cookies([session_dict])
        page = browser_context.new_page()
        page.goto(target)
        screenshot_bytes = page.locator(".code_block").screenshot()
        browser.close()
        return screenshot_bytes
