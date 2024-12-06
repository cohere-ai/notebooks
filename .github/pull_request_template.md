# Pull Request

## Type of Change
Please select one:
- [ ] New notebook
- [ ] Notebook update
- [ ] Documentation update
- [ ] Environment/dependency update
- [ ] Other

## Description
[What changes does this PR make?]

## Testing
[Describe how you've verified these changes work]

### For Notebooks:
- Include a screen recording showing execution and outputs
- Or include screenshots of key outputs with explanation

### For Documentation:
- Preview any markdown changes
- Test any new links or references

## Notebook Changes Checklist
Complete if modifying notebooks:
- [ ] I have run the notebook from start to finish without errors
- [ ] I have cleared all cell outputs before committing
- [ ] I have included all required pip installations with pinned versions (e.g., pip install package==1.2.3) in %%sh cells at the start of the notebook
- [ ] I have included a screen recording or screenshots demonstrating the changes
- [ ] I have added sufficient markdown cells to explain the notebook's purpose and usage

## Documentation Changes Checklist
Complete if modifying documentation:
- [ ] I have checked for similar wording/style issues across all documentation
- [ ] I have verified all links and references still work
- [ ] I have previewed how the changes will appear
- [ ] I have followed the repository's documentation style guide (if applicable)

## Related Issues
[Add any related issue numbers (e.g., Fixes #123)]

---

> **Note for notebook submissions:**
> - Run the notebook in a fresh environment (e.g., new conda env or colab instance) to ensure all dependencies are captured
> - Comments should explain the purpose of non-obvious code blocks and any external data dependencies

> **Note for documentation updates:**
> - For minor changes, consider bundling multiple related improvements in one PR
> - Look for opportunities to improve similar sections across the documentation
