# git-vscode-wsl2-practice

用于练习 Git 提交和 GitHub 上传的 PySide6（Qt）桌面程序。

## 运行

需要 Python 3.10 或更高版本。在项目目录执行：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe 1.py
```

如果当前 Python 已安装 PySide6，也可以直接运行 `python 1.py`。

## 功能

- 输入姓名，点击“打个招呼”或按回车显示问候。
- 未输入姓名时使用“朋友”作为称呼。
- 状态栏记录问候次数，“重置”按钮清空输入和计数。

程序只在本地运行，不会自动执行 Git 提交或推送。代码提交后，可手动运行
`git push` 上传到当前分支已配置的远端。
