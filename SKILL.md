---
name: dev-skill
description: 开发类 Skill 套件 — 打包 PLAN / plan-review / task-split / target / git-standards，一键安装
version: "1.0.0"
author: relunctance
license: MIT
category: development
tags:
  - development
  - skill-suite
metadata:
  hermes:
    platforms:
      claude_code: true
      openclaw: true
      hermes: true
      cursor: true
      vscode: true
---

# dev-skill

开发类 Skill 套件 — 一键安装所有开发流程相关的 skill。

## 包含的 Skill

| Skill | 用途 |
|-------|------|
| `PLAN skill` | 生成 PLAN.md — 项目规划文档 |
| `plan-review-skill` | 评审 PLAN.md — 锚点评审 + 存档 |
| `task-split-skill` | 拆解任务 — 锚点拆解 + L3 验收标准 |
| `target-skill` | 执行追踪 — 检查点 + 抗偏移 + 质量门禁 |
| `git-standards-skill` | Git 规范 — commit/push/分支策略 |
| `base-skill` | Agent 初始化套件（14 个核心 skills） |

## 四 Skill 联动

```
PLAN skill → plan-review-skill → task-split-skill → target-skill
```

| Skill | 职责 | 产物 |
|-------|------|------|
| PLAN skill | 生成 PLAN.md | `docs/PLAN.md` |
| plan-review-skill | 评审 M1 | `docs/reviews/M1评审结果.md` + `.target-trigger` |
| task-split-skill | 锚点拆解 | `.task-split.json` |
| target-skill | 执行追踪 | `.target-state.json` |

## 安装

```bash
git clone https://github.com/relunctance/dev-skill.git ~/repos/dev-skill
cd ~/repos/dev-skill
bash scripts/setup.sh
```

### ⚠️ 重要：dev-skill 自身也需安装到 profile skills 目录

`setup.sh` 只安装子 skill（base-skill / plan-review-skill / dev-std-skill），**dev-skill 自身**需要手动 link 到 profile skills 目录：

```bash
mkdir -p ~/.hermes/profiles/yutu/skills/dev-skill
ln -sf ~/repos/dev-skill/SKILL.md ~/.hermes/profiles/yutu/skills/dev-skill/SKILL.md
```

> 注意：hermes CLI `skills install` 默认装到全局 `~/.hermes/skills/`，yutu profile 的 skills 目录是 `~/.hermes/profiles/yutu/skills/`，两者不同。dev-skill 必须放在 profile 目录才能被 yutu 加载。

## 触发条件

用户说：
- `安装开发套件`
- `初始化开发环境`
- `安装 dev-skill`
- `开发环境准备`
