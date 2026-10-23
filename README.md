# Final Project

[![Notebook check](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml)

## Team Members

🦸
🦹

## Description

<!-- Replace this section with your question, your main findings, and links to your web page or dashboard. -->

For the final project, you will ask a global change question of your choosing and answer it with
the tools we have used this semester: tabular data with `pandas` and `ibis`, spatial vector and
raster data with interactive maps in `leafmap`, and text as data with classifiers, retrieval or
structured extraction. Good results deserve good communication, so the emphasis is on a clear
story in your own words, well-designed figures and maps, and a web page or dashboard that a
reader outside the class could follow.

## What to hand in

- [`proposal.md`](proposal.md), by the proposal deadline.
- Your analysis in one or more notebooks, run from top to bottom.
- `prompts/`: your conversations with your coding agent, exported as files.
- Optionally, a web page in [`web/`](web/), published to GitHub Pages on every push to `main`,
  and a dashboard or app.
- An updated README with a statement on AI use.

See the [rubric](rubric.md) for how the project is graded.

## Setup

List the packages your project uses in `requirements.txt`, and delete the ones it does not.
Never put API keys or tokens in a notebook or commit them; read them from the environment.

GitHub Actions runs two workflows on every push. The notebook check confirms that notebooks are
valid, every code cell parses, and no credentials are committed; it does not run the notebooks.
The site workflow publishes the `web/` folder to GitHub Pages.

## Links

[🌐 Course Website](https://espm-157.carlboettiger.info/)
