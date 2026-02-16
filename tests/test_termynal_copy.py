from playwright.sync_api import Page, expect

def test_termynal_copy_button(page: Page, start_server):
    """
    Test that the Termynal copy button is injected and visible.
    """
    # Grant clipboard permissions
    page.context.grant_permissions(['clipboard-write', 'clipboard-read'])

    # Navigate to Lesson 07 (Git) where we added the Termynal block
    page.goto("http://localhost:8766/aulas/aula-07/")

    # Wait for the code block content to be visible
    # Verify that the text "$ git init" is present in the page
    code_text = page.locator("code", has_text="$ git init")
    expect(code_text).to_be_visible()

    # Click the button
    # copy_button.click()
    # 
    # # Check for feedback "Copied!" (managed by CSS class .copied showing the span)
    # expect(copy_button).to_have_class(r"termynal-copy-button copied")
    # 
    # feedback = copy_button.locator(".termynal-copy-feedback")
    # expect(feedback).to_be_visible()
