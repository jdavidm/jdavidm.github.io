from playwright.sync_api import Page, expect, sync_playwright

def verify_publications_page(page: Page):
    page.goto("http://localhost:8000/publications.html")
    page.wait_for_selector(".pub-grid")

    expect(page.get_by_role("heading", name="Working Papers")).to_be_visible()

    # Save a screenshot to confirm it's fixed
    page.screenshot(path="/home/jules/verification/fixed-pubs.png", full_page=True)
    print("Screenshot saved to /home/jules/verification/fixed-pubs.png")

if __name__ == "__main__":
    import subprocess
    import time

    # ensure server is running
    # We will assume it's running on 8000 from before, or restart it

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 2000})
        try:
            verify_publications_page(page)
        finally:
            browser.close()
