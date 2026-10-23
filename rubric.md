# Final Project Rubric

Total: 30 points. The core elements are worth 20 points and every project is graded on them.
The remaining 10 points come from the optional elements, at up to 5 points each. Choose the ones
that fit your question; most projects will draw on two or three. Points earned on additional
optional elements can make up points lost elsewhere, up to the 30-point total.

Exceptional work on any element can earn up to 2 bonus points.

## Core elements (20 points)

### 1. Proposal (**2 points**)

`proposal.md` is turned in on time. It names the team, states a global change question, links
to the data sources, lists three analysis tasks, and says which of the optional elements the
project plans to use.

### 2. Narrative (**6 points**)

The project tells a clear story that a reader outside the class could follow, written in your
own words.

  - It explains the global change question and why it matters, with references where
    appropriate.
  - It explains the methods in plain language: where the data come from, what was done to them,
    and why.
  - It describes each figure, map or table ("the map shows...") and says what a reader should
    take from it.
  - It ends with a conclusion: what you found, how confident you are in it, and what you would do
    next.
  - Instructor headings are replaced with topical headings. The text is concise; length is not a
    virtue.

### 3. Presentation (**4 points**)

Figures, maps and tables communicate the results clearly.

  - Every figure has labeled axes, units, a legend where needed, and a caption written as a
    sentence.
  - The chart type fits the data, and the layout is deliberate. Visuals avoid clutter and
    overplotting.
  - A reader can follow the results from the rendered page or notebook without running any code.

### 4. Code (**4 points**)

The code is concise, readable, and reproducible.

  - Data are read from their original sources by URL or API, not from files downloaded by hand.
  - Code uses the high-level tools from the course (`ibis`, `plotnine`, `leafmap`, and so on)
    rather than more verbose workarounds.
  - Code avoids common model-generated clutter: no `print` statements in place of displayed
    values, no unnecessary `try` blocks or function definitions, no commented-out code, and few
    comments. Variable names and markdown cells explain the logic instead.
  - Each cell does one clear task. The notebook runs from top to bottom.

### 5. GitHub (**2 points**)

  - The README names the authors, describes the question and the findings, and links to any web
    page or dashboard.
  - The repository passes the notebook check on GitHub Actions, and the badge in the README is
    green.
  - Commits show how the work developed, with clear messages. Files have logical names.

### 6. Process and AI use (**2 points**)

  - The repository includes your conversations with your coding agent, exported to `prompts/`.
  - The README or notebook ends with a short statement on AI use: which models you used, for what,
    what they got wrong, and what you contributed beyond accepting their output.
  - The project is honest about who made each judgment. Output produced by a model is described
    as such, and your own reading is described as yours.

## Optional elements (up to 5 points each)

### A. Tabular data at scale

The project uses `ibis` on DuckDB to filter, join, group and aggregate tabular data, including
data larger than fits comfortably in memory. Claims about speed or memory are supported by
measurements.

### B. Vector data

The project reads and manipulates spatial vector data (with `ibis` spatial functions or
`geopandas`), including at least one spatial operation such as a spatial join, overlay or
distance calculation.

### C. Raster data

The project finds raster data through a STAC search, computes a derived quantity with a streaming
approach, and summarizes it, for example with zonal statistics over vector boundaries.

### D. Interactive maps

The project includes an interactive map made with `leafmap.maplibregl` that has at least two
layers, a legend, and a sensible starting view. The map supports the argument and is described
in the text.

### E. Text as data

The project treats documents as data, using one or more of regular expressions, classifiers
(such as Laya), embeddings and retrieval-augmented generation, or structured extraction with a
schema. Model outputs are compared against the source text, and the project documents cases
where the model was wrong.

### F. Verification against an independent source

At least one result is reconciled against an independent published source. The project
establishes what each source measures before comparing them, and the direction and size of any
discrepancy are quantified and explained.

### G. Web page

The project is published as a web page from the `web/` folder to GitHub Pages. A reader can
understand the question, the main figures or maps, and the conclusion from the page alone. The
README links to it.

### H. Dashboard or app

The project includes an interactive dashboard or app, as covered in module 4, that lets a reader
explore the results. It is published or can be launched from instructions in the README, and it
is linked from the README.

## Failure conditions

The project fabricates data, or presents made-up or "example" numbers, quotations or citations
as if they came from the sources. (Automatic fail)

This applies without change to output from a language model. Models sometimes produce plausible
numbers, quotations or references that are not in the sources. Passing those along as real is the
same failure whether you typed them or accepted them.

The project presents a model's judgment as your own. Using a model is allowed. Misrepresenting who
made the judgment is not.
