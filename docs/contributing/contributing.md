# Contributing

This wiki is generated from a bunch of [markdown](https://www.markdownguide.org/) files and is hosted on [GitHub](https://github.com/unora-project/unora-project.github.io) using GitHub Pages. Pull requests (PRs) are welcome, which is the way to contribute to the data hosted here.

## Admonition Consistency

When giving the reader notices or warnings in things like quest guides, follow this format for consistency sake:

### General info

When providing tips or relaying other types of general information to the reader.

```
!!! note ""

[info text]

!!! note ""
```

Example:

!!! note ""

[info text]

!!! note ""

### Story summaries

This abuses admonition rendering to just use the coloring of the admonition with no icons.

```
!!! info ""

[summary text]

!!! info """
```

Example:

!!! info ""

[summary text]

!!! info ""

### Party warning

Several quests require being in a party in order to do them. It's nice to let the reader know ahead of time so they understand they can't solo something.

```
??? warning ":octicons-people-16: Party required!"

    [help information]
```

Example:

??? warning ":octicons-people-16: Party required!"

    [help information]

### Combat warnings

```
??? danger ":material-sword-cross: Combat incoming!"

    [helpful text]
```

Example:

??? danger ":material-sword-cross: Combat incoming!"

    [helpful text]

### Boss fight warnings

```
??? danger ":material-emoticon-devil-outline: Boss room ahead!"

    [helpful text]
```

Example:

??? danger ":material-emoticon-devil-outline: Boss room ahead!"

    [helpful text]

### Repeatable quest

If a quest is repeatable, use the following format:

```
!!! example ":fontawesome-solid-repeat: Repeatable every X hours"
```

Example:

!!! example ":fontawesome-solid-repeat: Repeatable every X hours"
