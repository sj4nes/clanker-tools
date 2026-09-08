= Methods <methods>

Participants completed two sessions. The design is summarized in @fig:design and
the outcomes in @tab:outcomes.

#figure(
  rect(width: 60%, height: 3cm, stroke: 0.5pt)[
    #align(center + horizon)[Session 1 #sym.arrow.r Session 2]
  ],
  caption: [Study design. Replace this placeholder with `image("figures/design.png")`.],
) <fig:design>

#figure(
  table(
    columns: (auto, 1fr, 1fr),
    align: (left, center, center),
    stroke: none,
    table.hline(),
    table.header([Measure], [Control], [Intervention]),
    table.hline(stroke: 0.5pt),
    [Recall],        [0.62],   [0.74],
    [Reaction time], [512 ms], [486 ms],
    table.hline(),
  ),
  caption: [Primary outcomes by condition.],
  kind: table,
) <tab:outcomes>

As @methods notes, all analyses were pre-registered.
