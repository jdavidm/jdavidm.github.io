from playwright.sync_api import Page, expect, sync_playwright

def verify_software_page(page: Page):
    page.goto("http://localhost:8000/software.html")

    # Check that Software header and content exists
    expect(page.get_by_role("heading", name="Software")).to_be_visible()

    # Check that the main content div is constrained/centered (not full screen width)
    # The new version uses 'container' class which has max-width

    # Take a screenshot
    page.screenshot(path="/home/jules/verification/fixed-software.png", full_page=True)
    print("Screenshot saved to /home/jules/verification/fixed-software.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 1000})
        try:
            verify_software_page(page)
        finally:
            browser.close()
