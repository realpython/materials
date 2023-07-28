from playwright.sync_api import sync_playwright


def take_screenshot(target, session_dict):
    with sync_playwright() as playwright:
        webkit = playwright.webkit
        browser = webkit.launch()
        browser_context = browser.new_context(device_scale_factor=2)
        browser_context.add_cookies([session_dict])
        page = browser_context.new_page()
        page.goto(target)
        screenshot_bytes = page.locator(".code").screenshot()
        browser.close()
        return screenshot_bytes
