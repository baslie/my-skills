# my-skills

Custom skills collection for [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code).

## Skills

| Skill | Description |
|-------|-------------|
| [wireframe-builder](./wireframe-builder) | Generate lo-fi wireframes as single HTML files with Tailwind CSS. Creates grayscale mockups for landing pages, dashboards, forms, e-commerce, admin panels, and more. |

## Installation

### Global (all projects)

```bash
claude skill install --global https://github.com/baslie/my-skills/wireframe-builder
```

### Local (current project)

```bash
claude skill install https://github.com/baslie/my-skills/wireframe-builder
```

## Usage

After installation, invoke the skill in Claude Code:

```
/wireframe-builder
```

Or describe what you need:

> "Create a wireframe for a SaaS landing page"

## Structure

Each skill follows the standard structure:

```
skill-name/
├── SKILL.md           # Main skill definition
├── assets/            # Templates, images
└── references/        # Additional documentation
```

## License

MIT
