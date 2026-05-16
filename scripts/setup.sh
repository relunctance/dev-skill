#!/bin/bash
# dev-skill setup.sh — 安装前先检查环境，缺失则引导安装
#
# 用法：
#   bash setup.sh

set -e

echo "=== dev-skill 环境检查 ==="

# 检查 python3
if command -v python3 >/dev/null 2>&1; then
    PYTHON=$(command -v python3)
    VERSION=$(python3 --version 2>&1)
    echo "  python: $VERSION ($PYTHON)"
else
    echo "❌ python3 未找到"
    echo ""
    echo "请先安装 Python3："
    echo "  macOS:    brew install python3"
    echo "  Ubuntu:  sudo apt update && sudo apt install python3 python3-pip"
    echo "  Windows:  https://www.python.org/downloads/ (安装时勾选 Add to PATH)"
    echo "  其他:     https://www.python.org/downloads/"
    echo ""
    echo "安装完成后重新运行："
    echo "  bash setup.sh"
    exit 1
fi

# 检查 git
if command -v git >/dev/null 2>&1; then
    VERSION=$(git --version 2>&1)
    echo "  git:     $VERSION"
else
    echo "❌ git 未找到"
    echo ""
    echo "请先安装 Git："
    echo "  macOS:    brew install git"
    echo "  Ubuntu:  sudo apt update && sudo apt install git"
    echo "  Windows:  https://git-scm.com/downloads"
    echo ""
    echo "安装完成后重新运行："
    echo "  bash setup.sh"
    exit 1
fi

echo ""
echo "✅ 环境检查通过"
echo ""

# 执行 Python 安装脚本
echo "运行安装脚本..."
python3 "$(dirname "${BASH_SOURCE[0]}")/install.py"
