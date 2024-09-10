# HG_zuoyeben_A
必修一作业本

# Usage

- xoj后台选择试题建立试卷，在试卷管理页就可以导出试题的tex，复制到tex文件
- 试卷中的description就是知识点，需要将markdown转成latex格式，目前使用pandoc，但也不是很完美
  - 下载并安装pandoc
  - 到命令提示符下，运行`md_2_latex.bat`
  - 查找`\subsubsection`替换成\item \textbf；查找`itemize`替换成`compactitem`；删除`\tightlist`；删除各种空格