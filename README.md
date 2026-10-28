# 30 Days of JavaScript: Learn by Building

A personal coding challenge for practicing **HTML, CSS, and vanilla JavaScript** through hands-on projects. Follow along, explore the code, and build your own versions as you learn.

The goal is to get better at turning ideas into working applications: breaking down problems, responding to user input, debugging, and making your own implementation decisions.

**Status:** Work in progress. Day 1 is currently available; this repository does not yet contain all 30 projects.

## Who is this for?

This challenge is for learners who know some HTML and CSS and want more practice with JavaScript. You don't need to be an expert, but familiarity with variables, functions, and basic HTML will help you get started.

These are learning projects. Treat the code as something to explore, question, and improve as you develop your own skills.

## Projects

| Day | Project | JavaScript practice | Brief |
| --- | --- | --- | --- |
| 1 | [Interactive Color Playground](./Day%201%20%E2%80%94%20Interactive%20Color%20Playground/) | DOM selection, event listeners, input handling, random values, HEX colors, and clipboard promises | [Read the challenge](./Day%201%20%E2%80%94%20Interactive%20Color%20Playground/note.md) |

The Day 1 brief is written in Indonesian. The interface uses English labels.

## Get started

You need a modern web browser and a code editor. The current project requires no package installation, build step, backend, or API key.

1. Download this repository using **Code → Download ZIP** on GitHub and extract it, or clone it with Git:

   ```sh
   git clone https://github.com/Lopn17/30-days-of-javascript-beginner-to-advance.git
   cd 30-days-of-javascript-beginner-to-advance
   ```

2. Open the repository folder in your code editor.
3. Open `Day 1 — Interactive Color Playground/index.html` in your browser to try the project.

For clipboard functionality, serve the project through a local development server, such as the Live Server extension in VS Code. Open the page using the server's `localhost` address. Clipboard access depends on your browser's permissions and secure-context rules, so opening the file directly may not support copying.

## Try Day 1

- Use the color picker to change the page background.
- Click **Random Color** to generate a color and display its HEX code.
- After choosing or generating a color, click the displayed HEX code to copy it.
- Click **Reset** to return the background to white.

The JavaScript lives in the `<script>` section of `index.html`, and the current styling lives in its `<style>` section. The HTML also references `style.css`, but that file is not included in the repository.

## Use this repo to learn

1. **Read the brief first.** Start with the project's `note.md` and identify what the finished application should do.
2. **Try building your own version.** Break the requirements into smaller tasks and make an initial attempt before reading the existing solution.
3. **Test your work.** Use the brief's acceptance criteria, try repeated interactions, and inspect errors in your browser's developer console.
4. **Compare approaches.** Explore the code here and explain what each event listener changes on the page.
5. **Improve something.** Fix an edge case, reorganize the code, or take on a stretch goal from the brief.

For Day 1, useful questions to investigate include:

- Do the background, color picker, and HEX label agree when the page first loads and after a reset?
- What happens if you try copying before selecting a color, or if clipboard access is unavailable?
- Is the text readable on both very light and very dark backgrounds?

Take your time. Each “day” is a project milestone, not a deadline.

## Create your own challenge

The [30-Day Coding Project Architect prompt](./AI_Prompt_30_Days_Coding_Project_Architect.md) contains the instructions used to request progressively harder project briefs from an AI assistant.

To use it, copy the prompt into your preferred AI assistant, start with Day 1, and request the next day when you are ready. It asks for requirements and acceptance criteria while leaving the implementation to you. Generated projects may differ from the ones in this repository.

## Repository structure

```text
.
├── README.md
├── AI_Prompt_30_Days_Coding_Project_Architect.md
└── Day 1 — Interactive Color Playground/
    ├── index.html
    └── note.md
```

## Feedback

Found a bug or an unclear instruction? [Open an issue](https://github.com/Lopn17/30-days-of-javascript-beginner-to-advance/issues) with what you tried, what you expected, and what happened. Suggestions that help other learners are welcome.
