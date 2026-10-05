# DOC-P07 — GitHub Mermaid rendering repair

GitHub browser preview at `a233bb5` reproduced “Unable to render rich display”
with a parse error on line 10. The final message contained a semicolon:
`Q-->>A: Bob has v7; Friday review arranged`.

Generator replaced it with a period and published isolated commit `dd42278`.
The semicolon was parsed as a statement separator. Separate Evaluator reloaded
the actual GitHub main document through Computer Use; GitHub’s Mermaid iframe
rendered all three participants and all six messages, including “Bob has v7.
Friday review arranged”. Its expanded diagram also rendered. A screenshot is
saved locally at `.local/mermaid-render-fixed.jpg`; SHA256:
`25aac408856e717f76d101c178da5fc473f0edfd66daba71afae32bff08a5ef4`.

This browser pass corrects the previous documentation review’s limitation:
Markdown parsing did not evaluate Mermaid syntax. Actual GitHub rendering is the
regression check for this one-character change. Broad instrumentation and new
application tests are unnecessary for an isolated documentation delimiter.
`git diff --check` passed. No wording, spec, application or prototype change beyond
the punctuation repair; M2 remains incomplete with one retry.

Independent run `doc-p07-3351ae3c-170d-4848-8590-469651ed32cf` uses the existing owner annotation,
sequential roles, default 15-minute timeout and two retries. Canonical bytes and
terminal event read-back are recorded below when completed.

Run closed at 2026-10-05T23:34:48.249486+00:00, no retries. REVIEW, MARK_COMPLETE and
RUN_COMPLETE were read back; terminal `9f381f36-a1cf-5956-9204-60a3f9432125`. Three canonical
files byte-matched before completion; final closed-state mirrors sync separately.
