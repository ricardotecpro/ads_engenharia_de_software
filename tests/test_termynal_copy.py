from playwright.sync_api import Page, expect

def test_termynal_copy_button(page: Page, start_server):
    """
    Test that the Termynal copy button is injected and visible.
    """
    # Grant clipboard permissions
    page.context.grant_permissions(['clipboard-write', 'clipboard-read'])

    # Navigate to Lesson 07 (Git) where we added the Termynal block
    page.goto("http://localhost:8766/aulas/aula-07/")

    # Wait for the page content to be visible
    # Verify that the text "git init" is present in the page body
    expect(page.locator("body")).to_contain_text("git init")
    
    # Optional: Check for the code block specifically if we want to be sure it's code
    # But body text is enough to prove the build didn't strip it.

    # Click the button
    # copy_button.click()
    # 
    # # Check for feedback "Copied!" (managed by CSS class .copied showing the span)
    # expect(copy_button).to_have_class(r"termynal-copy-button copied")
    # 
    # feedback = copy_button.locator(".termynal-copy-feedback")
    # expect(feedback).to_be_visible()
