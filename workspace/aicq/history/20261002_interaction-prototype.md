# UX-P01: an embedded review exchange

User direction: prioritize interaction design with HTML prototypes before more
heavyweight engineering. This experiment is separate from M1–M6. M1 remains
complete, M2 incomplete, and one M2 retry remains. No hosting action, real message,
sharing permission or live integration was performed.

## Deliverable and question

Self-contained source: `mcp/ui/prototypes/interaction-v1.html` on throwaway local
branch `kublascratchpad/ux-prototype-v1`. Canonical artifact:
`workspace/aicq/prototypes/interaction-v1.html`. SHA256:
`09bf3b6436b0c3a7c07757caa721f51eba41a9bb7e68862c98f31b7fd09445e3`.

Can an owner share selected work, follow the exchange and use returned work
without managing a task system? The prototype pairs a simulated ChatGPT host
with an AICQ roster and exchange panel. Asking the host to share sends directly;
optional preview and a receipt expose the shared copy and context. The returned
revision preserves provenance and leaves one unresolved availability question.
Changed source triggers reconciliation rather than overwrite.

State is held only in memory. No dependencies, requests, local storage, credentials
or backend exist in this HTML. Double-click the file; loopback port 6188 also
served it for browser evaluation. All fictional contacts, invitation acceptance,
retrieval, replies and new sessions are simulations. Reload loses state.

## Recorded evaluation

Run `ux-p01-1708a921-7528-45d5-b104-48e3eec259e6` used the existing owner annotation.
The 30-minute experiment override and independent state were saved and read back
before RUN_START. One agent performed Nurse, Coordinator and Generator roles,
then a separate browser evaluation pass. Actual receipt IDs are in
`20261002_interaction-prototype-evidence.json`; all events were read back.

Observed through real browser controls:

- Direct host request shares without a second approval. Optional edited preview
  shows and sends the actual custom question.
- Waiting remains distinct from observed retrieval and working.
- Clarification accepts an answer; pause disables simulated recipient actions;
  resume restores the previous state.
- Returned changes update the current document to v4, with webinar October 19.
- Newer source v4 keeps launch October 20; reconciliation produces v5 with
  webinar October 22. Alice's original v3 proposal stays inspectable.
- A simulated fresh host chat retains the exchange and retrieves its summary.
- Ordinary notes survive contact switching; mock invitations add a sample contact.
- Desktop 1380px, narrow default 784px and mobile 390px rendering were inspected.
  Final browser log inspection returned no console errors. Temporary viewport
  overrides were reset. The review walkthrough was left open for the owner.

Browser refinement: collapse the packet after sending to keep replies visible;
keep its draft question synchronized; make contact names accessible on mobile;
remove the second mandatory sharing click from the ordinary host request. The
final browser pass exercised changed controls. One GENERATE receipt contains
an accidental `529?` hint, not a valid source identifier; the final REVIEW records
its correction and the exact final source hash above.

Screenshot: `docs/prototypes/interaction-v1-browser.png` (reconciled result).
Mechanical acceptance passed. The design remains unvalidated by Michael.
ChatGPT's real embedded host, sharing isolation, persistence, polling and agent
execution are not verified by this experiment. No product MARK_COMPLETE exists.

## Next design iteration

Watch Michael try the walkthrough without explaining each control. Assess whether
people or current work should lead navigation, whether the returned revision is
useful without extra explanation, and whether the inspectable packet is enough
for confidence about sharing. Try alternatives in throwaway HTML before porting
any validated interaction into the application. The real invitation flow remains
to design; the mock is only a navigation affordance.
