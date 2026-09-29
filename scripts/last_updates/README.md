# Page last-update dates

The page last-update dates displayed by RSQKit are generated from the Git
history of the Markdown files under `pages/`.

For the August 2026 release, regeneration is deliberately manual so that this
feature does not require changes to the GitHub Actions build. This is a
transitional arrangement: the same generator can later run automatically in a
build with access to the complete Git history.

Page changes must be committed before generating the dates. From the repository
root, run:

```bash
python scripts/generate_last_updates.py
```

Commit `_data/last_updates.yml` if it changes. Do not edit the generated file or
add manually maintained last-update fields to individual pages.
