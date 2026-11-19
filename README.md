# koushilmp

A marketplace of Claude skills by Koushil.

## Skills

| Skill | What it does |
| --- | --- |
| **trailhead** | Generates complete, beginner-to-expert documentation and learning guides on any topic. Produces a README, structured index, progressive chapters (beginner, intermediate, advanced, expert), diagrams and images, examples, exercises, and a glossary. |

## Install

### Claude Code (plugin marketplace)

```
/plugin marketplace add koushil-mankali/koushilmp
/plugin install koushil-skills@koushilmp
```

### Skills CLI

```bash
npx -y skills add koushil-mankali/koushilmp --skill trailhead
```

### Manual

Copy the skill folder into your skills directory:

```bash
git clone https://github.com/koushil-mankali/koushilmp.git
mkdir -p ~/.claude/skills
cp -r koushilmp/skills/trailhead ~/.claude/skills/
```

Restart Claude Code and the skill is picked up automatically.

## Usage

Just ask in plain language. Trailhead triggers on requests like:

- "Create a zero-to-expert guide on Kubernetes"
- "Write complete documentation for learning Rust"
- "Build a handbook with an index and README for GraphQL"

### What you get

```
<topic>/
├── README.md          # Overview and how to use the guide
├── INDEX.md           # Full table of contents
├── 01-beginner/
├── 02-intermediate/
├── 03-advanced/
├── 04-expert/
├── assets/            # Diagrams and images
├── exercises/
└── GLOSSARY.md
```

## Repository structure

```
koushilmp/
├── .claude-plugin/
│   └── marketplace.json
├── skills/
│   └── trailhead/
│       └── SKILL.md
├── README.md
└── LICENSE
```

## Adding more skills

1. Create `skills/<new-skill>/SKILL.md` with `name` and `description` frontmatter.
2. Add `"./skills/<new-skill>"` to the `skills` array in `.claude-plugin/marketplace.json`.
3. Commit and push.

## Contributing

Issues and pull requests are welcome. For a new skill or a change to an existing one, please describe the use case and include an example prompt.

## License

Released under the [MIT License](LICENSE).
