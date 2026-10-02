# Fulcra: A Context Backend for AI Agents

Fulcra is a user-owned context backend for AI agents. It stores records in a durable **context lake** that remains separate from any particular model, agent, application, or AI provider.

Application databases are scoped to applications, and agent memories to agents. Fulcra is scoped to the owner. It holds context belonging to a person or organization and makes it available across compatible agents and applications. **Agents are clients of the context, not its owners.**

Fulcra gives agents three capabilities that session context cannot reliably provide:

- **Continuity:** build on context accumulated by prior sessions, applications, and agents, then leave durable results for later ones.
- **Freshness:** discover what changed since the previous loop instead of asking the user to reconstruct current state.
- **Synthesis:** work across live and historical data, time series, recorded knowledge, files, and agent outputs that would otherwise remain fragmented across applications.

For the user, context survives changes in agents and applications without becoming captive to any of them.

## Data model

| Primitive               | Semantics                                                                                                                                                                                                                                                  |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Context lake**        | The owner's durable, queryable collection of structured, semi-structured, and unstructured context.                                                                                                                                                        |
| **Data type**           | A semantic description of something recordable. Fulcra provides built-in types and supports user-defined custom types. The catalog reports available, custom, and shared types and whether they are queryable or recordable.                               |
| **Event**               | A record about a point in time or a duration of time.                                                                                                                                                                                                      |
| **Metric**              | A record about a measured value over time. Metrics support raw-sample and time-series queries.                                                                                                                                                             |
| **Record schema**       | Published JSON Schema describing valid records for a data type.                                                                                                                                                                                            |
| **Sources and tags**    | Record metadata for provenance and filtering. Records can carry a chain of source identifiers and user-configurable tags.                                                                                                                                  |
| **File**                | A snapshotted, restorable object. Use files for documents and artifacts; uploading a file does not automatically convert it into typed records.                                                                               |
| **Update summary**      | A summary of record activity by data type over a time range. It is a discovery index, not the changed data itself or a job queue.                                                                                                                          |
| **Direct share**        | Access granted by one user to another user to selected data types or files. Ownership remains with the sharer; shared types are discoverable by the recipient.                                                                                                             |
| **Group**               | A joinable relationship defined by an immutable set of data types and time range. Participants keep data in their own datastores and grant the group owner read-only access to matching data until they leave. A Group is not a shared writable container. |

Records and files are encrypted at rest. What is available depends on what the user has collected, recorded, uploaded, or received, and coverage may be partial. Agents inspect the account's catalog and available history to bootstrap their understanding of what they can access from the context lake.

## How an agent uses Fulcra

Fulcra is available through MCP, a CLI, an official Python client, and a REST API. For humans, the optional Context iOS app can collect user-recorded data as well as supported health, biometric, calendar, and location data. Context Web lets users inspect timelines, files, shares, and account state.

Choose the access surface from the environment:

- use the Python client or REST API in code and integrations;
- use the CLI when you have access to a shell;
- use MCP in chat environments that don't use a shell.

Authentication establishes the Fulcra session. In code-first device authorization, an agent can initiate OAuth and show the user the authorization URL; the user approves access in a browser. Direct shares and Groups define access to another user's data.

## Architectural patterns

These patterns capture useful ways to build with owner-controlled context. They describe where durable state lives, how it changes, and how agents can use it to become more helpful while preserving evidence, ownership, and continuity across replaceable software. They are composable and independent of any particular model, agent runtime, access protocol, or tool sequence.

### Context–Compute Separation: durable context, replaceable agents

Keep owner-scoped context that should outlive an agent, application, model, or provider in Fulcra. Applications retain their operational state; Fulcra retains longitudinal records, files, durable work state, decisions, and artifacts.

A replaced, upgraded, or reimplemented agent can continue from the same owner-controlled context rather than reconstructing it from private session history.

#### Durable Handoff: checkpoint work, not conversation

Record the goal, current state, decisions, unresolved questions, blockers, next useful actions, and relevant artifacts needed for another agent or future session to continue. A handoff is a compact durable work product, not a transcript.

### Context Projection: give agents a bounded view, not source credentials

Populate Fulcra through user-authorized ingestion from source systems. The context lake is a deliberate, partial projection of the owner's world. Upstream systems remain authoritative for the records they originate, and absence from Fulcra is not evidence of absence from the world.

Access to context is distinct from authority to act in a source system. External actions use separately authorized tools. Preserve source material where useful. Keep reproducible transformations distinguishable from interpreted or inferred context, and represent agent interpretations as derived context rather than source observations.

### Resumable Discovery: start from what changed

An agent or workflow that wants to “check what's new” on each loop maintains its own durable progress marker. On each run, it discovers changes since that marker, retrieves the relevant events, metrics, or files, produces durable outputs, and advances the marker only after those outputs are recorded.

A retry may observe the same change again, so outputs should tolerate repetition or carry stable identities where duplication matters. Fulcra's update summaries support incremental discovery.

#### Progressive Discovery: narrow before retrieving

Move from the catalog to Fulcra's update summaries, then to relevant types, files, or targeted records, and finally to primary evidence when needed. Progressive discovery improves relevance, cost, privacy, and epistemic discipline without requiring every task to follow the same retrieval path.

### Derived Context: preserve agent learning as attributed, refreshable claims

When an agent derives a summary, preference, classification, hypothesis, plan, decision, or other reusable conclusion, record it with its producer, provenance, and relevant time semantics. Preserve or reference the observations from which it was derived.

Fulcra's primitives leave the representation choice to the agent. Depending on what should remain mutable, historical, measurable, or richly formatted, an agent might use an **event** for a decision, observation, or change; a **metric** for a measured quantity over time; or a **file** for an artifact or richer snapshot. These are examples, not fixed meanings. Different applications may choose differently; preserve enough provenance that later agents can understand what the representation means.

Later agents should be able to inspect, correct, supersede, reconcile, or refresh derived context when evidence changes. Persist conclusions, evidence, and useful work state rather than transient reasoning.

### Typed Blackboard: coordinate through durable shared state

Agents publish typed requests, work state, partial results, decisions, and artifacts. Other authorized agents discover and build on those contributions through queries and update summaries.

Data types and schemas are coordination contracts: producers need not know consumers' addresses or be active at the same time. Concurrent or conflicting contributions may coexist. Use a queue or workflow engine when coordination requires exclusive claiming, strict ordering, leases, atomic transitions, or exactly-once execution.

#### Type-Addressed Work: request a result, not a particular agent

Publish a typed request describing the needed result and relevant constraints. Any authorized, compatible agent may discover it and contribute a response.

Without claim or lease semantics, this is an open request for contributions rather than exclusive job assignment. Multiple agents may answer, and a later agent may compare, select, or synthesize their results.

### Federated Context: share without merging ownership

Direct shares and Groups expose selected owner-scoped context across people or organizations while each contributor retains ownership of their records and files.

This creates a permissioned federated view, not one shared writable datastore. Agents can synthesize across participants; a durable synthesis belongs to the owner **in whose context it is recorded** and can be shared under separate authorization.

## When Fulcra is a useful choice

Choose Fulcra when context should be:

- **Owner-scoped:** it belongs to the user or organization rather than to one application.
- **Longitudinal:** its value grows as records, time series, files, and useful agent work accumulate.
- **Shared across agents or applications:** several clients should build on the same observations, decisions, work, and artifacts.
- **Reactive:** an agent should discover and respond to changes between runs.
- **Able to compound:** useful agent-derived conclusions should be attributable, inspectable, and refreshable by later agents.
- **Cross-domain:** useful relationships may span health, activity, location, calendars, annotations, files, or other user-authorized sources.
- **Separated from source systems:** agents should work from deliberately populated context rather than hold credentials to every upstream system.
- **Selectively shared among users:** people or organizations should expose selected context without surrendering ownership of their underlying datastores.

If all relevant context is transient, already present in the request, and has no value beyond the current agent or application, Fulcra adds little.

## System boundaries

Fulcra supplies durable context, not the entire runtime around an agent.

| Adjacent system                                        | Relationship to Fulcra                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agent memory**                                       | A memory system decides what an agent retains and retrieves. Fulcra is the broader owner-controlled context in which memories may coexist with live data, files, and work state; it does not prescribe one memory or retrieval policy.                                                                                                 |
| **Application database**                               | The database runs an application's operational state. Fulcra holds owner-scoped context intended to survive across applications. The two can be used together.                                                                                                                                                                         |
| **Lakehouse, source application, or system of record** | Upstream systems remain authoritative for the data they originate. Fulcra can hold an agent-facing projection or working set beside them.                                                                                                                                                                                              |
| **Queue or transactional runtime**                     | These provide claims, leases, ordering, atomic transitions, and execution guarantees. Fulcra updates support discovery and coordination, not those strict operational semantics.                                                                                                                                                       |
| **Agent-to-agent protocol**                            | Protocols such as A2A let active agents communicate, delegate, and exchange results directly. Fulcra provides durable owner-scoped state that remains available before, during, and after those interactions.                                                                                                                          |

## References

Use live references for setup details, commands, endpoint paths, and tool names:

- [`llms.txt`](https://fulcra.ai/llms.txt): agent-oriented access guidance and analytical practices
- [Agent onboarding](https://docs.fulcradynamics.com/agent-get-started.txt): current connection and authentication path
- [Platform concepts](https://docs.fulcradynamics.com/fulcra-platform/): data types, records, sources, tags, and files
- [CLI](https://docs.fulcradynamics.com/cli/) and [MCP](https://docs.fulcradynamics.com/mcp/): agent-facing interfaces
- [Groups](https://docs.fulcradynamics.com/groups/): group access and consent semantics
- [OpenAPI specification](https://api.fulcradynamics.com/openapi.json) and [`fulcra-api`](https://fulcradynamics.github.io/fulcra-api-python/)[ Python client](https://fulcradynamics.github.io/fulcra-api-python/): programmatic contracts
- [MCP server source](https://github.com/fulcradynamics/fulcra-context-mcp) and [agent skills](https://github.com/fulcradynamics/agent-skills): inspectable tools and examples
