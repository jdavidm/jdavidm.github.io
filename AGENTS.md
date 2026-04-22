# Agent Instructions

## Creating Pull Requests
When asked to create, publish, or submit a Pull Request (PR), **DO NOT use `git push`**. Standard git pushing is blocked in this environment and will fail.

Instead, you **MUST** use the built-in `submit` tool provided in your environment. The `submit` tool handles packaging the changes, pushing the branch, and creating the pull request on GitHub correctly.

## Important: Commit Before Submitting
Before calling the `submit` tool to create a Pull Request, you **MUST** ensure that you have locally committed all of your changes to your working branch (e.g., using `git add` and `git commit`).

The `submit` tool pushes your local commits to the remote. If you have not committed your file modifications locally, the PR will fail to create or will be empty.
