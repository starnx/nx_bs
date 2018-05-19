# 新项目配置

## pip 配置国内镜像下载源

### 临时

```python
# 临时使用，添加“-i”或“--index”参数
pip install -i http://pypi.douban.com/simple/ flask
```

### 永久

- cd: C:\Users\你的用户名\
- 创建: pip目录
- 创建: pip.ini文件（注意：以UTF-8 无BOM格式编码）
- 写入以下内容并保存

```text
[global]
index-url=http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
```

**注意:** trusted-host 选项为了避免麻烦是必须的，否则使用的时候会提示不受信任，或者添加“--trusted-host=mirrors.aliyun.com”选项

>更多的国内镜像

```text
http://pypi.douban.com/simple/ 豆瓣
http://mirrors.aliyun.com/pypi/simple/ 阿里
http://pypi.hustunique.com/simple/ 华中理工大学
http://pypi.sdutlinux.org/simple/ 山东理工大学
http://pypi.mirrors.ustc.edu.cn/simple/ 中国科学技术大学
https://pypi.tuna.tsinghua.edu.cn/simple 清华
```

## VSCode 配置

```text
{
    "files.autoSave": "afterDelay",
    "workbench.iconTheme": "vscode-icons",
    "python.venvPath": "D:/virtualenv",
    "code-runner.executorMap": {
            "python": "$pythonPath $fullFileName",
        },
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Args": ["--max-line-length=248"],
}
```
